# 2. Tur Sunumları (isimsiz)

---
## SUNUM A — Gece Yarısı Ağ Haritası (Türkiye)

**0. Beyin fırtınası:** 1) Lansman gecesi ağ haritası: gönüllü ölçümlerle ISP bazlı gecikme raporu (seçildi) 2) Gece yarısı fiziksel mağaza sıra tutma 3) Evde kesinti için UPS ve yedek internet kiralama 4) Banka/çağrı merkezlerine lansman gecesi vardiya ajansı 5) Ebeveynler için aile oyun planı danışmanlığı 6) Lansman gecesi uyku/yorgunluk verisi, sponsorlu oyuncu sağlığı raporu.
Neden: Ağ haritasının verisi yalnızca bu gece toplanabilir, sonradan geriye dönük üretilemez; zamanla kilitli veri hendektir.

**2. Özet:** Lansman gecesi Türkiye'deki gönüllü oyuncuların rızaya dayalı ağ ölçümlerini toplayıp servis sağlayıcılara ve ağ firmalarına "ilk saat yük raporu" satmak.

**3. Nasıl işler:** Mobilde tek sayfa, "Ölçüme katıl" + KVKK onayı. Tarayıcı 23:30–01:30 arası 30 sn'de bir ping ve küçük indirme ölçümü yapar; yalnız kendi test uç noktasına ve açık ölçüm sunucularına gider, oyun/Rockstar sunucularına istek yok. Kayıt: il, dakika, gecikme, paket kaybı, ISP. IP anında ASN'e çevrilip saklanmaz. Araçlar: ücretsiz sunucu, PostgreSQL, Python, RIPEstat, Plotly. Sabah raporu: hangi sağlayıcıda hangi dakikada gecikme/kesinti.

**4. Gelir:** Ana müşteri 3 ISP + 2 ağ ekipmanı firması; rapor 40.000 TL tek seferlik → 5 müşteriyle 200.000 TL. Medya sponsorluğu ~30.000 TL. Muhafazakar 80.000 TL, iyi 230.000 TL. Katılımcıdan ücret yok; hedef 1.000 katılımcı. Fiyatlar tahmin.

**5. Maliyet/beceri:** Sunucu+alan adı ~1.500 TL/ay; KVKK avukat ~10.000 TL. Temel web, SQL/Python, ağ temelleri, KVKK bilgisi.

**6. İlk 72 saat:** 0–6 saat: sayfa yayında, 50 kişiyle test, 23:30–01:30 ölçüm. 6–24: veri temizleme, ISP bazlı özet. 24–48: 3 ISP ve 2 ağ firmasıyla görüşme. 48–72: erken erişim raporu, sözleşme görüşmeleri. Bu gece veri toplanmazsa hendek oluşmaz.

**7. Riskler:** Açık rıza, IP tutulmaz, 90 gün sonra silme, avukat onayı. "GTA" adı ve Rockstar görseli yok. Ölçüm trafiği küçük, açık uç noktalar. Örneklem yanlılığı raporda açık. Bu gece yetişmezse avantaj kaybolur.

**8. Hendek:** Zaman kilidi (bu gecenin verisi sonradan toplanamaz), katılımcı ağı ve ISP ilişkileri birikir, oyun topluluğu kurucuları ISP'ye B2B satış ve KVKK altyapısı kurmaz.

---
## SUNUM B — Perde: ilerlemeye duyarlı spoiler kalkanı

**0. Beyin fırtınası:** 1) Yayıncı sohbetleri için görev-duyarlı spoiler filtresi (B2B SaaS) — seçildi 2) Markalara sponsor teslim kanıtı raporu (yayında logo/anons süresi denetimi) 3) Ebeveyn/okullara konsol ebeveyn denetimi kurulumu ve seminer 4) TV modeline göre HDR/VRR ayar kartı veren WhatsApp asistanı (affiliate) 5) Yavaş internetli ilçelerde fiber indirme istasyonu ve SSD takma 6) Oyundaki kıyafet/araçların gerçek karşılıkları için "shop the look" affiliate kataloğu 7) Türkiye yayıncı izlenme verisinden markalara haftalık rapor.
Neden: 10.000 okur içerik üretmeye koşacak; yayıncıya altyapı satmayı neredeyse hiçbiri düşünmez. Gereken veri ancak çıkıştan sonra emekle toplanır.

