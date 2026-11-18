#!/usr/bin/env python3
"""Dalga envanteri: şarkı listesini MusicBrainz ile eşleştirir.

Girdi CSV sütunları: istasyon, sanatci, sarki, kaynak, not
Çıktı CSV: girdi + mbid, eslesme_puani, isrc, ilk_yayin, plak_sirketi, sirket_grubu, hedef

Kullanım:
    python3 eslestir.py envanter.csv envanter_eslesmis.csv

MusicBrainz kuralı gereği saniyede en fazla 1 istek atılır. 200 şarkı yaklaşık 10 dakika sürer.
Şirket grubu tahminidir: ilk yayının plak şirketine bakar, bugünkü hak sahibi farklı olabilir.
Her hedef şarkının hak sahibi elle doğrulanmalıdır.
"""
import csv, json, re, sys, time, urllib.parse, urllib.request

API = "https://musicbrainz.org/ws/2/"
UA = "DalgaEnvanter/0.1 (internal research tool)"
_last = [0.0]

# Büyük üç şirket grubu ve bilinen alt şirketleri (tahmini sınıflama için)
MAJOR = {
    "universal": "Universal", "umg": "Universal", "island": "Universal", "republic": "Universal",
    "interscope": "Universal", "geffen": "Universal", "def jam": "Universal", "capitol": "Universal",
    "motown": "Universal", "polydor": "Universal", "virgin": "Universal", "emi": "Universal",
    "mercury": "Universal", "decca": "Universal", "verve": "Universal", "mca": "Universal",
    "a&m": "Universal", "casablanca": "Universal", "blue note": "Universal",
    "sony": "Sony", "columbia": "Sony", "rca": "Sony", "epic": "Sony", "arista": "Sony",
    "legacy": "Sony", "jive": "Sony", "zomba": "Sony", "ruffhouse": "Sony",
    "warner": "Warner", "atlantic": "Warner", "elektra": "Warner", "reprise": "Warner",
    "parlophone": "Warner", "rhino": "Warner", "asylum": "Warner", "sire": "Warner",
    "nonesuch": "Warner", "atco": "Warner", "big beat": "Warner", "wea": "Warner",
    # bugun buyuk uce ait olan eski/tarihi plak sirketleri
    "okeh": "Sony", "cbs": "Sony", "monument": "Sony", "rca victor": "Sony", "bmg": "Sony", "laface": "Sony",
    "chess": "Universal", "checker": "Universal", "cadet": "Universal", "philips": "Universal", "vertigo": "Universal",
    "polygram": "Universal", "london": "Universal", "abc": "Universal", "dot": "Universal", "uni": "Universal",
    "chrysalis": "Warner", "cotillion": "Warner", "warner bros": "Warner", "eastwest": "Warner", "roadrunner": "Warner",
    "def american": "Universal", "geffen": "Universal", "fania": "bagimsiz-buyuk", "concord": "bagimsiz-buyuk",
}


def get(path, **params):
    wait = 1.1 - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    params["fmt"] = "json"
    url = API + path + "?" + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as r:
                _last[0] = time.time()
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            _last[0] = time.time()
            if e.code in (429, 503):
                time.sleep(3 * (attempt + 1))
                continue
            raise
    raise RuntimeError("MusicBrainz yanıt vermedi: " + url)


def esc(s):
    return s.replace('"', '\\"')


def label_group(names):
    for n in names:
        low = n.lower()
        for key, grp in MAJOR.items():
            if re.search(r"(?<![a-z])" + re.escape(key) + r"(?![a-z])", low):
                return grp
    return "bagimsiz" if names else "bilinmiyor"


def main_artist(artist):
    # "A ft. B", "A feat. B", "A & B", "A x B", "A, B" -> arama icin ana sanatci "A"
    return re.split(r"\s+(?:ft\.?|feat\.?|featuring|x|&|and)\s+|,", artist, flags=re.I)[0].strip()


def match(artist, title):
    res = []
    # once tam adla ara (grup adlari "Earth, Wind & Fire" bozulmasin), bulamazsa ana sanatciyla
    for a in dict.fromkeys([artist, main_artist(artist)]):
        q = f'recording:"{esc(title)}" AND artist:"{esc(a)}"'
        res = get("recording", query=q, limit=25).get("recordings", [])
        if res and max(int(r.get("score", 0)) for r in res) >= 90:
            break
    if not res:
        return None
    top = max(int(r.get("score", 0)) for r in res)
    # Orijinal stüdyo kaydını tercih et: konser, demo, remix vb. sürümleri ele, en eski yayını seç
    alt = ("live", "demo", "remix", "edit", "version", "instrumental", "acoustic", "mix", "remaster", "karaoke", "cover")
    def key(r):
        d = (r.get("disambiguation") or "").lower()
        return (int(r.get("score", 0)) < top - 5, any(a in d for a in alt), r.get("first-release-date") or "9999")
    best = min(res, key=key)
    rec = get("recording/" + best["id"], inc="isrcs+releases")
    releases = [r for r in rec.get("releases", []) if r.get("status") in (None, "Official")]
    releases.sort(key=lambda r: r.get("date") or "9999")
    labels = []
    if releases:
        rel = get("release/" + releases[0]["id"], inc="labels")
        labels = [li["label"]["name"] for li in rel.get("label-info", []) if li.get("label")]
    return {
        "mbid": best["id"],
        "eslesme_puani": best.get("score", ""),
        "isrc": " ".join(rec.get("isrcs", [])),
        "ilk_yayin": rec.get("first-release-date", ""),
        "plak_sirketi": "; ".join(dict.fromkeys(labels)),
        "sirket_grubu": label_group(labels),
    }


def main(src, dst):
    with open(src, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    extra = ["mbid", "eslesme_puani", "isrc", "ilk_yayin", "plak_sirketi", "sirket_grubu", "hedef"]
    fields = list(rows[0].keys()) + [c for c in extra if c not in rows[0]] if rows else extra
    for i, row in enumerate(rows, 1):
        try:
            m = match(row["sanatci"].strip(), row["sarki"].strip())
        except Exception as e:  # tek şarkıdaki hata tüm listeyi durdurmasın
            m = None
            row["not"] = (row.get("not", "") + f" | hata: {e}").strip(" |")
        if m:
            row.update(m)
            row["hedef"] = "evet" if m["sirket_grubu"] in ("bagimsiz", "bilinmiyor") else "hayir"
        else:
            row["hedef"] = "elle bak"
        print(f"[{i}/{len(rows)}] {row['sanatci']} - {row['sarki']}: {row.get('sirket_grubu', 'eşleşmedi')}", flush=True)
    with open(dst, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
