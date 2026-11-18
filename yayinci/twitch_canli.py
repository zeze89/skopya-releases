#!/usr/bin/env python3
"""Twitch canlı tarama: bir oyun kategorisinde şu an yayında olan orta ölçekli kanalları listeler.

Her çalıştırma o anın görüntüsünü `tarama.csv` dosyasına ekler. Gece boyunca birkaç kez
çalıştırılırsa `ozet.csv` her kanalın kaç taramada görüldüğünü ve ortalama izleyicisini verir.

Gerekenler:
  TWITCH_CLIENT_ID  ortam değişkeni (gizli değil)
  Erişim anahtarı: bulut ortamında ağ vekili Authorization başlığını kendisi ekler.
  Kendi bilgisayarınızda TWITCH_TOKEN ortam değişkenine uygulama erişim anahtarını yazın.

Kullanım:
  python3 twitch_canli.py                                  # Grand Theft Auto VI, 50-500 izleyici
  python3 twitch_canli.py --oyun "Grand Theft Auto V" --min 50 --max 500
"""
import argparse, csv, json, os, sys, time, urllib.parse, urllib.request
from datetime import datetime, timezone

API = "https://api.twitch.tv/helix/"
HERE = os.path.dirname(os.path.abspath(__file__))


def headers():
    cid = os.environ.get("TWITCH_CLIENT_ID")
    if not cid:
        sys.exit("TWITCH_CLIENT_ID ortam değişkeni yok.")
    h = {"Client-Id": cid, "Accept": "application/json"}
    tok = os.environ.get("TWITCH_TOKEN")
    # Bulutta vekil gerçek anahtarı ekler; yerel bilgisayarda TWITCH_TOKEN kullanılır.
    h["Authorization"] = "Bearer " + (tok or "vekil-tarafindan-eklenir")
    return h


def get(path, params):
    url = API + path + "?" + urllib.parse.urlencode(params, doseq=True)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers()), timeout=30) as r:
                left = r.headers.get("Ratelimit-Remaining")
                if left is not None and int(left) < 5:
                    time.sleep(max(0, int(r.headers.get("Ratelimit-Reset", time.time())) - time.time()) + 1)
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(5 * (attempt + 1))
                continue
            if e.code in (401, 403):
                sys.exit(f"Twitch {e.code}: anahtar eksik ya da süresi dolmuş. Yeni uygulama erişim anahtarı üretin.")
            raise
    raise RuntimeError("Twitch yanıt vermedi: " + url)


def game_id(name):
    data = get("games", {"name": name}).get("data", [])
    if not data:
        sys.exit(f"'{name}' kategorisi bulunamadı. Tam adı Twitch'teki gibi yazın.")
    return data[0]["id"]


def live_streams(gid):
    out, cursor = [], None
    while True:
        p = {"game_id": gid, "first": 100, "type": "live"}
        if cursor:
            p["after"] = cursor
        res = get("streams", p)
        out += res.get("data", [])
        cursor = res.get("pagination", {}).get("cursor")
        if not cursor or not res.get("data"):
            return out


def users(ids):
    info = {}
    for i in range(0, len(ids), 100):
        for u in get("users", {"id": ids[i:i + 100]}).get("data", []):
            info[u["id"]] = u
    return info


def followers(uid):
    try:
        return get("channels/followers", {"broadcaster_id": uid, "first": 1}).get("total", "")
    except Exception:
        return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--oyun", default="Grand Theft Auto VI")
    ap.add_argument("--min", type=int, default=50)
    ap.add_argument("--max", type=int, default=500)
    a = ap.parse_args()

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    gid = game_id(a.oyun)
    streams = live_streams(gid)
    mid = [s for s in streams if a.min <= s["viewer_count"] <= a.max]
    print(f"{now} | {a.oyun}: {len(streams)} canlı yayın, {len(mid)} tanesi {a.min}-{a.max} izleyici")

    u = users([s["user_id"] for s in mid])
    rows = []
    for s in mid:
        started = datetime.fromisoformat(s["started_at"].replace("Z", "+00:00"))
        hours = round((datetime.now(timezone.utc) - started).total_seconds() / 3600, 1)
        info = u.get(s["user_id"], {})
        rows.append({
            "tarama": now, "kanal": s["user_login"], "ad": s["user_name"], "dil": s["language"],
            "izleyici": s["viewer_count"], "yayin_saati": hours, "takipci": followers(s["user_id"]),
            "tur": info.get("broadcaster_type", ""), "baslik": s["title"][:140],
            "etiketler": " ".join(s.get("tags") or []), "oyun": a.oyun,
            "link": "https://twitch.tv/" + s["user_login"],
        })

    path = os.path.join(HERE, "tarama.csv")
    new = not os.path.exists(path) or os.path.getsize(path) == 0
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["tarama"])
        if new and rows:
            w.writeheader()
        w.writerows(rows)

    # Özet: tüm taramalardaki her kanal
    with open(path, newline="", encoding="utf-8") as f:
        allrows = list(csv.DictReader(f))
    agg = {}
    for r in allrows:
        k = r["kanal"]
        g = agg.setdefault(k, {"kanal": k, "dil": r["dil"], "gorulme": 0, "izleyici_toplam": 0,
                               "en_uzun_yayin_saati": 0.0, "takipci": r["takipci"], "tur": r["tur"], "link": r["link"]})
        g["gorulme"] += 1
        g["izleyici_toplam"] += int(r["izleyici"])
        g["en_uzun_yayin_saati"] = max(g["en_uzun_yayin_saati"], float(r["yayin_saati"] or 0))
    out = []
    for g in agg.values():
        g["ort_izleyici"] = round(g.pop("izleyici_toplam") / g["gorulme"])
        out.append(g)
    out.sort(key=lambda g: (-g["gorulme"], -g["en_uzun_yayin_saati"], -g["ort_izleyici"]))
    with open(os.path.join(HERE, "ozet.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["kanal", "dil", "gorulme", "ort_izleyici", "en_uzun_yayin_saati", "takipci", "tur", "link"])
        w.writeheader()
        w.writerows(out)
    print(f"tarama.csv'ye {len(rows)} satır eklendi; ozet.csv'de {len(out)} kanal var.")


if __name__ == "__main__":
    main()
