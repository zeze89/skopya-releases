# Yarışma Sunumları (isimsiz)

---
## SUNUM A

**1. Fikrin adı**
KlipPusula: clipper'lar için kural denetçisi, ödeme hesaplayıcı ve klip defteri

**2. Özet**
GTA 6 lansmanında kampanya klibi çıkaran binlerce kişi için, klip üretmeyen ama klip işinde para kaybettirecek hataları (yanlış hashtag, süre, geç gönderim) önleyen ucuz bir web aracı satıyorum. Altın hücumunda kazma satmak gibi.

**3. Nasıl işler**
- Kullanıcı kampanya sayfasındaki kural metnini yapıştırır. Araç hashtag, süre, platform ve link teslim süresini (makaledeki 30 dakika kuralı) ayıklar ve yükleme öncesi onay listesine çevirir. Ayıklama tarayıcıda, kural tabanlı ve isteğe bağlı küçük bir yapay zeka çağrısıyla yapılır.
- Ödeme hesaplayıcı: görüntülenme × 1.000 başına oran × (1 − platform payı), klip tavanı ve asgari eşik dahil. Takvim de gösterir: onay, +7 gün kazanç, 3 gün bekleme, yaklaşık 10 gün sonra bakiye.
- Klip defteri (makaledeki kayit.csv fikrinin arayüzü): klip, kampanya, görüntülenme ve kazanç girilir. Hangi kampanyanın saatlik olarak daha kârlı olduğunu gösterir.
- Kampanya listesini ben elle derlerim, kullanıcı da ekleyebilir. Platformlardan veri çekmem.
- Araçlar: statik HTML/JS, Cloudflare Pages (ücretsiz), Shopier ya da Lemon Squeezy ile ödeme, Claude Code ile hızlı geliştirme.

**4. Gelir modeli ve rakamlar**
Ücretsiz hesaplayıcı trafik çeker. Pro sürüm (kural denetçisi, defter, dışa aktarma) 149 TL tek seferlik. Varsayımlar, açıkça tahmin:
- İlk 2 hafta 6.000 ziyaretçi (Türkçe X, Reddit, Discord, YouTube yorumları).
- %2,5 dönüşüm: 150 satış × 149 TL ≈ 22.000 TL.
- Karamsar senaryo %1 dönüşüm: yaklaşık 9.000 TL. İyimser %4: yaklaşık 36.000 TL.
Bu rakamlar garanti değil, hepsi trafik varsayımına bağlı. Ödeme komisyonu yaklaşık %5-10 düşer.

**5. Başlangıç maliyeti ve beceri**
Zorunlu maliyet 0 TL; özel alan adı istenirse yılda yaklaşık 400 TL. Temel HTML/JS ya da bir kod ajanını yönlendirebilmek yeterli.

**6. İlk 72 saat**
- 0-8. saat: hesaplayıcı ve onay listesi (ücretsiz çekirdek) yayına girer; Pro ödeme sayfası bağlanır.
- 8-24. saat: içerik yayınlanır, ör. "GTA 6 klip kampanyasında ilk gün kazanç hesabı". Clipper topluluklarında ücretsiz hesaplayıcı paylaşılır, satış yapılmaz, yardım edilir.
- 24-48. saat: ilk kullanıcılardan geri bildirim; kural ayıklayıcı hataları düzeltilir; 5-10 kampanya elle listelenir.
- 48-72. saat: Pro'ya klip defteri ve dışa aktarma eklenir; ilk 50 alıcıya lansman fiyatı; geri ödeme garantisi duyurulur.

**7. Riskler ve yönetimi**
- Rockstar/Take-Two: ürün oyun görüntüsü içermez, logo ve görsel kullanmaz. "GTA" adı ürün adında geçmez, yalnızca betimleyici metinde geçer. "Resmi değil, bağlantısı yok" notu konur.
- Platform kuralları: Content Rewards'tan otomatik veri çekmem; veri kullanıcı girişi ve elle derlemeden gelir.
- Yanıltma riski: kazanç vaadi yapmam.
- Veri gizliliği: defter verisi tarayıcıda kalır.
- Yanlış ayıklama: "son kontrolü kendin yap" uyarısı; yanlış kural çıkarırsa iade.

