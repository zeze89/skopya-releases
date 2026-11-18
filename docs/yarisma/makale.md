# gta 6 ücretsiz clipping hattı kur: indir, kes, dikey yap, altyazı ekle

gta 6 bu gece 00:00'da açılıyor. aynı saatte binlerce yayıncı saatlerce oynayacak ve o yayınların kırk saniyelik anları kısa video olarak tekrar tekrar paylaşılacak. bu işe clipping deniyor.

bu yazıda clipping hattını sıfır liraya kurdum ve baştan sona çalıştırdım. 19 buçuk dakikalık bir videodan 2 dakika 17 saniyede üç dikey, altyazılı klip çıktı. komutlar, süreler ve kodun tamamı aşağıda.

bu yazıda şunlar var:

> clipping nedir, para nereden gelir

> hangi görüntüden klip çıkarabilirsin

> 6 adımlık ücretsiz hat ve çalışan kod

> sahne algılama, whisperx ve n8n ile genişletme

> denemenin süreleri ve çıktısı

> yapay zekana yapıştıracağın ajan tarifi

> hazır açık kaynak araçlar

## clipping nedir

uzun bir videodan (yayın, podcast, konuşma) 15 ila 60 saniyelik tek bir an seçilir. kesilir, dikey yapılır, altyazı eklenir ve kendi hesabından paylaşılır. işin zor kısmı doğru anı bulmak, geri kalanı makinenin işi.

paranın geldiği yollar üç tane:

1. kampanyalar. bir yayıncı ya da marka bütçe koyar, clipper'lar o kişinin görüntüsünden klip çıkarır ve doğrulanmış her 1.000 görüntülenme için ödeme alır. content rewards bunun en büyük örneklerinden biri. platformun kendi yayımladığı veriye göre 16 kasımda 710 canlı kampanyanın ortanca oranı 1.000 görüntülenme başına 1 dolardı, kampanyaların yarısı 1 ile 2 dolar arasındaydı. ortanca klip tavanı 200 dolar, ortanca asgari ödeme eşiği 2 dolar. bu rakamlar platformun kendi sayfasından, kampanya başına değişir; her kampanyanın sayfasında yazanı oku.

2. x'in kendi clip özelliği. 9 kasımdan beri ios ve android uygulamasında en az 2 dakikalık, önceden kaydedilmiş bir videodan 5 ila 60 saniyelik bir bölüm kesip yorumunla paylaşabiliyorsun. klip videonun yüzde 30'unu geçemiyor ve üstünde Clip from etiketi duruyor. hem sen hem asıl video sahibi original content rewards programındaysanız ikiniz de kazanabiliyorsunuz.

3. kendi hesabının programları. tiktok creator rewards için 10 bin takipçi, son 30 günde 100 bin görüntülenme ve en az 1 dakikalık özgün video gerekiyor. youtube'da ise ortaklık programına girmen lazım. yeni başlayanın ilk pratik yolu kampanyalar.

görseldeki 90 dolar bir hesap örneği: 100.000 görüntülenme, ortanca 1 dolar oranı ve yüzde 10 platform payı. ödeme sırası da şöyle: klibi paylaşırsın, linkini 30 dakika içinde kampanyaya gönderirsin, onay gelir, klip onaydan sonra 7 gün daha kazanır, 3 gün bekleme olur ve ödeme yaklaşık 10 gün sonra bakiyene düşer. content rewards bakiyesinden 1 dolardan itibaren çekebilirsin.

pratik üç ipucu:

- bütçesi hala geniş duran kampanyaya gir, kampanya sayfasında kalan bütçe yazıyor.

- klibi yüklemeden önce kampanyanın istediği hashtag, süre ve platformu satır satır kontrol et.

- filigransız çıktı veren araçla çalış, aşağıdaki hat filigran koymuyor.

## hangi görüntüden klip çıkarırsın

hat hazır olunca ilk soru şu: bu görüntü kimin ve kesmeme izin var mı?

üç güvenli kaynak var.

izinli kampanya görüntüsü. content rewards kampanyalarında görüntüyü kampanya sahibi lisanslıyor ve nasıl kullanacağını sayfasında yazıyor. en kolay yol bu.

açık lisanslı videolar. creative commons attribution gibi lisanslar kesmene, değiştirmene ve paylaşmana izin veriyor, yeter ki kaynağı belirt ve değiştirdiğini söyle. ben denemeyi böyle bir videoyla yaptım.

