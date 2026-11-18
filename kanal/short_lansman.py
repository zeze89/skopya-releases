#!/usr/bin/env python3
"""GTA 6 lansman gecesi Twitch istatistikleri: 1080x1920, 30 fps, ~21 sn, sessiz dikey video.

Veriler yayinci/ klasorundeki Twitch API taramalarindan elle aktarildi (UTC).
Kullanim: python3 short_lansman.py cikti.mp4
"""
import subprocess, sys
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
OUT = sys.argv[1] if len(sys.argv) > 1 else "lansman.mp4"

# --- veri (Twitch Helix, 18 Kasim 2026, UTC) ---
TIMELINE = [("20:04", 12611), ("21:52", 16717), ("23:06", 29166)]
VIEWERS = 2983026
LANGS = [("English", 849833), ("Spanish", 844281), ("German", 306173),
         ("Portuguese", 260697), ("French", 196450), ("Russian", 180048)]
TOP = [("IlloJuan", 344103), ("Rubius", 239275), ("alanzoka", 181605)]
SOURCE = "Source: Twitch API snapshots, Nov 18 2026 (UTC)"
HANDLE = "ZeteraClipso"

# --- gorunum ---
BG, BG2 = (14, 12, 32), (38, 18, 64)
PINK, TEAL, SUN, WHITE, MUTED = (255, 79, 154), (40, 214, 200), (255, 184, 76), (245, 243, 255), (170, 160, 205)
# kalin ve yari kalin yazi tipi adaylari (Linux, Windows); ilk bulunan kullanilir
FD = ["/usr/share/fonts/opentype/inter/InterDisplay-Black.otf", "C:/Windows/Fonts/seguibl.ttf",
      "C:/Windows/Fonts/ariblk.ttf", "DejaVuSans-Bold.ttf"]
FB = ["/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf", "C:/Windows/Fonts/seguisb.ttf",
      "C:/Windows/Fonts/arialbd.ttf", "DejaVuSans-Bold.ttf"]


def font(paths, size, _c={}):
    k = (paths[0], size)
    if k not in _c:
        for p in paths:
            try:
                _c[k] = ImageFont.truetype(p, size)
                break
            except OSError:
                continue
    return _c[k]


def ease(t):  # 0..1 -> yumusak gecis
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def background():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    for y in range(H):  # dikey gradyan
        a = y / H
        d.line([(0, y), (W, y)], fill=tuple(int(BG[i] * (1 - a) + BG2[i] * a) for i in range(3)))
    return im


BASE = background()


def text(d, xy, s, f, fill, anchor="la"):
    d.text(xy, s, font=f, fill=fill, anchor=anchor)


