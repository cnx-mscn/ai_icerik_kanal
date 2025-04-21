
# AI İçerik Kanalı

Bu sistem, gündeme göre her gün bilgilendirici içerik üretip Buffer üzerinden sosyal medyada otomatik olarak paylaşım yapar.

## Kullanım

1. `.env` dosyasını `.env.example` dosyasına göre oluşturun ve kendi API anahtarlarınızı girin.
2. Gerekli kütüphaneleri yükleyin:

```
pip install -r requirements.txt
```

3. İçerik üretmek için:

```
python içerik_ureticisi.py
```

4. İçeriği sosyal medyada paylaşmak için:

```
python paylaş.py
```