kendi çektiğin görüntüler. kendi yayının, podcast'in ya da videon. hak sende olduğu için kimseye sormadan kesebilirsin.

iki küçük not da var. youtube'un reused content kuralına göre monetize edilecek bir videoda kendi katkın görünmeli: yorum, kurgu ya da hikaye. izin sahibinden izin almış olsan bile bu kural ayrıca geçerli. rockstar da kendi politikasında ticari olmayan fan kullanımına izin veriyor. para kazandıran bir klip bu tanımın dışında kalıyor, o yüzden oyun klibi için kampanya sahibinin verdiği görüntüyü kullan.

## 6 adımlık ücretsiz hat

hattın her adımında ücretsiz ve açık kaynak bir araç var:

1. indir. yt-dlp (unlicense, 208 bin yıldız). yalnız izinli videolarda kullan.

2. yazıya çevir. faster-whisper (mit lisanslı). konuşmayı kelime kelime zamanlarıyla çıkarıyor, gpu istemiyor.

3. anı seç. ollama ile yerelde çalışan bir model (qwen3 4b, apache 2.0). her 25-45 saniyelik pencereye 1 ile 10 arası puan veriyor.

4. kes. ffmpeg.

5. dikey yap. opencv ve yunet yüz bulucu. konuşmacının yüzüne göre 9:16 kırpıyor, yüz yoksa o pencereyi ele alıyor.

6. altyazı yak. ffmpeg ve libass. kelime kelime, büyük harf, ekranın alt kısmında.

kurulum:

son komut ffmpeg'inde altyazı filtresi var mı diye bakıyor. satır çıkarsa tamam.

yerel yapay zeka için ollama kur (ollama.com), sonra modeli indirip kendi adınla kaydet:

deneme videosu: linux.conf.au 2019'da yapılan how to avoid meetings konuşması (maia sauren, cc by lisansı, wikimedia commons):

sonra aşağıdaki dosyayı klip.py adıyla kaydet ve çalıştır:

klip.py:

## denemenin sonucu

videonun uzunluğu 1.170 saniye. ekran kartı yok, ücretli servis yok, işlemci üstünde çalıştı:

- yazıya çevirme: 96,7 saniye

- aday pencere seçimi, yüz kontrolü ve yerel yapay zeka puanı: 32,1 saniye

- üç klibin kesilip altyazının yakılması: 8,4 saniye

- toplam: 137,2 saniye

hat 71 aday pencere buldu. 12 tanesinde konuşmacı kamerada olduğu için yapay zeka bu 12'sine puan verdi, en iyi üçü kesildi. klipler 26 ile 27 saniye sürdü.

üç klibin 15. saniyesinden kareler yukarıda: 720x1280, konuşmacıya göre kırpılmış, altyazı kelime kelime yanıyor. yapay zekanın verdiği başlıklar da konuşmaya uygun geldi: Colonialism and third person pronouns, Knowing when to speak, I'm happiest when things go organic.

bu denemede iki şey çıktı ve ikisi de çözümü olan şeyler.

- klip 1'in başında slayt göründü, kırpma konuşmacıyı kaçırdı. çözüm: yayınlamadan önce her klibi izle, gerekirse başlangıç saniyesini 2-3 saniye kaydır.

- pencereler segment sınırında başlıyor, bazen cümlenin ortasından. çözüm: klibin ilk kelimesine bak, gerekirse başlangıcı bir segment ileri al.

bir de kurulumda iki şey takıldı: faster-whisper dosyayı kendisi açarken hata verdi, o yüzden sesi ffmpeg ile alıp numpy dizisi olarak veriyorum (kodda pcm satırı). ollama'nın kendi indirme sunucusu benim test makinemde kapalıydı, o yüzden modeli gguf olarak indirip modelfile ile kaydettim. senin bilgisayarında ollama pull qwen3:4b çalışacaktır, o zaman koddaki modelin adını qwen3:4b yap. bu kısa yolu ben denemedim.

## yapay zeka ajanına yapıştıracağın tarif

hattı elle çalıştırmak yerine bir yapay zeka ajanına (claude code, codex ya da yerel bir ajan) devredebilirsin. ona şu tarifi ver:

bu tarifin iki işi kritik: ben izlemeden yayın yok kuralı ve kayit.csv. ikincisi hattı zamanla iyileştiriyor, çünkü hangi klibin tuttuğunu rakamla görüyorsun.

