# GTA 6 Yol Haritası — Klip Hattı + Müzik Hattı

Kaynak: 1. tur en güçlü kombinasyon (KlipPusula + Sabah Teslim) ve 3. tur kazananı (Leonida Dalgası) + jürinin önerdiği "yayıncılara telifsiz müzik paketi".
Başlangıç: 18 Kasım 2026, ~21:45 (TR). GTA 6 çıkışı: 19 Kasım 00:00.
Not: Tüm gelir rakamları yarışmacıların ve jürinin tahminleridir, doğrulanmamıştır.

**Pazar: uluslararası.** Ürünler İngilizce, fiyatlar dolar cinsinden. Türkiye yalnızca şirketin kurulu olduğu yer.

## Genel yapı: 2 hat, 4 ürün

| Hat | Ürün | Müşteri | Gelir | Rockstar riski |
|---|---|---|---|---|
| Klip | **KlipPusula** — kural denetçisi, kazanç hesaplayıcı, klip defteri | Klipçiler | Pro 5 $/ay | Yok (görüntüye dokunmaz) |
| Klip | **Sabah Teslim** — gece yayınından sabah 09:00'da 5 hazır klip | Uluslararası orta ölçekli yayıncılar (50–500 izleyici, İngilizce öncelikli) | ~150 $/ay | Orta (karar kapısı #1) |
| Müzik | **Dalga Ajansı** (eski adı Leonida Dalgası) — oyun radyosundaki şarkıların hak sahiplerine dinlenme artışı hizmeti | Bağımsız plak şirketi, mirasçı, müzik yayıncısı (yurt dışı) | 1.500 $ peşin kurulum | Düşük (müşterinin kendi kataloğu) |
| Müzik | **Temiz Yayın Müziği** — yayıncılara telif sorunu olmayan özgün müzik paketi | Yayıncılar, klipçiler | Paket / abonelik | Çok düşük (kendi IP'miz) |

### Hatlar arası bağlantılar
1. KlipPusula kullanıcıları ve çevresindeki yayıncılar → Sabah Teslim müşterisi.
2. Sabah Teslim müşterileri ve KlipPusula kullanıcıları → Temiz Yayın Müziği alıcısı (yayında ve klipte telif kısıtlaması yaşamamak için).
3. **Dalga Ajansı müşterisinin şarkısı için müzik tanıtım kampanyası:** hak sahibinin kendi sesiyle (oyun görüntüsü olmadan) klip kampanyası açılır, KlipPusula'da listelenir, klipçi topluluğu üretir. Telif açısından temiz, çünkü sesin sahibi müşterinin kendisi.
4. Ortak veri omurgası: klip kayıt defteri (kayit.csv), kampanya listesi, şarkı–hak sahibi tablosu ve dinlenme artış serisi.

### Öncelik mantığı
- Önce sıfır riskli ve hemen yayına girebilen: KlipPusula.
- Zamanla kilitli olan: oyunun radyo listesi ve şarkıların ilk günlerdeki dinlenme verisi yalnızca şimdi toplanabilir. Dalga envanteri ilk gün başlar.
- Rockstar politikasına bağlı olan (Sabah Teslim'in GTA kısmı) karar kapısından sonra büyür.

---

## Faz 0 — Bu gece (00:00'a kadar)
- [x] KlipPusula ücretsiz çekirdeği yayında: kural metni ayıklayıcı (hashtag, süre, platform, 30 dk teslim) + kazanç ve ödeme takvimi hesaplayıcı. Statik HTML/JS, Cloudflare Pages.
- [ ] Ürün adlarında ve alan adlarında "GTA", "Rockstar", "Leonida", "Vice" geçmez; her sayfada "resmi değildir, bağlantısı yoktur" notu.
- [x] Makaledeki klip hattını CC lisanslı deneme videosuyla bir kez çalıştır. (18 Kasım: 19,5 dk video, 294 sn, 3 klip; klip 3'te slayt kırpma sorunu)
- [ ] Dalga envanter tablosunu aç: şarkı, istasyon, sanatçı, ISRC, kayıt hakkı sahibi, eser hakkı sahibi, iletişim, çıkış öncesi taban, günlük dinlenme.
- [ ] GTA 6 yayını duyuran 40 uluslararası orta ölçekli yayıncının listesi (Twitch, Kick, YouTube).

## Faz 1 — İlk 72 saat (19–21 Kasım)

### Gün 1 (19 Kasım)
- [ ] Oyunu oyna, radyo istasyonlarının şarkı listesini topla (kendi oynanış + topluluk listeleri).
- [ ] **Rockstar'ın güncel içerik/monetizasyon politikasını oku → KARAR KAPISI #1.**
- [ ] KlipPusula'yı klipçi topluluklarında satış yapmadan, yardım olarak paylaş.
- [ ] 30 yayıncıya ücretsiz 3 klip demo teklifi (konusu karar kapısı #1'e göre).

### Gün 2 (20 Kasım)
- [ ] Şarkıları ISRC ve hak sahipleriyle eşleştir (MusicBrainz, Discogs, ASCAP/BMI repertuvarı, ISNI). Büyük şirket hitlerini ele; uzun kuyruğu tut.
- [ ] Taban sorunu: liste çıkınca her şarkının çıkış öncesi geçmişini kamuya açık kaynaklardan geriye dönük çek; bulunamayanlarda ilk günü taban kabul et ve raporda belirt.
- [ ] Sabah Teslim demolarını teslim et (VOD'u yayıncıdan dosya olarak al, yt-dlp ile indirme).
- [ ] KlipPusula Pro ödeme sayfası (5 $/ay; uluslararası ödeme alan bir sağlayıcı, ör. Lemon Squeezy veya Paddle).

### Gün 3 (21 Kasım)
- [ ] En hızlı yükselen 30 uzun kuyruk şarkının hak sahibine ücretsiz tek sayfalık artış raporu (İngilizce).
- [ ] Sabah Teslim: ilk 2 imza hedefi; aylık ön ödeme.
- [ ] Temiz Yayın Müziği için 2–3 bağımsız prodüktörle görüşme (ülke fark etmez).

### KARAR KAPISI #1 (Gün 1): Rockstar politikası para kazandıran oyun klibine izin veriyor mu?
- **İzin veriyor:** Sabah Teslim GTA yayınlarıyla devam eder; her klipte yayıncının yüzü, yorumu ve kurgu katkısı ağırlıklı olur.
- **İzin vermiyor ya da belirsiz:** Sabah Teslim yalnızca yayıncının sohbet, IRL ve podcast yayınlarıyla ve kampanya sahibinin lisansladığı görüntüyle çalışır. KlipPusula, Dalga Ajansı ve Temiz Yayın Müziği bu karardan etkilenmez.

## Faz 2 — Hafta 1–2 (22 Kasım – 2 Aralık)

**Altyapı**
- [ ] Şahıs şirketi ve e-arşiv fatura (B2B faturası için).
- [ ] Yurt dışı tahsilat hesabı (müşterilerin tamamı yurt dışında).
- [ ] Sözleşme şablonları: Sabah Teslim hizmet sözleşmesi, Dalga hizmet sözleşmesi, müzik paketi lisans metni. Bir kez avukata göster.

**Dalga Ajansı**
- [ ] 3 pilot hedefi; gelir peşin kurulum ücreti (jürinin şartı). Başarı payı en fazla isteğe bağlı bonus.
- [ ] Her müşteride ilk iş: Rockstar ile yaptığı sync sözleşmesinde oyunun adını tanıtımda kullanma kısıtı var mı, yazılı teyit.
- [ ] Dinlenme verisi yalnızca platform şartlarına uygun kaynaklardan ya da müşterinin kendi panelinden (ör. sanatçı panelleri) alınır.
- [ ] İlk müşteri için müzik tanıtım kampanyası (bağlantı #3): şarkının kendi sesiyle, oyun görüntüsü olmadan; KlipPusula'da listelenir.

**Sabah Teslim**
- [ ] n8n otomasyonu, sohbet yoğunluğu sinyali, oyun terimleri sözlüğü (İngilizce öncelikli, çok dilli altyazı).
- [ ] Haftalık "ne tuttu" raporu.

**Temiz Yayın Müziği**
- [ ] İlk 10 parça; her parça için prodüktörden yazılı tam hak devri.
- [ ] Yapay zekâ ile üretilen parça kullanılacaksa aracın ticari lisans şartları kontrol edilir.
- [ ] Ad ve kapakta "Vice", "Leonida", GTA çağrışımı yok.

**KlipPusula**
- [ ] 5–10 kampanyayı elle listele, klip defteri ve dışa aktarma.

### KARAR KAPISI #2 (14. gün)
| Ürün | Devam koşulu | Koşul tutmazsa |
|---|---|---|
| KlipPusula | ≥1.000 ziyaretçi ve ≥20 Pro abone | Ücretsiz bırak, yalnızca Sabah Teslim ve müzik paketi için müşteri kazanma aracı olarak kullan |
| Sabah Teslim | ≥2 ücretli müşteri | Fiyatı ya da hedef yayıncı büyüklüğünü değiştir |
| Dalga Ajansı | ≥1 ödenmiş pilot | Hizmeti durdur, yalnızca veri raporu satışına küçült |
| Temiz Yayın Müziği | ≥10 yayıncı ücretsiz sürümü kullanıyor | Paketi KlipPusula Pro'ya dahil et, ayrı satma |

## Faz 3 — Ay 1 (Aralık)
- [ ] Temiz Yayın Müziği satışa açılır; Sabah Teslim müşterilerine dahil edilir.
- [ ] Her hafta kayıt defterinden rapor; çalışmayan kanalı kes.

**Ay 1 hedefleri (tahmin):**
| Kalem | Temkinli | Hedef |
|---|---|---|
| KlipPusula Pro | 30 abone ≈ 150 $ | 100 abone ≈ 500 $ |
| Sabah Teslim | 2 müşteri ≈ 300 $ | 3 müşteri ≈ 450 $ |
| Dalga Ajansı | 0–1 pilot (0–1.500 $) | 3 pilot ≈ 4.500 $ |
| Temiz Yayın Müziği | Ücretsiz sürümle kullanıcı toplama | İlk satışlar |

## Faz 4 — Ay 2–3 (Ocak – Şubat)
- [ ] Sabah Teslim 10 müşteriye; son kontrol için yarı zamanlı editör.
- [x] KlipPusula İngilizce sürümü (yapıldı, 18 Kasım).
- [ ] Dalga: dinlenme artış endeksini müzik süpervizörleri, A&R ve sync ajanslarına abonelik olarak sunmak, yalnızca kullanım şartlarına uygun veriyle.
- [ ] "Temiz Yayın" ek paketi: Sabah Teslim + müzik paketi birlikte.

**Ay 3 hedefi (tahmin):** KlipPusula ~1.500 $/ay (300 abone), Sabah Teslim ~1.500 $/ay (10 müşteri), Dalga 3–8 toplam müşteri.

## Faz 5 — Ay 4–6 (sürdürülebilirlik)
- [ ] GTA 6 çevrimiçi modu ve güncellemelerdeki her yeni radyo şarkısı Dalga'yı yeniden besler.
- [ ] Klip hattı ve müzik paketi oyundan bağımsız: sonraki büyük lansmanlara ve yayın türlerine taşınır.
- [ ] Değerlendirme: 3. turun gözden kaçan fikri — görme engelli oyuncular için Türkçe sesli betimleme / erişilebilirlik karnesi — üçüncü hat olarak açılmalı mı?

---

## Sürekli hukuki kontrol listesi
- [ ] Ürün, alan adı ve playlist adlarında Rockstar markası ve kurgusal adlar yok; yalnızca betimleyici kullanım + bağlantısızlık notu.
- [ ] Oyun görüntüsü yalnızca karar kapısı #1 izin veriyorsa ve yayıncının kendi hesabında monetize edilir; biz monetize etmeyiz.
- [ ] VOD yayıncıdan dosya olarak alınır.
- [ ] Bot, sahte görüntülenme ve sahte dinlenme yok; sözleşmelere yazılır.
- [ ] Soğuk e-posta/mesaj: yalnızca kamuya açık iş iletişimi, tek tık çıkış; GDPR (AB/BK), CAN-SPAM (ABD) ve KVKK yükümlülükleri kontrol edilir.
- [ ] Sync sözleşmesi tanıtım kısıtı her Dalga müşterisinde teyit edilir.
- [ ] Müzik paketinde her parçanın hak devri belgesi saklanır.
- [ ] Vergi ve fatura (şahıs şirketi, e-arşiv, yurt dışı gelir beyanı).

## Riskler ve yedek planlar
| Risk | Etkilenen | Yedek plan |
|---|---|---|
| Rockstar ticari klibe izin vermiyor | Sabah Teslim | GTA dışı yayın içerikleri ve lisanslı kampanya görüntüsü |
| Klipçi trafiği düşük | KlipPusula | Ücretsiz bırak, müşteri kazanma aracına çevir; İngilizce sürüm |
| Hak sahipleri cevap vermiyor ya da ödemiyor | Dalga | Ücretsiz raporla güven kur; olmazsa veri raporu satışına küçült |
| Sync sözleşmesi tanıtımı yasaklıyor | Dalga | Oyun adı geçmeden genel dinlenme artışı hizmeti olarak sun |
| Dinlenme artışı kısa sürüyor | Dalga | Gelir peşin kurulum ücretinde; güncellemelerdeki yeni şarkılarla yeni müşteri |
| Tek kişinin zamanı yetmiyor | Hepsi | Öncelik: KlipPusula → Dalga envanteri → Sabah Teslim → müzik paketi; editör ve prodüktörle iş bölümü |

## Gereken beceriler ve bütçe
- **Beceriler:** temel web (veya bir kod ajanını yönlendirebilmek), komut satırı, Türkçe kurgu sezgisi, İngilizce B2B yazışma, müzik hakları (ISRC, kayıt ve eser hakkı farkı), satış yazışması.
- **Başlangıç bütçesi (tahmin):** 0–20.000 TL — alan adları, tek seferlik avukat incelemesi, şirket kuruluşu, ilk müzik parçalarının prodüktör ücreti.
