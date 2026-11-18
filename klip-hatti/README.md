# Klip hattı

Uzun bir videodan dikey (9:16), kelime kelime altyazılı kısa klipler çıkarır. Hepsi yerelde ve ücretsiz araçlarla çalışır:
faster-whisper (yazıya çevirme), OpenCV YuNet (yüz bulma ve kırpma), Ollama veya llama-cpp-python (her pencereyi 1–10 puanlama), FFmpeg (kesme ve altyazı).

**Yalnızca izinli görüntüyle kullanın:** kampanya sahibinin lisansladığı görüntü, açık lisanslı video veya yayıncının yazılı izni.

## Windows kurulumu

PowerShell'i bu klasörde açın:

```powershell
powershell -ExecutionPolicy Bypass -File .\kurulum.ps1
```

Betik Python, FFmpeg ve Ollama'yı winget ile kurar. Ardından konuşma modeli olarak `large-v3`'ü, puanlama modeli olarak Qwen3 30B-A3B'yi (yaklaşık 25 GB) indirir ve `klip.cmd` kısayolunu yazar. Ekran kartı kullanılmaz.

## Kullanım

```powershell
.\klip.cmd video.mp4 cikti 3
```

`cikti` klasörüne `klip1.mp4`, `klip2.mp4`, `klip3.mp4` ve altyazı dosyaları yazılır.

## Ayarlar (ortam değişkenleri)

| Değişken | Varsayılan | Açıklama |
|---|---|---|
| `KLIP_WHISPER` | `small` | Konuşma modeli. Uzun yayınlar için `large-v3-turbo` önerilir: `large-v3`'e yakın kalite, birkaç kat hızlı. `large-v3` işlemcide gerçek zamandan yavaş çalışır. |
| `KLIP_MODEL` | `qwen3clip` | Ollama model adı. |
| `KLIP_THREADS` | çekirdek sayısının yarısı | Yazıya çevirme ve puanlama için iş parçacığı. |
| `KLIP_DUZEN` | `konusma` | `konusma`: konuşmacının yüzüne göre 9:16 kırpar. `oyun`: üstte yüz kamerası, altta oyunun ortası. Yüz kamerası yoksa oyunun ortası tam dikey kırpılır. |
| `KLIP_NUM_GPU` | `0` | Ollama'nın ekran kartına yükleyeceği katman sayısı. 0 = yalnızca işlemci. Zayıf ekran kartlarında (ör. RX 550) Ollama çöktüğü için varsayılan 0. |
| `KLIP_YUZ_ORANI` | `0.8` | Bir pencerenin aday sayılması için yayıncının/konuşmacının göründüğü süre oranı. |

Ollama çalışmıyorsa `klip.py` aynı klasördeki `qwen3-4b.gguf` dosyasını llama-cpp-python ile kullanır.

Yazıya çevirme sonucu videonun yanına `<video>.<model>.transkript.json` olarak kaydedilir. Aynı videoyu farklı ayarlarla tekrar işlerken bu adım atlanır (testte 313 sn yerine 79 sn).

Oyun yayını örneği:

```powershell
$env:KLIP_DUZEN="oyun"; .\klip.cmd yayin.mp4 cikti 5
```

## Bilinen sınırlar

- Yüz kontrolü her saniye yapılır ve yalnızca videonun tipik yüzüne (boyut, oyun düzeninde konum) benzeyen yüzler sayılır. Slayttaki fotoğraf yüzleri böylece elenir. Yine de her klibi yayından önce izleyin.
- Oyun düzeni yüz kamerasının sabit durduğunu varsayar. Gerçek bir yayın kaydıyla henüz denenmedi.
- Pencereler konuşma parçası sınırında başlar, bazen cümlenin ortasından. Gerekirse başlangıcı kaydırın.

## Test sonucu (18 Kasım 2026, 4 çekirdekli bulut makinesi)

CC BY lisanslı 1.170 saniyelik konuşma: yazıya çevirme 227 sn, puanlama 46 sn, kesme ve altyazı 20 sn, toplam 294 sn. 192 aday pencere, 9 tanesi yüzlü, 3 klip (25–30 sn). Klip 3'te slayt kırpma sorunu görüldü.

## Test sonucu (18 Kasım 2026, Threadripper 3960X, 128 GB, yalnızca işlemci)

10 dakikalık aynı konuşma (`test-video/`):
- `large-v3` ile yazıya çevirme yaklaşık 14 dakika sürdü (gerçek zamandan yavaş). Gece yayınları için `large-v3-turbo` kullanın.
- Qwen3 30B-A3B ile puanlama ve 3 klibin kesilmesi: 63 sn. 134 aday, 4'ü yüzlü, 3 klip.
- Ollama, model RX 550'ye yüklenmeye çalışınca çöktü (`0xc0000005`). Çözüm: `KLIP_NUM_GPU=0` (varsayılan).