**8. Neden rakiplerinden farklı**
Diğerleri klip üretmeye odaklanır; bu pazar kalabalık ve ücretsiz araçlarla rekabet etmek zor. KlipPusula klip yapanın para kazanma tarafına odaklanır. Telifli içerikle hiç temas etmez. Sıfır maliyetle bu gece çıkabilir. Hype bittikten sonra da her klip kampanyasına uyarlanır; yeni kampanya şablonları abonelik gelirine dönüşebilir.

---
## SUNUM B

**1. Fikrin adı**
"Klip Masası": Türk yayıncılar için GTA 6 lansmanına özel, kendi kliplerini ve klip kampanyalarını yöneten ajans

**2. Tek cümlelik özet**
Herkes klip kesmeye koşarken ben işin talep tarafına geçiyorum: 5 bin ile 100 bin takipçili Türk yayıncılara aylık ücretle kendi yayınlarının klip operasyonunu ve Content Rewards kampanyasını kurup yönetiyorum.

**3. Nasıl işler**
1. Lansmandan önce GTA 6 yayını açacağını duyuran 40 orta ölçekli Türk yayıncıyı listelerim (Kick, Twitch, YouTube). DM ve e-postayla hazır bir teklif sunarım.
2. Yayıncıyla kısa bir hizmet sözleşmesi imzalarım. Görüntü onun, kullanım izni yazılı. Rockstar politikasına uyma sorumluluğu sözleşmede açıkça yazar.
3. Makaledeki ücretsiz hattı çalıştırırım (yt-dlp, faster-whisper, Ollama, ffmpeg ya da PeakCut). Her yayından günde 8-12 dikey, Türkçe altyazılı klip çıkar. Klipler yayıncının kendi hesaplarına onun onayıyla gider.
4. Bütçesi olan yayıncı için Content Rewards'ta kampanya açarım: brief, hashtag, kurallar. Klip gönderenleri denetler, sahte görüntülenmeleri ayıklarım.
5. Her hafta kayit.csv'den rapor: hangi an tuttu, takipçi artışı, bin görüntülenmenin maliyeti.