def chrome(d, t):
    text(d, (W // 2, 120), "GTA 6 LAUNCH NIGHT", font(FD, 64), PINK, "mm")
    text(d, (W // 2, 195), "on Twitch, by the numbers", font(FB, 44), MUTED, "mm")
    text(d, (W // 2, H - 150), SOURCE, font(FB, 30), MUTED, "mm")
    text(d, (W // 2, H - 95), "@" + HANDLE, font(FB, 34), TEAL, "mm")


def fmt(n):
    return f"{int(round(n)):,}"


def scene_timeline(d, t):  # 0-6 sn: canli yayin sayisi artisi
    text(d, (W // 2, 420), "LIVE STREAMS", font(FB, 52), WHITE, "mm")
    peak = TIMELINE[-1][1]
    x0, x1, base_y, top_y = 170, 910, 1350, 700
    for i, (hh, n) in enumerate(TIMELINE):
        p = ease((t - i * 1.2) / 1.4)
        if p <= 0:
            continue
        cx = x0 + (x1 - x0) * i / (len(TIMELINE) - 1)
        h = (base_y - top_y) * (n / peak) * p
        col = PINK if i == len(TIMELINE) - 1 else TEAL
        d.rounded_rectangle([cx - 95, base_y - h, cx + 95, base_y], radius=18, fill=col)
        text(d, (cx, base_y - h - 55), fmt(n * p), font(FD, 58), WHITE, "mm")
        text(d, (cx, base_y + 55), hh + " UTC", font(FB, 40), MUTED, "mm")
    if t > 4.0:
        a = ease((t - 4.0) / 0.8)
        text(d, (W // 2, 1560), f"+{(TIMELINE[-1][1] / TIMELINE[0][1] - 1) * 100:.0f}% in 3 hours",
             font(FD, 70), tuple(int(c * a + BG[i] * (1 - a)) for i, c in enumerate(SUN)), "mm")


def scene_viewers(d, t):  # 6-10 sn: toplam izleyici
    p = ease(t / 2.2)
    text(d, (W // 2, 700), "PEOPLE WATCHING", font(FB, 56), WHITE, "mm")
    text(d, (W // 2, 900), fmt(VIEWERS * p), font(FD, 150), SUN, "mm")
    text(d, (W // 2, 1060), "at the same time", font(FB, 52), MUTED, "mm")
    if t > 2.4:
        text(d, (W // 2, 1300), "across " + fmt(TIMELINE[-1][1]) + " streams", font(FB, 52), TEAL, "mm")


def scene_langs(d, t):  # 10-16 sn: dil siralamasi
    text(d, (W // 2, 420), "VIEWERS BY LANGUAGE", font(FB, 52), WHITE, "mm")
    peak = LANGS[0][1]
    for i, (name, v) in enumerate(LANGS):
        p = ease((t - i * 0.25) / 1.0)
        y = 560 + i * 150
        text(d, (110, y), name, font(FB, 46), WHITE)
        wbar = 820 * (v / peak) * p
        col = PINK if name == "Spanish" else TEAL
        d.rounded_rectangle([110, y + 62, 110 + max(wbar, 4), y + 112], radius=12, fill=col)
        text(d, (970, y), fmt(v * p), font(FD, 46), WHITE, "ra")
    if t > 2.6:
        text(d, (W // 2, 1560), "Spanish is neck and neck", font(FD, 60), SUN, "mm")
        text(d, (W // 2, 1640), "with English", font(FD, 60), SUN, "mm")


def scene_top(d, t):  # 16-21 sn: en buyuk yayinlar
    text(d, (W // 2, 520), "BIGGEST STREAMS RIGHT NOW", font(FB, 50), WHITE, "mm")
    for i, (name, v) in enumerate(TOP):
        p = ease((t - i * 0.4) / 0.9)
        if p <= 0:
            continue
        y = 720 + i * 230
        x = 110 + (1 - p) * 300
        d.rounded_rectangle([x, y, x + 860, y + 180], radius=26, fill=(52, 30, 86))
        text(d, (x + 50, y + 90), f"{i + 1}", font(FD, 90), PINK, "lm")
        text(d, (x + 160, y + 62), name, font(FD, 56), WHITE, "lm")
        text(d, (x + 160, y + 128), fmt(v) + " viewers", font(FB, 42), MUTED, "lm")
    if t > 2.6:
        text(d, (W // 2, 1560), "Follow for daily GTA 6 stats", font(FD, 58), TEAL, "mm")


SCENES = [(0, 6, scene_timeline), (6, 10, scene_viewers), (10, 16, scene_langs), (16, 21, scene_top)]
DUR = SCENES[-1][1]

ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                       "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                       "-pix_fmt", "yuv420p", "-movflags", "+faststart", OUT], stdin=subprocess.PIPE)
for fr in range(DUR * FPS):
    t = fr / FPS
    im = BASE.copy()
    d = ImageDraw.Draw(im)
    chrome(d, t)
    for a, b, fn in SCENES:
        if a <= t < b:
            fn(d, t - a)
    ff.stdin.write(im.tobytes())
ff.stdin.close()
ff.wait()
print("yazildi:", OUT, f"{DUR} sn")