**2. Özet:** Yayıncının hikâyede bulunduğu noktayı bilen ve yalnızca o noktanın ilerisine ait spoiler mesajlarını silen, Twitch/Kick/YouTube resmi API'leriyle çalışan moderasyon uygulaması.

**3. Nasıl işler:** Yayıncı OAuth ile moderatör yetkisi verir. `!görev 14` ile ilerleme bildirilir. Spoiler grafiği her görevden sonra açığa çıkan karakter/olay/mekân adlarını tutar. Katman 1 (ücretsiz): anahtar kelime + yazım varyantları (Türkçe argo dahil). Katman 2: şüpheli mesajlar küçük bir LLM'e "görev 14'ün ötesini açık ediyor mu?" diye sorulur. Silinen mesaj için "geri al" düğmesi; her düzeltme grafiği iyileştirir. Araçlar: Python/Node, Postgres, 10$ VPS, ucuz LLM API.

**4. Gelir:** Ücretsiz plan + "Perde korumasında" rozeti; Pro 15$/ay; ajans lisansı 150$/ay (10 kanal). Varsayım: 30 günde 2.000 yayıncıya ulaşım, %5 ücretliye geçer, 5 ajans → ~2.250$/ay gelir, ~150$ gider. Sonraki hikâye oyunları ve dizi finalleriyle 6. ayda 5.000–8.000$/ay iyimser hedef.

**5. Maliyet/beceri:** ~60$. Orta düzey backend (webhook, OAuth), soğuk satış; oyunu oynamak/yayın izlemek.

**6. İlk 72 saat:** Bu gece: Twitch MVP + tek sayfa site; 30 TR/EN yayıncının moderatörüne ücretsiz kurulum teklifi. 0–24: ilk 15 görevin grafiği, pilotlarda yanlış pozitif düzeltme. 24–48: LLM katmanı, panel, Kick/YouTube. 48–72: ilk vaka yayını, Pro açılır, ajans teklifleri.

**7. Riskler:** Resmi API ve yayıncı yetkisi, hız sınırları; Nightbot sınıfı moderasyon aracı. Oyun görüntüsü/metni satılmaz, grafik olgusal bilgi; sızıntı yok; Rockstar markası üründe yok. "Onaya düşür" modu, eşik ayarı. Mesajlar saklanmaz. Motor oyundan bağımsız.

**8. Hendek:** AutoMod sabit liste kullanır, görev bilmez. Görev–spoiler grafiği ve çok dilli varyant sözlüğü ancak çıkıştan sonra toplanır; her "geri al" veriyi güçlendirir. Moderatör yetkisi vermiş yayıncı hikâye ortasında araç değiştirmez.

---
## SUNUM C — Veli Hattı: Okullar için GTA 6 Lansman Paketi

**0. Beyin fırtınası:** 1) KOBİ'lere lansman haftası izin/devamsızlık politikası kiti 2) Cuma/Pazartesi vardiya planlama şablonu (İK B2B) 3) Hafta sonu PS5 kiralama ve eve teslim 4) Spoiler Kalkanı: sessize alma listeleri ve tarayıcı eklentisi 5) Çiftler için "Oyun Gecesi Anlaşması" baskı şablonu 6) Okul ve velilere pedagog onaylı "Lansman Haftası Veli Paketi" (seçildi) 7) Mahalle kafelerine oyunsuz "lansman gecesi" menü/etkinlik formatı.
Neden: İçerik üreticileri ve klipçiler kurumsal güven ve satış döngüsü isteyen bu işi yapmaz; lansmanın en az karşılanan ihtiyacı ebeveyn ve okulda.

**2. Özet:** Özel okullara ve rehberlik servislerine pedagog onaylı, okul logosuyla gönderilebilen hazır "GTA 6 veli bilgilendirme paketi" lisansı satmak.

