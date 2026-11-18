import sys, os, json, time, subprocess, urllib.request
import numpy as np, cv2
SRC, OUT = sys.argv[1], sys.argv[2]; N = int(sys.argv[3]) if len(sys.argv) > 3 else 3
os.makedirs(OUT, exist_ok=True); T0 = time.time()
def log(m): print(f"[{time.time()-T0:6.1f}s] {m}", flush=True)

# 1) konusmayi kelime kelime metne cevir (yerel, ucretsiz)
WHISPER = os.environ.get("KLIP_WHISPER", "small")  # guclu makinede: large-v3
THREADS = int(os.environ.get("KLIP_THREADS", max(4, (os.cpu_count() or 8) // 2)))
CACHE = f"{SRC}.{WHISPER}.transkript.json"  # ayni yayini farkli ayarlarla tekrar islerken yeniden yaziya cevirmez
if os.path.exists(CACHE):
    _c = json.load(open(CACHE, encoding="utf-8")); S = _c["S"]; DUR = _c["dur"]
    for s in S: s["w"] = [tuple(w) for w in s["w"]]
else:
    from faster_whisper import WhisperModel
    pcm = subprocess.run(["ffmpeg","-v","error","-i",SRC,"-vn","-ac","1","-ar","16000","-f","f32le","-"], capture_output=True, check=True).stdout
    segs, info = WhisperModel(WHISPER, device="cpu", compute_type="int8", cpu_threads=THREADS).transcribe(
        np.frombuffer(pcm, dtype=np.float32), vad_filter=True, word_timestamps=True)
    S = [dict(a=s.start, b=s.end, t=s.text.strip(), w=[(w.word, w.start, w.end) for w in s.words]) for s in segs]
    DUR = info.duration
    json.dump({"S": S, "dur": DUR}, open(CACHE, "w", encoding="utf-8"))
log(f"transkript: {len(S)} parca, {DUR:.0f} sn ses")

# 2) 25-45 sn'lik aday pencereler
C = []
for i in range(len(S)):
    j = i
    while j < len(S) and S[j]["b"] - S[i]["a"] < 25: j += 1
    if j < len(S) and S[j]["b"] - S[i]["a"] <= 45:
        C.append((S[i]["a"], S[j]["b"], " ".join(x["t"] for x in S[i:j+1])))

# 3) yuz bulucu: konusmaci kamerada degilse (slayt) o pencereyi ele
det = cv2.FaceDetectorYN.create(os.path.join(os.path.dirname(os.path.abspath(__file__)), "yunet.onnx"), "", (1280, 720), 0.6)
cap = cv2.VideoCapture(SRC); W, H = int(cap.get(3)), int(cap.get(4)); det.setInputSize((W, H)); FC = {}
def face_box(t):  # (merkez x, merkez y, genislik) ya da None
    k = round(t*2)/2
    if k not in FC:
        cap.set(cv2.CAP_PROP_POS_MSEC, k*1000); ok, f = cap.read(); FC[k] = None
        if ok:
            _, fa = det.detect(f)
            if fa is not None and len(fa): r = fa[np.argmax(fa[:, 14])]; FC[k] = (float(r[0] + r[2]/2), float(r[1] + r[3]/2), float(r[2]))
    return FC[k]
# yayincinin/konusmacinin tipik yuzu: videonun geneline yayilmis orneklerin ortancasi
_ref = [b for t in np.arange(5, DUR, max(5.0, DUR/120)) if (b := face_box(t))]
REF = tuple(np.median(np.array(_ref), axis=0)) if _ref else None
DUZEN = os.environ.get("KLIP_DUZEN", "konusma")  # konusma: yuze gore kirp | oyun: ustte yuz kamerasi, altta oyun
def speaker(t):  # yuz var ve boyutu/konumu tipik yuze benziyor mu (slayttaki fotograf yuzlerini eler)
    b = face_box(t)
    if b is None or REF is None: return None
    if abs(b[2] - REF[2]) > 0.45 * REF[2]: return None
    if DUZEN == "oyun" and (abs(b[0] - REF[0]) > 0.15 * W or abs(b[1] - REF[1]) > 0.15 * H): return None
    return b
def face_x(t): b = speaker(t); return b[0] if b else None
def ratio(a, b):
    if DUZEN == "oyun" and REF is None: return 1.0  # yuz kamerasi olmayan yayin: yuz sarti yok
    v = [speaker(t) is not None for t in np.arange(a, b, 1.0)]; return sum(v)/len(v)  # her saniye bak: slayta gecis kacmasin

# 4) yerel LLM (ollama) her pencereye 1-10 puan verir
_LL = None
def _llama(p):
    global _LL
    if _LL is None:
        from llama_cpp import Llama
        _LL = Llama(model_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "qwen3-4b.gguf"), n_ctx=4096, n_threads=THREADS, verbose=False)
    r = _LL.create_chat_completion(messages=[{"role": "user", "content": p}], temperature=0, response_format={"type": "json_object"}, max_tokens=120)
    return json.loads(r["choices"][0]["message"]["content"])
def puan(text):
    p = 'Bu konusma parcasi tek basina 9:16 kisa videoda izleyiciyi tutar mi? Sadece JSON ver: {"score": 1-10 tam sayi, "hook": "en fazla 8 kelimelik baslik"}\n\n' + text[:1500]
    model = os.environ.get("KLIP_MODEL", "qwen3clip")
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": p}], "stream": False, "format": "json", "keep_alive": "30m"}).encode()
    try:
        # buyuk model ilk cagrida diskten yuklenir; bekleme suresi uzun tutulur
        r = urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:11434/api/chat", body, {"Content-Type": "application/json"}), timeout=int(os.environ.get("KLIP_LLM_TIMEOUT", "900")))
        return json.loads(json.loads(r.read())["message"]["content"])
    except OSError as e:
        detay = e.read().decode(errors="replace")[:300] if hasattr(e, "read") else str(e)
        try:
            import llama_cpp  # noqa: F401  (yalnizca kuruluysa yedek yola gec)
        except ImportError:
            sys.exit(f"Ollama ile puanlama basarisiz ({model}): {detay}\n"
                     f"Kontrol: 'ollama list' modeli gosteriyor mu, 'ollama run {model} OK' calisiyor mu?")
        return _llama(p)  # ollama yoksa ayni modeli llama-cpp-python ile calistir
P = []
for a, b, t in C[::max(1, len(C)//24)]:
    if ratio(a, b) >= float(os.environ.get("KLIP_YUZ_ORANI", "0.8")):  # yayinci klibin cogunda gorunmeli
        o = puan(t); P.append((float(o["score"]), a, b, o.get("hook", ""), t))
log(f"{len(C)} aday, {len(P)} tanesi yuzlu, hepsi puanlandi")
P.sort(reverse=True); K = []
for p in P:
    if all(p[2] < k[1] or p[1] > k[2] for k in K): K.append(p)
    if len(K) == N: break

# 5) kes, 9:16 kirp (konusmacinin yuzune), kelime kelime altyazi yak
def ts(x): return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
for n, (sc, a, b, hook, t) in enumerate(sorted(K, key=lambda k: k[1]), 1):
    xs = [x for tt in np.arange(a, b, 0.5) if (x := face_x(tt)) is not None]
    cw = int(H*9/16)//2*2; x0 = int(min(max(np.median(xs) - cw/2, 0), W - cw)) if xs else (W - cw) // 2
    ws = [w for s in S for w in s["w"] if w[1] >= a-.05 and w[2] <= b+.05]
    ev = "".join(f"Dialogue: 0,{ts(max(ws[k][1]-a,0))},{ts((ws[k+3][1] if k+3 < len(ws) else ws[-1][2])-a)},K,,0,0,0,,{''.join(w[0] for w in ws[k:k+3]).strip().upper()}\n" for k in range(0, len(ws), 3))
    open(f"{OUT}/klip{n}.ass", "w").write("[Script Info]\nPlayResX: 720\nPlayResY: 1280\n[V4+ Styles]\nFormat: Name,Fontname,Fontsize,PrimaryColour,OutlineColour,Bold,BorderStyle,Outline,Alignment,MarginV\nStyle: K,Sans,54,&H00FFFFFF,&H00101010,-1,1,4,2,260\n[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n" + ev)
    if DUZEN == "oyun" and REF is None:  # yuz kamerasi yok: oyunun ortasini tam dikey kirp
        video = ["-vf", f"crop={cw}:{H}:{(W - cw) // 2}:0,scale=720:1280,subtitles={OUT}/klip{n}.ass"]
    elif DUZEN == "oyun":  # ustte yuz kamerasi (720x448), altta oyunun ortasi (720x832)
        fw = REF[2] * 3.2; fh = fw * 448 / 720
        fx = int(min(max(REF[0] - fw/2, 0), W - fw)); fy = int(min(max(REF[1] - fh/2, 0), H - fh))
        gw = int(H * 720 / 832) // 2 * 2; gx = (W - gw) // 2
        vf = (f"[0:v]split=2[c][g];[c]crop={int(fw)//2*2}:{int(fh)//2*2}:{fx}:{fy},scale=720:448[ust];"
              f"[g]crop={gw}:{H}:{gx}:0,scale=720:832[alt];[ust][alt]vstack,subtitles={OUT}/klip{n}.ass[v]")
        video = ["-filter_complex", vf, "-map", "[v]", "-map", "0:a?"]
    else:
        video = ["-vf", f"crop={cw}:{H}:{x0}:0,scale=720:1280,subtitles={OUT}/klip{n}.ass"]
    subprocess.run(["ffmpeg","-v","error","-y","-ss",f"{a:.2f}","-to",f"{b:.2f}","-i",SRC] + video + ["-c:v","libx264","-preset","veryfast","-crf","23","-c:a","aac",f"{OUT}/klip{n}.mp4"], check=True)
    log(f"klip{n}: {a:.0f}-{b:.0f} sn, puan {sc:.0f}, baslik: {hook}")
log("bitti")