**4. Gelir modeli ve gerçekçi rakamlar**
- Paket A (yalnız klip): aylık 6.000 TL
- Paket B (klip ve kampanya yönetimi): aylık 10.000 TL ve kampanya bütçesinin %15'i
Varsayımlar: 40 temastan %10'u döner, ilk ay 3 müşteri (2 A, 1 B). B müşterisinin kampanya bütçesi 500 dolar.
- 1. ay: ≈ 25.000 TL
- 3. ay (6 müşteri, 2'si B): yaklaşık 50.000 TL/ay
Tek kişinin kapasitesi 6-8 müşteri; üstü için yarı zamanlı editör.

**5. Başlangıç maliyeti ve gereken beceri**
Ücretsiz hat ve mevcut bilgisayar yeter. Tek sayfalık PDF teklif ve şablon sözleşme. İsteğe bağlı 300 TL alan adı. Beceri: temel komut satırı, an seçme gözü, satış yazışması, raporlama.

**6. İlk 72 saat planı**
- 0–12. saat: Hattı test, 40 yayıncıya DM, 3'üne ücretsiz demo (lansman yayınından 3 klip).
- 12–36. saat: Demoları teslim, "ilk hafta %50 indirim" teklifi. Hedef 2 imza.
- 36–72. saat: Günde 10 klip, ilk B müşterisinin kampanyası, ilk rapor ve vaka metni.

**7. Riskler ve yönetimi**
- Telif ve Rockstar: Hiçbir klibi kendi hesabımda monetize etmem. Sözleşmede: sızıntı yok, mod yok, başlıkta spoiler yok. Her klipte yorum, kurgu ve altyazıyla dönüştürücü katkı.
- Platform: Bot, sahte görüntülenme, hesap paylaşımı yok. Kendi müşterimin kampanyasından klip kesmem (çıkar çatışması yok).
- Ödeme: Paket ücreti peşin. Kampanya bütçesini yayıncı kendisi yatırır.

**8. Neden rakiplerinden farklı**
Diğerleri aynı kampanyalarda 1$/1.000 için yarışacak; ben talep tarafındayım. Gelir sabit aylık ücret. Türkçe pazar niş: global araçlarda Türkçe altyazı ve mizah ayarı yok. Hype bitince yayıncı başka oyuna geçer, hizmet sürer.

---
## SUNUM C

**1. Fikrin adı**
GTA 6 Türkçe Topluluk Üyeliği: Rehber, Canlı Oturum, Sürekli Güncelleme

**2. Tek cümlelik özet**
Ücretsiz Türkçe Discord topluluğunu, oyunun ömrü boyunca süren rehber ve canlı soru-cevap üyeliğine dönüştürüp aylık abonelikle gelir elde ederiz.

**3. Nasıl işler**
- Ücretsiz katman: Discord'da Türkçe ipuçları, soru kanalları, haftalık tartışmalar.
- Üyelik katmanı (aylık): Türkçe yazılı rehber arşivi, görev sıraları, ekonomi ve karakter analizleri, haftalık canlı soru-cevap ve kayıtları.
- Araçlar: Discord, Google Dokümanlar, OBS Studio, Patreon ya da Türkiye'den ödeme alan bir üyelik aracı, Google Forms.
- Rehberler metin ağırlıklı. Görüntü kullanımı kısa ve açıklama amaçlı. Ücretli içerik ticari klip değildir.

**4. Gelir modeli ve gerçekçi rakamlar**
Varsayımlar: Discord'da 15.000 üye (ilk 3 ayda hedef, sıfırdan). Abonelik 99 TL/ay. Kesinti %15. Churn %10.
- Orta senaryo: %1,5 dönüşüm, ~225 üye, net ~18.900 TL/ay.
- Kötü senaryo: %0,7 dönüşüm, ~105 üye, net ~8.800 TL/ay.
- Üçüncü ayda yalnızca 50 üye varsa model zararda; fiyat yeniden değerlendirilir.

**5. Başlangıç maliyeti ve gereken beceri**
Araç maliyeti ~0 TL. Haftada 15-20 saat. Beceri: oyun bilgisi, Türkçe yazım, canlı yayın, moderasyon, ödeme/fatura kurulumu.

**6. İlk 72 saat planı**
- 0-24 saat: Discord, ücretsiz kanallar ve üyelik sayfası açılıştan önce hazır. İlk 10 rehber başlığı.
- 24-48 saat: ilk canlı soru-cevap, üyelere özel ilk üç rehber, anket.
- 48-72 saat: ilk hafta raporu, iki fiyat testi, haftalık rehber takvimi.

**7. Riskler ve yönetimi**
- Rockstar: fan kullanımı ticari değil; ücretli içerikte görüntü minimumda, politika yayın öncesi kontrol edilir.
- Leak, korsan, izinsiz video yok. Hile, hesap satışı, mod yok; moderasyonla uygulanır.
- Vergi/fatura yükümlülükleri kontrol, üye verisi KVKK kapsamında.
- Üye listesi Discord dışında da tutulur.

**8. Neden rakiplerinden farklı**
Klip pazarı kalabalık ve ucuz. Biz Türkçe topluluğu ve güvenilir bilgiyi satıyoruz. Hype sonrasında güncellemeler ve canlı oturumlar üyeliği canlı tutar. Hedef izlenme değil, aylık sadakat.

---
## SUNUM D

**1. Fikrin adı**
Sabah Teslim: Türk GTA 6 yayıncıları için izinli klip operasyonu (B2B abonelik)

**2. Tek cümlelik özet**
Görüntülenme başına 1 dolar kovalamak yerine, makaledeki ücretsiz hattı yayıncıya hizmet olarak satarım: gece yayın yapar, sabah 09:00'da onayına hazır 5 dikey, Türkçe altyazılı klip bulur ve kendi hesabından paylaşır.

**3. Nasıl işler**
- Yayıncı yazılı yetki ve VOD erişimi verir; klipleri ben yayımlamam, o yayımlar.
- n8n, yayın bitince hattı tetikler: yt-dlp (izinli VOD), faster-whisper, yerel qwen3 puanlaması, ffmpeg, yüz kamerasına göre 9:16 kırpma, libass altyazı.
- Ek sinyal: sohbet yoğunluğu — yayıncının sohbet kaydında mesaj hızının sıçradığı anlar aday pencere olur. Oyun yayınında "an" konuşmadan çok tepkidedir.
- Türkçe argo ve oyun terimleri sözlüğü altyazı hatalarını düzeltir.
- Her klibi izlerim, başlangıcı kaydırırım, 10 adaydan 5'ini teslim ederim.
- kayit.csv müşteri bazında tutulur, haftalık "ne tuttu" raporu.

**4. Gelir modeli ve gerçekçi rakamlar**
Varsayımlar: 50–500 anlık izleyicili Türk yayıncı; paket ayda 4.000 TL (20 yayın günü, günde 5 klip); müşteri başına günde ~20 dk insan kontrolü; denemeden ücretliye dönüşüm %10–15.
- 1. ay: 40 teklif, 4–5 müşteri, 16.000–20.000 TL.
- 3. ay: 12–15 müşteri, 48.000–60.000 TL (tek kişinin tavanı, günde 4–5 saat kontrol).
- Ek: kampanya kurulum ücreti 2.500 TL.
- Kıyas: makaledeki örnekte 100.000 görüntülenme 90$ ve garantisiz; burada gelir teslimata bağlı.

**5. Başlangıç maliyeti ve gereken beceri**
0 TL: mevcut dizüstü yeter (makalenin denemesi ekran kartsız 137 sn), tüm araçlar açık kaynak. Beceri: temel komut satırı, yapay zeka ajanına tarif verebilmek, Türkçe kurgu sezgisi, soğuk mesaj.

**6. İlk 72 saat planı**
- Bu gece 20:00–00:00: hattı CC videoyla test; 40 Türk yayıncıya "ilk gece yayınından 3 klip ücretsiz, sabah 09:00'da elinde" teklifi.
- 00:00–09:00: kabul eden ilk 5 yayıncının VOD'unu işle, kontrol et, teslim et.
- 2. gün: görüntülenme ekran görüntüleriyle ücretli pakete çevir.
- 3. gün: n8n otomasyonu, sohbet sinyali, ilk mini rapor.

**7. Riskler ve yönetimi**
- Telif: görüntüyü ben monetize etmem; yayıncının yazılı yetkisiyle kurgu emeği satarım.
- Rockstar: para kazandıran klip fan kullanımı tanımının dışında kalabilir; güncel politika lansman günü okunur, müşteriye yazılı bildirilir. Her klipte yayıncının yüzü ve yorumu bulunur; gerekirse yalnız kampanya sahibinin lisansladığı görüntüyle çalışılır.
- Reused content: yorum ve kurgu katkısı her klipte görünür.
- Bot/sahte izlenme yok, hesap şifresi alınmaz, spoiler etiketi.
- Müşteri kaybı: aylık ön ödeme, sözleşmede teslimat tanımı.

**8. Neden rakiplerinden farklı**
Rekabetin olmadığı tarafa, hattı kuramayan yayıncıya geçiyorum. Gelir sabit ve tekrarlayan, hak sorunu kaynağında çözülü. Hat oyundan bağımsız; hype bitince aynı müşteriyle devam. Sohbet yoğunluğu sinyali ve Türkçe sözlük hazır araçların yapmadığı iki şey.

---
## SUNUM E

**1. Fikrin adı**
Kitlen Hazır: Türkçe GTA 6 Takip Defteri + Kendi Yüzünle Rehber Kanalı

**2. Özet**
Oyun görüntüsü kullanmadan, kendi anlattığın kısa videolarla küçük bir Türkçe kitle toplarsın. Bu kitleye kendi yaptığın dijital GTA 6 tamamlama defterini (Google Sheets, Notion, yazdırılabilir PDF) satarsın.

**3. Nasıl işler**
1. Görevler, koleksiyonlar, yan aktiviteler ve kilometre taşları için sekmeli takip defteri (Sheets, Notion, Canva). Rockstar grafiği yok; kendi çizimler ve düz tipografi.
2. Defteri oynarken doldurup güncellersin: v1.1, v1.2... Güncelleme vaadi alıcıyı geri getirir.
3. Telefonla çekilen 30-45 sn konuşmalar (yüz/ses + kendi grafiklerin). "İlk 24 saatte yaptığım 5 hata" gibi. Oyun görüntüsü yok.
4. Shorts, TikTok, Reels'te yayın; profil linkinden e-posta listesi (ücretsiz mini sürüm) ve ücretli tam sürüm.
5. Gumroad veya Shopier; e-posta için MailerLite ücretsiz katmanı.

**4. Gelir modeli ve rakamlar**
Varsayımlar: tam sürüm 5$, kesinti %10-15. İlk ay 20 video, toplam 100 bin görüntülenme; %1 tıklama, tıklayanların %4'ü alır.
- Temkinli: 40 satış, ~175$ net.
- İyimser: 500 bin görüntülenme, 200 satış, ~850$.
Asıl kazanç kitle ve e-posta listesi.

**5. Başlangıç maliyeti ve beceri**
0-10$. Elektronik tablo düzeni, telefonla çekim, basit kurgu (CapCut). Kod gerekmez.

**6. İlk 72 saat**
- 0-6 saat: defter iskeleti; "ilk izlenimler" videosu.
- 6-24: v1 yayında (mini + tam sürüm), 3 kısa video.
- 24-48: v1.1, soruları video konusu yap, Türkçe topluluklarda kurallara uyarak faydalı paylaşım.
- 48-72: ilk satış analizi, tutan formatı çoğalt, ilk bülten.

**7. Riskler ve yönetimi**
- Rockstar görüntüsü/logosu yok; "resmi değildir" ibaresi; marka adı sadece betimleyici.
- Sızıntı yok, spoiler uyarısı.
- Bot/satın alınmış görüntülenme yok; vergi kontrolü.
- 7 günlük iade.

**8. Neden rakiplerinden farklı**
Görüntü kullanmadığı için telif/ToS riski neredeyse sıfır. Gelir kampanya bütçesine bağlı değil. Hype sonrası DLC, online mod ve sonraki oyunlar için yeni defterler. Bu gece başlanabilir.

---
## SUNUM F

**1. Fikrin adı**
Lansman Kampanya Kurulum Ortağı: yayıncılar ve markalar için izinli klip kampanyası kurma ve yönetme hizmeti

**2. Tek cümlelik özet**
GTA 6 lansmanında yayın yapacak yayıncılar ve küçük markalar için izinli klip kampanyalarını kuruyor, klipçileri seçiyor ve ödemeleri takip ediyoruz. Klip kesmiyoruz; kampanya tarafında çalışıyoruz.

**3. Nasıl işler**
1. Kampanya sahibinin bütçesini ve hedefini alırız. Bütçeyi sahip platforma kendisi yatırır.
2. Kampanya sayfası: izinli görüntü hakları, hashtag, süre, platform, klip tavanı, bütçe. Platform kuralları satır satır kontrol.
3. Türkçe TikTok/Shorts'ta özgün klip üreten klipçileri davet; hesap başına sınır; bot ve sahte görüntüleme yasağı kampanya metninde.
4. Her klibi yayından önce izleriz (başlangıç saniyesi, ilk kelime kontrolü).
5. Görüntülenme, onay, ödeme durumu ücretsiz bir tabloda takip edilir.
Araçlar: Google Sheets, ücretsiz form, makaledeki açık kaynak hat.

**4. Gelir modeli ve rakamlar**
Varsayımlar: kampanya başına 50$ kurulum + bütçenin %10'u yönetim ücreti.
- 1.000$'lık kampanyada gelir 150$.
- Gerçekçi ilk ay: 2 kampanya, ~300$. İyi ay: 5 kampanya, ~750$. Hiç kampanya kapanmayan ay da mümkün.
- İlk 72 saatte imza olasılığı %20-30 (varsayım).
- Bütçeyi biz tutmayız.

**5. Başlangıç maliyeti ve gereken beceri**
0$. Türkçe yazışma, temel kurgu, kampanya kurallarını anlatabilmek, müzakere. Günde 3-4 saat.

**6. İlk 72 saat planı**
- 0-6: tek sayfalık teklif sayfası, kontrol listesi, 3 örnek klip.
- 6-24: 30 yayıncı ve 10 küçük markaya kişisel mesaj; "bütçesi açık kampanyayı 24 saatte kurarız".
- 24-48: görüşme, yazılı teklif, depozito şartı.
- 48-72: ilk kampanya, 15 klipçi davetiyesi, ilk klip onayları.

**7. Riskler ve yönetimi**
- Rockstar: Oyun görüntüsü içeren ödemeli kampanyayı politika yazılı olarak doğrulanmadan kurmayız. İlk işler yayıncının kendi anlatımlı içeriği ya da izinli marka görüntüsüyle.
- Sahte görüntüleme şüphesinde ödeme durdurulur.
- Depozito gelmeden kampanya açılmaz.
- Her kampanya öncesi güncel koşullar kontrol; her klipte kaynak/izin belgesi saklanır.

**8. Neden rakiplerinden farklı**
Çoğu yarışmacı klipçi tarafında yarışacak; biz kampanya sahibi tarafında güven ve doğrulama satıyoruz. Bu bilgi hype sonrası da her oyun ve marka kampanyasında kullanılabilir.