## hattı genişletmek: sahne algılama, whisperx ve n8n

kendi hattına eklemek isteyebileceğin üç şey var.

sahne algılama. pyscenedetect (bsd lisanslı) videodaki kesme noktalarını buluyor. aynı deneme videosunda 27,5 saniyede 49 sahne buldu. klibin başlangıcını ve bitişini bu noktalara yaklaştırırsan klip yarım planda başlamaz. ben bunu klip.py'ye bağlamadım, ayrı çalıştırıp sonucu okudum:

whisperx. faster-whisper ile aynı ailede, kelime zamanlarını daha hassas hizalıyor (bsd-2 lisanslı). altyazı kayması görürsen faster-whisper yerine bunu dene. ben faster-whisper kullandım ve altyazı gayet oturdu.

n8n. kendi sunucunda çalıştırabildiğin, kaynağı açık bir otomasyon aracı. indirme, yazıya çevirme, klip.py ve bildirim adımlarını kutu kutu bağlayıp her yeni videoda otomatik çalıştırabilirsin. lisansı fair-code türünde, kendi işin için kullanmak serbest, şartları yine de github sayfasından oku. bunu bu yazıda kurmadım.

## hazır açık kaynak araçlar

kod yazmak istemeyenler için hazır projeler var. hepsinin github sayfasını 18 kasımda kontrol ettim. peakcut'ı ise gerçekten çalıştırdım.

peakcut. mit lisanslı, 856 yıldız, 14 kasımda açılmış. kendi bilgisayarında çalışıyor, tarayıcıdan açılıyor. python 3.10 ve ffmpeg yetiyor. yapay zeka anahtarı eklersen anı içeriğe bakarak seçiyor, anahtar yoksa en yüksek sesli anları seçiyor. ben aynı videoyla anahtarsız çalıştırdım: kurulum sorunsuz geçti, ses modeli ilk seferde 480 mb indirdi ve altı klip çıktı. anahtarsız mod içeriği anlamadığı için başlıkları hep aynı gelir. ollama dahil kendi modelini bağlayabiliyorsun.

autoclip. mit lisanslı, 371 yıldız. tamamen yerel çalışıyor: whisper ve ollama, hiçbir şey makineden çıkmıyor. konuşmacıyı takip eden 9:16 kırpma ve altyazı yakma var. gpu isteğe bağlı, işlemcide de çalışıyor ama yavaş. ben denemedim.

supoclip. agpl-3.0 lisanslı, 3.400 yıldız, dün gece güncellenmiş. docker ile kuruluyor. transkript için assemblyai anahtarı istiyor, tamamen yerel çalıştırmak için de whisper ve ollama rehberi var. ben denemedim.

openshorts. mit lisanslı, 8.900 yıldız. docker ve 8 gb ram istiyor, işlemcide 8 dakikalık videoyu 5 ile 8 dakikada işliyor. altyazı ve kırpma ücretsiz, dublaj gibi bazı özellikler için kendi gemini, elevenlabs ya da fal.ai anahtarını getiriyorsun. ben denemedim.

viralcutter. gpl-3.0 lisanslı, 477 yıldız. whisperx üstünde çalışıyor, anı seçmek için ücretsiz gemini anahtarı ya da yerel gguf model kullanıyor. nvidia ekran kartı öneriliyor. ben denemedim.

reelsaw. agpl-3.0 lisanslı, yeni bir proje. docker compose ile kuruluyor, anahtarsız tamamen yerel çalışmayı destekliyor. ben denemedim.

kendi hattın 62 satırlık tek dosya. hazır araçlar ise arayüz, düzenleme ekranı ve daha fazla özellik veriyor. hangisi sana uyuyorsa onu kullan.

## başlamadan önce son kontrol

1. izinli bir kaynak seç: kampanya, açık lisans ya da kendi görüntün.

2. bütçesi geniş duran bir kampanya bul.

3. hattı bu yazıdaki videoyla bir kere çalıştır.

4. kendi kaynağınla çalıştır, ilk klibi izlemeden paylaşma.

5. kayit.csv'ye yaz, bir hafta sonra neyin tuttuğuna bak.

gta vi açıldığında yayınlar akmaya başlayacak. hat hazırsa ilk kampanyayı bulup ilk klibi çıkarman yarım saat sürer.