**3. Nasıl işler:** Okul psikolojik danışmanı/çocuk gelişimi uzmanıyla gelir paylaşımlı ortaklık. Paket: 2 sayfa veli bülteni, "çocuğumla GTA konuşması" soru kartları, PlayStation/Xbox ebeveyn denetimi adımları, okul duyuru metni. Rockstar görseli yok. Canva ile marka-nötr; okul logo ekler. Satış: kurumsal e-posta ve LinkedIn'de rehber öğretmenler. Ardından aylık "Dijital Oyun Takvimi" bülteni.

**4. Gelir:** Okul lisansı 900 TL; veli bireysel PDF 79 TL; abonelik 300 TL/ay. Varsayım: ~3.000 özel okul e-postası, %2 yanıt → 60 × 900 = 54.000 TL; %20 aboneliğe → 3.600 TL/ay; 300 veli PDF → 23.700 TL. Pedagog payı %30. İlk ay net ~55.000 TL (tahmin).

**5. Maliyet/beceri:** 0–500 TL. Açık Türkçe yazı, temel tasarım, kurumsal e-posta; uzmanlık ortakta.

**6. İlk 72 saat:** 0–12: 5 pedagoga mesaj, taslak bülten. 12–36: uzman onayı, tasarım, ödeme sayfası, kamuya açık okul e-postaları. 36–60: ilk 500 e-posta, 40 rehber öğretmene LinkedIn mesajı. 60–72: güncelleme, ilk 5 okuldan referans, ikinci gönderim.

**7. Riskler:** Yalnız kurumsal/kamuya açık adresler, tek tık çıkış. Tanı/tıbbi iddia yok. Logo/görsel yok, nominatif kullanım. Oyunu karalamayan ton.

**8. Hendek:** Diğerleri oyuncuya satar; okul–veli–pedagog kanalı akla gelmez. Uzman ortaklığı, kurumsal satış ve okul güveni 72 saatte klonlanamaz. İlk okullar referans olur. Takvim aboneliği; Fortnite, EA FC vb. lansmanlara uyarlanır.

---
## SUNUM D — Vardiya Radarı

**0. Beyin fırtınası:** 1) İK/operasyon yöneticilerine devamsızlık hazırlık paketi + "dikkat şoku takvimi" aboneliği (seçildi) 2) Ebeveynlere +18 oyun için "aile anlaşması" seti 3) Site yönetimleri için gece gürültüsü/komşuluk afişi 4) Çocuğun kart harcamalarına itiraz için tüketici hakem heyeti dilekçe üreticisi 5) Uzun seanslar için bilek/boyun fizyoterapi kartı, kliniklere B2B lisans 6) "Oyun dul eşi" hediye ve uzlaşı kiti 7) Restoran/kafelere "gece vardiyası menüsü" 8) Sigorta acentelerine konsol/ekipman poliçe şablonu.
Neden: Kararı veren İK müdürünü hedefleyen, GTA 6'yı tekrarlanan bir "kitlesel dikkat şoku" olarak ele alan kimse yok; B2B fiyat ve tekrarlı gelir.

**2. Özet:** İK ve operasyon yöneticilerine GTA 6 gibi kitlesel dikkat olaylarında (19 Kasım Perşembe) beklenen devamsızlığı hesaplayan ve önlemi hazır veren paket; ardından olay takvimi aboneliği.

**3. Nasıl işler:** Google Sheets "Devamsızlık Hesaplayıcı": çalışan sayısı, 18-34 yaş payı, vardiya yapısı → şeffaf varsayımla +1 ile +3 puan ek devamsızlık. Paket: "Dürüst Gün" politikası (önceden talep edilen yarım gün/vardiya takası), WhatsApp/e-posta duyuru şablonları, yedek vardiya planı, Cuma sabahı ölçüm formu. Bir İK uzmanı gözden geçirir. LinkedIn'de çağrı merkezi, depo/lojistik, e-ticaret, perakende İK'sına kişisel mesaj. Sonra "Dikkat Şoku Takvimi" (maçlar, dizi finalleri, lansmanlar, indirim günleri) aboneliği. İzinli, isimsiz olay sonrası devamsızlık verisiyle sektör kıyas tablosu.

