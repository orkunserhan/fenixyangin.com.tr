# Fenix Yangın

Fenix Sistem Yangın Mühendislik kurumsal web sitesi — statik HTML/CSS/JS.
Framework yok, derleme adımı yok: düz HTML + tek CSS dosyası + tek JS dosyası.

## Yapı

```
index.html              Anasayfa
pages/                   İç sayfalar
css/fenix-design.css     Tüm stiller
js/fenix.js              Tüm etkileşim
parts/turkiye-agi.html   Hizmet ağı haritası (iframe)
assets/                  Logo, favicon, görseller
.htaccess / _headers     Sunucu yapılandırması (Apache / Netlify)
```

## Yerel önizleme

`index.html` dosyasını tarayıcıda açın veya klasörde bir statik sunucu çalıştırın:

```
python -m http.server 8000
```

Sonra `http://localhost:8000` adresini açın.