**4. Gelir:** Paket 1.490 TL; abonelik 790 TL/ay. 72 saatte 150 mesaj, %5 → 7-8 satış ≈ 11.000 TL. İlk ay ~16.000 TL; 6. ay 40 abone ≈ 31.600 TL/ay. Atölye 5.000 TL. Tahmindir.

**5. Maliyet/beceri:** ~500 TL. Temel İK bilgisi, Sheets, net yazı. Kod yok.

**6. İlk 72 saat:** 0–12: hesaplayıcı + politika taslağı + ödeme linki. 12–36: 150 kişilik liste, ilk 50 mesaj ("yarın sabah devamsızlık yaşayabilirsiniz"). 36–72: teslimat, Cuma sabahı gerçekleşen devamsızlık formu, kıyas raporu, abonelik teklifi.

**7. Riskler:** Hukuki görüş değildir; avukat/İK danışmanı inceler. Çalışan sosyal medyasını izleme/cezalandırma önerilmez. Logo/görsel yok. Yalnız toplu, isimsiz veri. Devamsızlık çıkmayabilir → "risk azaltma" olarak sunulur.

**8. Hendek:** GTA 6'nın işverene maliyetini hesaplayan yok. Gerçek olay sonrası devamsızlık verisi (her satışla büyüyen kıyas) ve İK güveni bir gecede kopyalanamaz. "Dikkat şoku" ürünü; Euro, dizi finalleri, konsol lansmanlarıyla devam eder.

---
## SUNUM E — Aile Cihaz Kalkanı

**0. Beyin fırtınası:** Clipping/kampanya (yasak), takip defteri/rehber (yasak), mod/hesap satışı (yasak), lansman gecesi ebeveyn cihaz ayarı (seçildi), lansman sonrası ikinci el konsol değerleme ve takas, ev ağı kalibrasyonu (modem/ağ önceliği), GTA adı geçmeden gece yarısı yiyecek/kahve siparişi.
Neden: Oyuna bağlı olmayan, çocuklu aileye hizmet veren ve lansman gecesinde talebi doğan alan. Hendek zayıf, açıkça yazıldı.

**2. Özet:** Lansman gecesi çocuklu Türk ailelerine konsol ve PC'lerde yaş sınırı, harcama limiti ve çocuk hesabı ayarlarını uzaktan ya da evde kuran kişisel kurulum hizmeti.

**3. Nasıl işler:** Form (PS5, Xbox, Windows PC, Switch; çocuk yaşı; hesap sayısı). Platformların resmi ebeveyn denetimleri kurulur: yaş sınırı, satın alma onayı, harcama limiti, mağaza ve çevrimiçi kısıtı. Sonunda kontrol listesi ve ayar ekran görüntüsü. Görüntülü bağlantı ya da yerinde ziyaret; ödeme kurulum sonrası.

**4. Gelir:** Uzaktan 400 TL, yerinde 800 TL; ~30 dk. Lansman haftası günde 5–10 aile → 35–70 kurulum → 14.000–56.000 TL brüt. Sonraki 3 ay aylık 10–20 aile → 4.000–16.000 TL. Yıllık paket 99 TL/ay, 20 aile → 1.980 TL/ay. Talebin kanıtı yok.

**5. Maliyet/beceri:** Sıfır. Platform ebeveyn ayarlarını bilmek, aileyle güven, net Türkçe.

**6. İlk 72 saat:** 0–24: test hesaplarında kurulum, sözleşme/ödeme formu, yerel aile grupları ve veli kanallarında tanıtım (GTA adı geçmeden). 24–48: ilk 5–10 aileye ücretsiz kurulum, geri bildirim. 48–72: kontrol listesini düzelt, ücretli sayfa, ilk ödemeler.

**7. Riskler:** KVKK açık rıza, şifre istenmez, yalnız ekran paylaşımı. Sadece resmi platform özellikleri. "Her şeyi engeller" vaadi yok.

**8. Hendek (yarışmacının kendi beyanı):** "Dürüst olarak ilk ve tek değil." Bilgisayarcılar/teknik akrabalar bunu ücretsiz yapıyor. Hendek: Türkçe doğrulanmış kurulum kayıtları, lansman haftası hızı, aile referansları. Özgünlük düşük olabilir.

---
## SUNUM F — Oyun Radarı: Okullar için Veli Brifingi

**0. Beyin fırtınası:** 1) PS kafe ve oyun salonlarına lansman haftası rezervasyon/fiyatlama danışmanlığı 2) Seyahat acentelerine "gerçek Vice City: Miami ve Florida Keys" tur paketi 3) Restoran/dark kitchen'lara "uzun oyun gecesi" menü kiti 4) İK'ya lansman haftası devamsızlık/verimlilik brifingi 5) İkinci el konsol ve SSD fiyat endeksi, perakendecilere haftalık bülten 6) Özel okul rehberlik servislerine "GTA 6 Veli Brifingi": seminer, okul logolu kit, aylık abonelik (seçildi) 7) Engelli oyunculara erişilebilir kurulum danışmanlığı.
Neden: 10.000 kişi oyunculara satış yapacak; oyuncu olmayan, endişeli ve parası olan tarafa (veli/okul) kimse bakmayacak. Güvenle yürüyen satış kopyalanması zor.

**2. Özet:** Lansmanın velilerde yarattığı soru dalgasını özel okulların rehberlik servislerine uzman onaylı seminer ve kit olarak satmak, sonra her büyük oyun çıkışında yenilenen aboneliğe çevirmek.

**3. Nasıl işler:** İçerik: 18+ ne demek, PS5 Family Management ve Xbox Family Settings adımları, ekran süresi önerileri, "çocuğunla nasıl konuşursun" senaryoları; oyun görüntüsü yok, yalnız metin/ikon/menü ekranı. Lisanslı psikolojik danışman onaylar, seminerleri birlikte verir, %30 pay. Ürünler: 45 dk online veli semineri, okul logolu kit (PDF, slayt, ebeveyn denetimi kartı), aylık "Oyun Radarı" brifingi (rehber öğretmenlere 1 sayfa + kısa video). Araçlar: Canva, Zoom, Google Forms, LinkedIn/e-posta, iyzico/fatura.

**4. Gelir:** Seminer 4.000 TL, kit lisansı 1.500 TL, abonelik 2.000 TL/ay (KDV hariç). İlk ay (temkinli): 15 seminer + 40 kit = 120.000 TL, ortak payı sonrası ~84.000 TL. 12. ay: 80 abone × 2.000 × 12 = 1,92 milyon TL yıllık tekrarlayan gelir + seminerler. Ek kanallar: belediye aile merkezleri, dershaneler, kurumsal İK "çalışan veli" webinarları.

**5. Maliyet/beceri:** 2.000–5.000 TL. B2B satış/sunum, düzgün Türkçe içerik, platform menüleri; pedagojik meşruiyet ortaktan.

**6. İlk 72 saat:** 0–12: kit taslağı, iki konsolda menü ekran görüntüleri, açılış sayfası. 12–24: 3 danışmana teklif, birini bağla, onaya gönder. 24–48: kolej zincirlerinden 200 PDR koordinatörü, LinkedIn/e-posta. 48–72: rehber öğretmenlere ücretsiz 20 dk webinar, ilk seminer tarihleri, ilk kit faturaları.

**7. Riskler:** "GTA 6" yalnız betimleyici, logo/görsel yok, bağlantısızlık ibaresi. Uzman onayı, PEGI/ESRB kaynağı. Ahlaki panik pazarlanmaz. Öğrenci verisi yok. Genel bilgilendirme, terapi değil.

**8. Hendek:** Ters kitle: oyun dünyasını oyuncu olmayanlara tercüme ediyor. Okullar anonim hesaptan almaz; uzman ortaklığı, kurumsal fatura, referans okullar gerekir. İlk giren okulun "dijital oyun danışmanı" olur, her yeni çıkışta yenilenir.
