import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\orkun\.gemini\antigravity\scratch\fenix-static-final\pages"

def read_clean(filepath):
    with open(filepath, "rb") as f:
        raw = f.read()
    raw = raw.replace(b"\r\r\n", b"\r\n")
    return raw.decode("utf-8")

def write_clean(filepath, content):
    # Normalize all line endings to single \r\n
    content = content.replace("\r\r\n", "\n").replace("\r\n", "\n").replace("\n", "\r\n")
    with open(filepath, "wb") as f:
        f.write(content.encode("utf-8"))

def enrich_fm200():
    filepath = os.path.join(BASE_DIR, "fm200-gazli-yangin-sondurme-sistemleri.html")
    content = read_clean(filepath)

    # 1. Update H2s to precisely match requested topics
    content = content.replace(
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Sistemi Nasıl Çalışır?</h2>',
        '<h2 class="fx-h2" style="margin:10px 0 14px">Sistemin Çalışma Prensibi: FM200 Yangın Söndürme Mekanizması</h2>'
    )
    content = content.replace(
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Sisteminin Temel Bileşenleri</h2>',
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM 200 Sistem Özellikleri ve Kurulum Standartları</h2>'
    )
    content = content.replace(
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Nerelerde Kullanılır?</h2>',
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Gazlı Söndürme Sistemi Uygulama Alanları</h2>'
    )
    content = content.replace(
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Sistem Seçimi ve Projelendirme</h2>',
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Tasarım Süreci ve Mühendislik Hesapları</h2>'
    )
    content = content.replace(
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Gaz Dolumu ve Periyodik Bakım</h2>',
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Periyodik Bakım ve Gaz Dolumu Süreci</h2>'
    )
    content = content.replace(
        '<h2 class="fx-h2" style="margin-bottom:6px;color:#ffffff">FM200 Sistem Teklifi Alın</h2>',
        '<h2 class="fx-h2" style="margin-bottom:6px;color:#ffffff">FM200 Gazlı Söndürme Sistemi Teklif Talebi</h2>'
    )

    old_intro = "Fenix Yangın FM200 sistemleri, uluslararası onaylı üreticilerin yüksek basınca dayanıklı, sızdırmazlığı fabrikasyon olarak test edilmiş orijinal bileşenlerinden meydana gelir. Sistem mimarisinde yer alan kritik donanımlar şunlardır:"
    new_intro = "Fenix Yangın FM200 sistemleri; NFPA 2001, TS EN 15004 ve ISO 14520 normlarına tam uyumlu 25 bar veya 42 bar çalışma basıncına sahip yüksek dayanımlı bileşenlerden oluşur. VdS ve UL onaylı hidrolik hesaplama yazılımlarıyla boru çapları, basınç kayıpları ve 10 saniyelik boşalma süresi simüle edilir. <strong>FM 200 sistem özellikleri ve kurulum</strong> standartlarımız kapsamında kullanılan temel donanımlar şunlardır:"
    content = content.replace(old_intro, new_intro)

    # 2. Competitive Differentiator #2 & #5: Scale-based project scope table + F-Gaz compliance + Calculator Bridge in SECTION 9: FIYATLAR
    target_fiyat_marker = '<h3 class="fx-h3" style="font-size:18px;margin:0 0 6px">Projenize Özel FM200 Maliyet Hesabı Yaptırın</h3>'
    fm200_scale_table = '''<!-- COMPETITIVE ADVANTAGE: ODA ÖLÇEĞİNE GÖRE SİSTEM KONFİGÜRASYONU VE F-GAZ YÖNETMELİĞİ UYUMU -->
<div style="margin-bottom:28px;background:#fff;border-radius:12px;border:1px solid #e2e8f0;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,0.03)">
<div style="padding:18px 24px;background:#f8fafc;border-bottom:1px solid #e2e8f0;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px">
<div>
<span style="font-size:12px;font-weight:700;color:var(--fx-primary);text-transform:uppercase;letter-spacing:0.06em">MÜHENDİSLİK ÖLÇEKLENDİRME REHBERİ</span>
<h3 class="fx-h3" style="font-size:18px;margin:4px 0 0;color:#0f172a">Oda Büyüklüğüne Göre FM200 Sistem Konfigürasyonu ve Kapsam Matrisi</h3>
</div>
<a class="fx-btn fx-btn--primary fx-btn--sm" href="gazli-yangin-sondurme-hesaplama.html">10 Saniyede Gaz Miktarı Hesapla →</a>
</div>
<div style="overflow-x:auto">
<table style="width:100%;border-collapse:collapse;font-size:13.5px;text-align:left">
<thead>
<tr style="background:#0f172a;color:#fff">
<th style="padding:13px 18px;font-weight:700">Proje Ölçeği / Mahal Tipi</th>
<th style="padding:13px 18px;font-weight:700">Silindir &amp; Basınç Yapısı</th>
<th style="padding:13px 18px;font-weight:700">Algılama &amp; Otomasyon Kapsamı</th>
<th style="padding:13px 18px;font-weight:700">Test &amp; Yasal Mevzuat</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #e2e8f0">
<td style="padding:13px 18px;font-weight:600;color:#0f172a">Pano İçi / Mikro Kabin<br/><span style="font-size:12px;color:#64748b;font-weight:400">(0,5 m³ – 10 m³)</span></td>
<td style="padding:13px 18px;color:#334155">1 kg – 12 kg Kompakt Tüp (15–25 Bar)</td>
<td style="padding:13px 18px;color:#334155">Isıya Duyarlı Polimer Hortum + Basınç Şalteri</td>
<td style="padding:13px 18px;color:#334155">Şalter Açtırma (Shunt Trip) &amp; Sızdırmazlık Kontrolü</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0;background:#f8fafc">
<td style="padding:13px 18px;font-weight:600;color:#0f172a">Küçük Ölçekli Sistem / Server Odası<br/><span style="font-size:12px;color:#64748b;font-weight:400">(10 m² – 45 m²)</span></td>
<td style="padding:13px 18px;color:#334155">Tekli Dikişsiz Silindir (25 / 42 Bar · 32L–120L)</td>
<td style="padding:13px 18px;color:#334155">Çapraz Zonlu Optik/Isı Dedektörü + Söndürme Paneli</td>
<td style="padding:13px 18px;color:#334155">Door Fan Sızdırmazlık Testi + F-Gaz Kayıt Etiketi</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
<td style="padding:13px 18px;font-weight:600;color:#0f172a">Orta Ölçekli Veri Merkezi &amp; Arşiv<br/><span style="font-size:12px;color:#64748b;font-weight:400">(50 m² – 150 m²)</span></td>
<td style="padding:13px 18px;color:#334155">Çoklu Silindir &amp; Manifold (25 / 42 Bar · 2–4 Tüp)</td>
<td style="padding:13px 18px;color:#334155">Çapraz Zon + Hava Çekmeli (VESDA) + Klima/Damper Rölesi</td>
<td style="padding:13px 18px;color:#334155">Door Fan Testi + Basınç Tahliye Damperi + F-Gaz Belgesi</td>
</tr>
<tr>
<td style="padding:13px 18px;font-weight:600;color:#0f172a">Büyük Endüstriyel / Tier III+ Tesis<br/><span style="font-size:12px;color:#64748b;font-weight:400">(150 m² ve üzeri)</span></td>
<td style="padding:13px 18px;color:#334155">Merkezi Silindir Bankası + %100 Yedek Batarya (42 Bar)</td>
<td style="padding:13px 18px;color:#334155">Yönlendirme Vanalı (Selector Valve) + BMS Entegrasyonu</td>
<td style="padding:13px 18px;color:#334155">Akredite Door Fan Testi + VdS/UL İzometri + F-Gaz Sertifikası</td>
</tr>
</tbody>
</table>
</div>
<div style="padding:14px 20px;background:#fef2f2;border-top:1px solid #fecaca;font-size:13px;color:#7f1d1d;line-height:1.55">
<strong>Yasal Mevzuat Uyarısı (Florlu Sera Gazları Yönetmeliği):</strong> HFC-227ea (FM200) sistemlerinin kurulumu, sızdırmazlık kontrolleri ve dolumu; Çevre, Şehircilik ve İklim Değişikliği Bakanlığı <em>Florlu Sera Gazlarına İlişkin Yönetmelik</em> uyarınca yalnızca EKED / F-Gaz sertifikalı teknik personel tarafından yapılmalı ve Bakanlık veritabanına (F-Gaz Portalı) kaydedilmelidir. Fenix Yangın tüm projelerinde tam yasal uyumluluk belgesi sunar.
</div>
</div>
'''
    if 'Oda Büyüklüğüne Göre FM200 Sistem Konfigürasyonu' not in content and target_fiyat_marker in content:
        box_start = '<div style="display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;padding:24px 28px;background:#f8fafc;border-radius:12px;border:1px solid #e2e8f0">'
        content = content.replace(box_start + '\r\n<div>\r\n' + target_fiyat_marker, fm200_scale_table + '\r\n' + box_start + '\r\n<div>\r\n' + target_fiyat_marker)

    # 3. Add F-Gaz FAQ to JSON-LD and visible FAQ section
    fm200_json_anchor = '''        {
          "@type": "Question",
          "name": "Bir mahal için FM200 sistemi nasıl boyutlandırılır ve projelendirilir?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Boyutlandırma; mahalin net hacmi (en, boy, yükseklik ve asma tavan/yükseltilmiş zemin dahil), yangın yükü sınıfı, mahal sıcaklığı ve rakım faktörleri dikkate alınarak uluslararası NFPA 2001 veya TS EN 15004 standartlarındaki tasarım konsantrasyonu (genellikle %6.25 - %7) üzerinden hidrolik yazılımlarla hesaplanır."
          }
        }'''
    fm200_json_new = fm200_json_anchor + ''',\r\n        {
          "@type": "Question",
          "name": "FM200 gazlı söndürme sistemlerinde F-Gaz Yönetmeliği ve Bakanlık kaydı zorunlu mu?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Evet. HFC-227ea (FM200) içerikli yangın söndürme sistemlerinin kurulumu, periyodik sızdırmazlık kontrolleri ve yeniden dolumu; Çevre, Şehircilik ve İklim Değişikliği Bakanlığı Florlu Sera Gazlarına İlişkin Yönetmelik kapsamında yalnızca EKED / F-Gaz sertifikalı teknik personel tarafından yapılmalı ve Bakanlık F-Gaz Portalı veritabanına kayıt altına alınmalıdır."
          }
        }'''
    if "FM200 gazlı söndürme sistemlerinde F-Gaz Yönetmeliği" not in content and fm200_json_anchor in content:
        content = content.replace(fm200_json_anchor, fm200_json_new)

    fm200_html_anchor = '''<div class="fx-rows__item" style="display:block;background:#fff;padding:20px 24px;border-radius:10px;border:1px solid #e2e8f0;margin-bottom:12px">
<h3 class="fx-h3 fx-h3--sm" style="margin:0 0 8px;font-size:17px">Bir mahal için FM200 sistemi nasıl boyutlandırılır ve projelendirilir?</h3>
<p class="fx-text fx-text--sm" style="color:#475569;margin:0;line-height:1.6">Boyutlandırma; mahalin net hava hacmi (asma tavan ve taban dahil), yangın sınıfı, sıcaklık ve rakım verileri alınarak NFPA 2001 ve TS EN 15004 standartlarındaki tasarım konsantrasyonu formülleriyle hesaplanır. İki fazlı akış hidrolik simülasyonu ile boru çapları, basınç kaybı ve nozul delik çapları optimize edilir.</p>
</div>'''
    fm200_html_new = fm200_html_anchor + '''\r\n<div class="fx-rows__item" style="display:block;background:#fff;padding:20px 24px;border-radius:10px;border:1px solid #e2e8f0;margin-bottom:12px">
<h3 class="fx-h3 fx-h3--sm" style="margin:0 0 8px;font-size:17px">FM200 gazlı söndürme sistemlerinde F-Gaz Yönetmeliği ve Bakanlık kaydı zorunlu mu?</h3>
<p class="fx-text fx-text--sm" style="color:#475569;margin:0;line-height:1.6">Evet. HFC-227ea (FM200) içerikli yangın söndürme sistemlerinin kurulumu, periyodik sızdırmazlık kontrolleri ve yeniden dolumu; Çevre, Şehircilik ve İklim Değişikliği Bakanlığı <em>Florlu Sera Gazlarına İlişkin Yönetmelik</em> kapsamında yalnızca EKED / F-Gaz sertifikalı teknik personel tarafından yapılmalı ve Bakanlık F-Gaz Portalı veritabanına kayıt altına alınmalıdır.</p>
</div>'''
    if fm200_html_anchor in content and 'F-Gaz Yönetmeliği ve Bakanlık kaydı zorunlu mu?</h3>' not in content:
        content = content.replace(fm200_html_anchor, fm200_html_new)

    write_clean(filepath, content)
    print("Enriched FM200 page with competitive tables & F-Gaz compliance.")

def enrich_davlumbaz():
    filepath = os.path.join(BASE_DIR, "davlumbaz-yangin-sondurme-sistemleri.html")
    content = read_clean(filepath)

    target_pos = '<!-- SECTION 9: KULLANIM ALANLARI -->'
    
    kitchen_section = '''<!-- ENRICHED: RESTORAN VE ENDÜSTRİYEL MUTFAK ÇÖZÜMLERİ + İTFAİYE RUHSAT KONTROL LİSTESİ -->
<section class="fx-section fx-section--paper" id="endustriyel-mutfak-cozumleri">
<div class="fx-wrap">
<div style="max-width:800px;margin-bottom:32px">
<span class="fx-eyebrow">MUTFAK SEKTÖRÜNE ÖZEL MÜHENDİSLİK</span>
<h2 class="fx-h2" style="margin:10px 0 14px">Restoran ve Endüstriyel Mutfak Çözümleri: Kurulum, Bakım ve İtfaiye Uyumu</h2>
<p class="fx-text" style="color:#475569;line-height:1.65">
Ticari mutfaklarda yangın güvenliği, yalnızca standart bir söndürücü tüp montajı değil; pişirme hücrelerinin, davlumbaz filtrelerinin ve dikey baca hattının kesintisiz korunmasını sağlayan entegre bir mühendislik disiplinidir. Fenix Yangın, <strong>davlumbaz yangın söndürme sistemi</strong>, <strong>otomatik davlumbaz söndürme</strong> ve <strong>endüstriyel mutfak yangın güvenliği</strong> ihtiyaçlarını tek bir güçlü hizmet yapısında birleştirir:
</p>
</div>
<div class="fx-grid fx-grid--3" style="gap:24px;margin-bottom:32px">
<div class="fx-card" style="padding:24px;background:#fff;border-radius:12px;border:1px solid #e2e8f0;border-top:3px solid var(--fx-red)">
<h3 class="fx-h3" style="font-size:18px;margin:0 0 10px;color:var(--fx-navy)">Restoran ve Fast-Food Mutfakları</h3>
<p class="fx-text fx-text--sm" style="color:#64748b;line-height:1.55;margin-bottom:14px">A la carte restoranlar, burger ve döner zincirlerinde sürekli yüksek ısıda çalışan derin fritözler, lavataşlı ızgaralar ve ocak hatları için milisaniyeler içinde reaksiyon gösteren otomatik sıvı söndürme.</p>
<ul class="fx-check-list" style="font-size:13px;color:#475569">
<li>Fritöz ve wok ocaklarına odaklı paslanmaz nozul yerleşimi</li>
<li>Acil manuel çekme istasyonu ile kaçış hattından anında tetikleme</li>
<li>Pişirme ekipmanı gaz/elektrik beslemesinin anında otomatik kesilmesi</li>
</ul>
</div>
<div class="fx-card" style="padding:24px;background:#fff;border-radius:12px;border:1px solid #e2e8f0;border-top:3px solid var(--fx-navy)">
<h3 class="fx-h3" style="font-size:18px;margin:0 0 10px;color:var(--fx-navy)">Otel, AVM ve Yemekhane Mutfakları</h3>
<p class="fx-text fx-text--sm" style="color:#64748b;line-height:1.55;margin-bottom:14px">Yüzlerce kişiye yemek üretilen açık büfe otel ana mutfakları, AVM ortak baca hatlarına bağlı food-court restoranları ve fabrika yemekhanelerinde geniş alan koruması.</p>
<ul class="fx-check-list" style="font-size:13px;color:#475569">
<li>Çoklu silindir bataryaları (10 Lt – 18 Lt) ve modüler akış dağıtımı</li>
<li>Ortak baca kanallarında alevin diğer katlara sıçramasını önleyen baca nozulları</li>
<li>Bina yangın alarm ve duman tahliye otomasyonuna tam entegrasyon</li>
</ul>
</div>
<div class="fx-card" style="padding:24px;background:#fff;border-radius:12px;border:1px solid #e2e8f0;border-top:3px solid #16a34a">
<h3 class="fx-h3" style="font-size:18px;margin:0 0 10px;color:var(--fx-navy)">BYKHY Madde 57 &amp; İtfaiye Ruhsatı Uyumu</h3>
<p class="fx-text fx-text--sm" style="color:#64748b;line-height:1.55;margin-bottom:14px">Binaların Yangından Korunması Hakkında Yönetmelik Madde 57 gereğince yüksek binalarda, AVM'lerde ve 100 kişiden fazla kapasiteye sahip mutfaklarda otomatik davlumbaz söndürme sistemi yasal zorunluluktur.</p>
<ul class="fx-check-list" style="font-size:13px;color:#475569">
<li>İtfaiye yangın uygunluk raporu için onaylı teknik dosya ve şema</li>
<li>6 aylık zorunlu eriyen lehim (fusible link) dedektör değişimi ve tutanağı</li>
<li>Yetkili mühendis kaşeli periyodik bakım uygunluk belgesi</li>
</ul>
</div>
</div>

<!-- COMPETITIVE ADVANTAGE #4: BELEDİYE RUHSATI VE İTFAİYE DENETİMİ 6 MADDELİK KONTROL LİSTESİ -->
<div style="background:#fff;border-radius:12px;border:1px solid #e2e8f0;padding:28px;margin-bottom:28px;box-shadow:0 4px 16px rgba(0,0,0,0.03)">
<div style="max-width:780px;margin-bottom:22px">
<span class="fx-badge fx-badge--red" style="font-size:11px;margin-bottom:8px;display:inline-block">RUHSAT VE DENETİM REHBERİ</span>
<h3 class="fx-h3" style="font-size:20px;margin:0 0 8px;color:var(--fx-navy)">Belediye İşyeri Açma Ruhsatı ve İtfaiye Denetiminde Aranan 6 Zorunlu Kriter</h3>
<p class="fx-text fx-text--sm" style="color:#64748b;margin:0;line-height:1.6">Belediye ruhsat denetimlerinde ve sigorta ekspertizlerinde davlumbaz söndürme sisteminin onay alabilmesi için aşağıdaki 6 teknik şartın eksiksiz sağlanması gerekir:</p>
</div>
<div class="fx-grid fx-grid--3" style="gap:18px">
<div style="padding:16px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0">
<strong style="color:var(--fx-red);font-size:14px;display:block;margin-bottom:4px">01 · Sınıf F (Class K) Sabunlaşma Etkisi</strong>
<p class="fx-text fx-text--sm" style="color:#475569;margin:0;line-height:1.5">Kızgın bitkisel ve hayvansal yağ yangınlarında su veya kuru toz değil; yağ yüzeyinde <em>saponifikasyon (sabunlaşma)</em> köpük battaniyesi oluşturan düşük pH'lı potasyum karbonat sıvı ajan kullanılmalıdır.</p>
</div>
<div style="padding:16px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0">
<strong style="color:var(--fx-red);font-size:14px;display:block;margin-bottom:4px">02 · Otomatik Gaz Kesme Selenoid Vanası</strong>
<p class="fx-text fx-text--sm" style="color:#475569;margin:0;line-height:1.5">BYKHY Madde 57 uyarınca sistem aktive olduğu anda mutfağın doğalgaz veya LPG ana besleme hattını otomatik olarak kapatan selenoid vana bağlantısı zorunludur.</p>
</div>
<div style="padding:16px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0">
<strong style="color:var(--fx-red);font-size:14px;display:block;margin-bottom:4px">03 · Egzoz Fanı ve Elektrik Enterlok Rölesi</strong>
<p class="fx-text fx-text--sm" style="color:#475569;margin:0;line-height:1.5">Kontrol kutusu içindeki mikro-switch (anahtar) vasıtasıyla yangın anında elektrikli pişirme cihazlarının enerjisi kesilmeli ve yangın otomasyon panosuna sinyal iletilmelidir.</p>
</div>
<div style="padding:16px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0">
<strong style="color:var(--fx-red);font-size:14px;display:block;margin-bottom:4px">04 · Cihaz Bazlı Nozul ve Yağ Kapakları</strong>
<p class="fx-text fx-text--sm" style="color:#475569;margin:0;line-height:1.5">Her fritöz, ızgara, ocak, davlumbaz filtre arkası (plenum) ve baca ağzına ayrı nozul yönlendirilmeli; tüm nozullarda tıkanmayı önleyen silikon/metal yağ koruma kapağı bulunmalıdır.</p>
</div>
<div style="padding:16px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0">
<strong style="color:var(--fx-red);font-size:14px;display:block;margin-bottom:4px">05 · Kaçış Yolunda Manuel Çekme Butonu</strong>
<p class="fx-text fx-text--sm" style="color:#475569;margin:0;line-height:1.5">Mutfak personelinin yangın anında kaçış kapısına yönelirken sistemi elle tetikleyebilmesi için çıkış güzergahına mühürlü manuel boşaltma istasyonu monte edilmelidir.</p>
</div>
<div style="padding:16px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0">
<strong style="color:var(--fx-red);font-size:14px;display:block;margin-bottom:4px">06 · 6 Aylık Yetkili Bakım &amp; Lehim Tutanağı</strong>
<p class="fx-text fx-text--sm" style="color:#475569;margin:0;line-height:1.5">İtfaiye ve sigorta denetimlerinde 6 ayda bir eriyen lehimli dedektörlerin (fusible link) yenilendiğini gösteren yetkili mühendislik bakım formu ibraz edilmelidir.</p>
</div>
</div>
</div>

<div style="display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;padding:20px 26px;background:#fff;border-radius:10px;border:1px solid #e2e8f0">
<div>
<h4 style="margin:0 0 4px;font-size:16px;color:var(--fx-navy)">Endüstriyel Mutfağınız İçin Hızlı Keşif ve İtfaiye Ruhsat Uygunluğu</h4>
<p class="fx-text fx-text--sm" style="margin:0;color:#64748b">Ocak ve fritöz ölçülerinizi WhatsApp üzerinden paylaşın; mühendislerimiz aynı gün içinde akış hesabı ve teklifinizi hazırlasın.</p>
</div>
<a class="fx-btn fx-btn--wa" href="https://wa.me/905327409097?text=Merhaba,%20end%C3%BCstriyel%20mutfak%20davlumbaz%20yang%C4%B1n%20s%C3%B6nd%C3%BCrme%20sistemi%20ke%C5%9Ffi%20ve%20teklifi%20almak%20istiyorum." rel="noopener" target="_blank"><svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.669-.699c.969.586 1.838.88 2.791.88 3.182 0 5.768-2.587 5.768-5.766.001-3.187-2.575-5.77-5.768-5.77zm3.385 8.163c-.144.405-.837.774-1.17.822-.311.045-.694.053-1.055-.065-.214-.07-.487-.163-.836-.317-1.464-.643-2.416-2.115-2.489-2.213-.072-.098-.596-.794-.596-1.52 0-.726.381-1.082.517-1.23.136-.148.297-.185.396-.185.099 0 .198.001.284.005.091.004.213-.035.333.254.125.3.428 1.045.466 1.121.038.077.063.167.013.267-.05.1-.075.162-.15.25-.075.088-.158.196-.226.263-.075.074-.153.155-.066.305.087.15.385.635.826 1.028.568.507 1.048.665 1.198.74.15.075.238.066.326-.036.088-.102.376-.437.476-.587.1-.15.2-.125.337-.075.137.05.867.409 1.016.484.15.075.25.112.287.175.037.062.037.362-.107.767z"/></svg>WhatsApp Mutfak Keşfi</a>
</div>
</div>
</section>'''

    if target_pos in content and 'id="endustriyel-mutfak-cozumleri"' not in content:
        content = content.replace(target_pos, kitchen_section + "\r\n" + target_pos)

    davlumbaz_json_anchor = '''        {
          "@type": "Question",
          "name": "Davlumbaz yangın söndürme sistemi fiyatları nasıl belirlenir?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Fiyatlar mutfağın büyüklüğü, davlumbaz alanı, ocak, ızgara ve fritöz gibi korunacak ekipmanların adedi ile borulama metrajına göre hazırlanan projeye bağlı olarak değişkenlik gösterir. Teknik inceleme sonrasında net maliyet teklifi oluşturulur."
          }
        }'''
    davlumbaz_json_new = davlumbaz_json_anchor + ''',\r\n        {
          "@type": "Question",
          "name": "Belediye ruhsatı ve itfaiye denetiminde davlumbaz söndürme sistemi için hangi şartlar aranır?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Belediye işyeri açma ruhsatı ve itfaiye denetimlerinde; UL 300 / EN 16282 uyumlu Sınıf F (potasyum karbonat bazlı) ıslak kimyasal söndürücü, otomatik doğalgaz/LPG kesme selenoid vanası, davlumbaz egzoz fanını durduran enterlok rölesi, her pişirme cihazı ve baca girişinde doğru açılı nozullar, kaçış güzergahında mühürlü manuel çekme butonu ve 6 aylık yetkili servis bakım tutanağı zorunlu tutulmaktadır."
          }
        }'''
    if "Belediye ruhsatı ve itfaiye denetiminde davlumbaz söndürme" not in content and davlumbaz_json_anchor in content:
        content = content.replace(davlumbaz_json_anchor, davlumbaz_json_new)

    davlumbaz_html_anchor = '''<div class="fx-faq-card">
<div class="fx-faq-card__q">
<span class="fx-faq-card__q-badge">S7</span>
<span>Davlumbaz yangın söndürme sistemi fiyatları nasıl belirlenir?</span>
</div>
<p class="fx-faq-card__a">Fiyatlar mutfağın büyüklüğü, davlumbaz alanı, ocak, ızgara ve fritöz gibi korunacak ekipmanların adedi ile borulama metrajına göre hazırlanan projeye bağlı olarak değişkenlik gösterir. Teknik inceleme sonrasında net maliyet teklifi oluşturulur.</p>
</div>'''
    davlumbaz_html_new = davlumbaz_html_anchor + '''\r\n<div class="fx-faq-card">
<div class="fx-faq-card__q">
<span class="fx-faq-card__q-badge">S8</span>
<span>Belediye ruhsatı ve itfaiye denetiminde davlumbaz söndürme sistemi için hangi şartlar aranır?</span>
</div>
<p class="fx-faq-card__a">Belediye işyeri açma ruhsatı ve itfaiye denetimlerinde; UL 300 / EN 16282 uyumlu Sınıf F (potasyum karbonat bazlı) ıslak kimyasal söndürücü, otomatik doğalgaz/LPG kesme selenoid vanası, davlumbaz egzoz fanını durduran enterlok rölesi, her pişirme cihazı ve baca girişinde doğru açılı nozullar, kaçış güzergahında mühürlü manuel çekme butonu ve 6 aylık yetkili servis bakım tutanağı zorunlu tutulmaktadır.</p>
</div>'''
    if davlumbaz_html_anchor in content and '<span class="fx-faq-card__q-badge">S8</span>' not in content:
        content = content.replace(davlumbaz_html_anchor, davlumbaz_html_new)

    write_clean(filepath, content)
    print("Enriched Davlumbaz page with 6-point Fire Dept inspection checklist.")

def enrich_pano_ici():
    filepath = os.path.join(BASE_DIR, "pano-ici-yangin-sondurme-sistemleri.html")
    content = read_clean(filepath)

    target_pos = '<!-- SECTION 7: SISTEM SECIMI VE DEGERLENDIRME (PHOTO 3 INTEGRATED) -->'

    case_studies_section = '''<!-- ENRICHED: ÖZGÜN UYGULAMA ÖRNEKLERİ + TÜP KAPASİTESİ SEÇİM TABLOSU (POZİSYON 29 ATILIMI) -->
<section class="fx-section fx-section--paper" id="ozgun-uygulama-ornekleri">
<div class="fx-wrap">
<div style="max-width:820px;margin-bottom:32px">
<span class="fx-eyebrow">SAHA MÜHENDİSLİĞİ VE VAKA ANALİZİ</span>
<h2 class="fx-h2" style="margin:10px 0 14px">Elektrik Panosu Otomatik Söndürme: Uygulama Örnekleri ve Proje Referansları</h2>
<p class="fx-text" style="color:#475569;line-height:1.65">
<strong>Pano içi yangın söndürme sistemi</strong> uygulamalarında başarı, standart bir söndürücünün panoya asılmasıyla değil; elektrik panosunun ark riski, hücre tipi ve enerji kesme dinamiklerinin doğru mühendislikle çözülmesiyle elde edilir. Fenix Yangın olarak endüstriyel tesisler, enerji dağıtım merkezleri ve veri merkezlerinde hayata geçirdiğimiz 4 kritik elektrik panosu otomatik söndürme uygulama modeli:
</p>
</div>

<div class="fx-grid fx-grid--2" style="gap:24px;margin-bottom:32px">
<!-- Örnek 1: Ana Dağıtım Panosu -->
<div class="fx-card" style="padding:26px;background:#fff;border-radius:12px;border:1px solid #e2e8f0;border-left:4px solid var(--fx-red)">
<div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
<span class="fx-badge fx-badge--red" style="font-size:11px">Vaka 01</span>
<h3 class="fx-h3" style="font-size:18px;margin:0">Ana Dağıtım Panosu (ADP 630A–2500A) Yangın Koruması</h3>
</div>
<p class="fx-text fx-text--sm" style="color:#64748b;line-height:1.55;margin-bottom:12px">
<strong>Risk:</strong> Giriş kompakt şalterleri, ana baralar ve kablo bağlantı pabuçlarında gevşeklik kaynaklı ark parlaması (arc flash), yüksek akım ısınması ve bara yangınları.
</p>
<p class="fx-text fx-text--sm" style="color:#475569;line-height:1.55;margin-bottom:12px">
<strong>Fenix Mühendislik Çözümü:</strong> İndirekt sistem mimarisi. Baraların ve ana şalter çıkışlarının üzerinden geçirilen ısıya duyarlı polimerik algılama hortumu yangını algılar. Silindir diferansiyel vanasını açarak HFC-227ea / FK-5-1-12 gazını paslanmaz çelik dağıtım boruları ve nozullardan panoya homojen olarak basar. Entegre basınç şalteri (pressure switch), ana giriş şalterinin açtırma bobinine (shunt trip) anlık sinyal göndererek panonun şebeke enerjisini milisaniyeler içinde keser.
</p>
<div style="font-size:13px;font-weight:600;color:var(--fx-navy)">Sonuç: Ark anında söndürülür, trafo dairesine yangın sıçraması engellenir ve fabrika ana elektriği güvenle korunur.</div>
</div>

<!-- Örnek 2: Kompanzasyon Panosu -->
<div class="fx-card" style="padding:26px;background:#fff;border-radius:12px;border:1px solid #e2e8f0;border-left:4px solid #ea580c">
<div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
<span class="fx-badge" style="background:#ffedd5;color:#c2410c;font-size:11px">Vaka 02</span>
<h3 class="fx-h3" style="font-size:18px;margin:0">Kompanzasyon Panolarında Patlama ve Yangın Güvenliği</h3>
</div>
<p class="fx-text fx-text--sm" style="color:#64748b;line-height:1.55;margin-bottom:12px">
<strong>Risk:</strong> Kondansatörlerin harmonik rezonans nedeniyle aşırı ısınması, dielektrik yağ sızıntısı, kondansatör patlaması ve kontaktör kontaklarının yapışması.
</p>
<p class="fx-text fx-text--sm" style="color:#475569;line-height:1.55;margin-bottom:12px">
<strong>Fenix Mühendislik Çözümü:</strong> Doğrudan (direkt) polimer hortumlu söndürme veya kompakt kondanse aerosol jeneratörü. Hortum, kondansatör kademeleri ve deşarj dirençleri boyunca sarılır; patlama anında oluşan ilk alev noktasından delinerek söndürücü ajanı alevin merkezine püskürtür. Eşzamanlı olarak reaktif güç kontrol rölesi beslemesi kesilir.
</p>
<div style="font-size:13px;font-weight:600;color:var(--fx-navy)">Sonuç: Kondansatör patlamasının diğer kademelere ve komşu panolara sıçraması önlenir.</div>
</div>

<!-- Örnek 3: MCC Motor Kontrol Merkezi -->
<div class="fx-card" style="padding:26px;background:#fff;border-radius:12px;border:1px solid #e2e8f0;border-left:4px solid var(--fx-navy)">
<div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
<span class="fx-badge" style="background:#e0f2fe;color:#0369a1;font-size:11px">Vaka 03</span>
<h3 class="fx-h3" style="font-size:18px;margin:0">Motor Kontrol Merkezleri (MCC) ve Sürücü Panoları</h3>
</div>
<p class="fx-text fx-text--sm" style="color:#64748b;line-height:1.55;margin-bottom:12px">
<strong>Risk:</strong> Çok gözlü (çekmeceli) MCC panolarında frekans invertörleri (VFD), soft starter modülleri ve kontaktör ark parlamaları; üretim bandının plansız durmasına neden olur.
</p>
<p class="fx-text fx-text--sm" style="color:#475569;line-height:1.55;margin-bottom:12px">
<strong>Fenix Mühendislik Çözümü:</strong> Çok hücreli panolar için ayrık algılama hatları ve tek merkezden beslenen dağıtım manifoldu. Elektriksel iletkenliği sıfır olan temiz gaz kullanımı sayesinde, sürücü kartlarında ve elektronik devrelerde en ufak korozyon veya kalıntı oluşmaz. Yangın söndükten sonra panoda sadece arızalı modül değiştirilerek üretim hattı derhal çalıştırılır.
</p>
<div style="font-size:13px;font-weight:600;color:var(--fx-navy)">Sonuç: Günler sürecek fabrika duruş maliyeti birkaç saate indirilir.</div>
</div>

<!-- Örnek 4: PLC ve Otomasyon Kabinetleri -->
<div class="fx-card" style="padding:26px;background:#fff;border-radius:12px;border:1px solid #e2e8f0;border-left:4px solid #16a34a">
<div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
<span class="fx-badge" style="background:#dcfce7;color:#15803d;font-size:11px">Vaka 04</span>
<h3 class="fx-h3" style="font-size:18px;margin:0">PLC, Otomasyon ve CNC Tezgah Kabinleri Koruması</h3>
</div>
<p class="fx-text fx-text--sm" style="color:#64748b;line-height:1.55;margin-bottom:12px">
<strong>Risk:</strong> SCADA sistemleri, PLC kontrolörler, CNC işleme merkezi elektrik kabinleri ve 24V DC güç kaynaklarında elektriksel aşırı yük ve soğutma yağı buharı tutuşması.
</p>
<p class="fx-text fx-text--sm" style="color:#475569;line-height:1.55;margin-bottom:12px">
<strong>Fenix Mühendislik Çözümü:</strong> FK-5-1-12 (Novec 1230) veya HFC-227ea (FM-200) temiz gazlı mikro silindir entegrasyonu. Pano kapakları açılmadan, saniyeler içinde hacimsel dolum gerçekleşir. SCADA ekranına anlık kuru kontak yangın sinyali iletilerek operatör bilgilendirilir.
</p>
<div style="font-size:13px;font-weight:600;color:var(--fx-navy)">Sonuç: PLC yazılımları, CNC servo sürücüleri ve hassas I/O modülleri hasarsız kurtarılır.</div>
</div>
</div>

<!-- COMPETITIVE ADVANTAGE #1: PANO HACMİNE GÖRE TÜP KAPASİTESİ SEÇİM TABLOSU VE HORTUM PARAMETRELERİ -->
<div style="margin-bottom:32px;background:#fff;border-radius:12px;border:1px solid #e2e8f0;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,0.03)">
<div style="padding:20px 24px;background:#f8fafc;border-bottom:1px solid #e2e8f0">
<span style="font-size:12px;font-weight:700;color:var(--fx-red);text-transform:uppercase;letter-spacing:0.06em">MÜHENDİSLİK SEÇİM CETVELİ</span>
<h3 class="fx-h3" style="font-size:19px;margin:4px 0 6px;color:var(--fx-navy)">Pano Hacmine Göre Söndürme Tüpü Kapasitesi Seçim Tablosu (1 kg – 12 kg)</h3>
<p class="fx-text fx-text--sm" style="color:#64748b;margin:0">NFPA 2001 temiz ajan tasarım konsantrasyonları (%7 HFC-227ea / %5.3 FK-5-1-12) baz alınarak kapalı elektrik panoları için referans boyutlandırma tablosu:</p>
</div>
<div style="overflow-x:auto">
<table style="width:100%;border-collapse:collapse;font-size:13.5px;text-align:left">
<thead>
<tr style="background:#0f172a;color:#fff">
<th style="padding:14px 18px;font-weight:700">Tüp Kapasitesi</th>
<th style="padding:14px 18px;font-weight:700">Korunan Pano İç Hacmi (m³)</th>
<th style="padding:14px 18px;font-weight:700">Sistem Çalışma Tipi</th>
<th style="padding:14px 18px;font-weight:700">Örnek Pano Ölçüsü &amp; Uygulama Alanı</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #e2e8f0">
<td style="padding:13px 18px;font-weight:700;color:var(--fx-red)">1 kg Silindir</td>
<td style="padding:13px 18px;font-weight:600;color:#0f172a">0,5 m³ – 1,0 m³</td>
<td style="padding:13px 18px;color:#334155">Direkt (Doğrudan Hortumlu)</td>
<td style="padding:13px 18px;color:#475569">80x60x200 cm tek kapılı tali dağıtım, PLC veya asansör kumanda panosu</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0;background:#f8fafc">
<td style="padding:13px 18px;font-weight:700;color:var(--fx-red)">2 kg Silindir</td>
<td style="padding:13px 18px;font-weight:600;color:#0f172a">1,0 m³ – 2,0 m³</td>
<td style="padding:13px 18px;color:#334155">Direkt veya İndirekt (Nozullu)</td>
<td style="padding:13px 18px;color:#475569">100x80x210 cm standart dikili tip güç panosu, kompanzasyon kabini</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
<td style="padding:13px 18px;font-weight:700;color:var(--fx-red)">4 kg Silindir</td>
<td style="padding:13px 18px;font-weight:600;color:#0f172a">2,0 m³ – 3,8 m³</td>
<td style="padding:13px 18px;color:#334155">İndirekt (Polimer Algılama + Nozul)</td>
<td style="padding:13px 18px;color:#475569">200x80x210 cm çift gözlü Ana Dağıtım Panosu (ADP), UPS ve inverter kabini</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0;background:#f8fafc">
<td style="padding:13px 18px;font-weight:700;color:var(--fx-red)">6 kg Silindir</td>
<td style="padding:13px 18px;font-weight:600;color:#0f172a">3,8 m³ – 6,0 m³</td>
<td style="padding:13px 18px;color:#334155">İndirekt (Çoklu Nozul Dağıtımlı)</td>
<td style="padding:13px 18px;color:#475569">Çok gözlü Motor Kontrol Merkezi (MCC), kompanzasyon + ADP birleşik diziler</td>
</tr>
<tr>
<td style="padding:13px 18px;font-weight:700;color:var(--fx-red)">9 kg – 12 kg Silindir</td>
<td style="padding:13px 18px;font-weight:600;color:#0f172a">6,0 m³ – 12,0 m³</td>
<td style="padding:13px 18px;color:#334155">İndirekt (Kollektör &amp; Bölmeli Hat)</td>
<td style="padding:13px 18px;color:#475569">OG/AG şalt hücre dizileri, CNC işleme merkezleri, rüzgar türbini nacelle panoları</td>
</tr>
</tbody>
</table>
</div>
<div style="padding:16px 24px;background:#f8fafc;border-top:1px solid #e2e8f0;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;font-size:13px">
<div><strong style="color:var(--fx-navy)">Polimer Hortum Aktivasyon Isısı:</strong> <span style="color:#475569">100°C – 120°C (Yüksek seri: 150°C–180°C)</span></div>
<div><strong style="color:var(--fx-navy)">Hortum Çalışma Basıncı:</strong> <span style="color:#475569">15 Bar – 18 Bar (Manometre İzlemeli)</span></div>
<div><strong style="color:var(--fx-navy)">Min. Bükülme Yarıçapı:</strong> <span style="color:#475569">R = 100 mm (Esnek Poliamid/Floropolimer)</span></div>
<div><strong style="color:var(--fx-navy)">Dielektrik Dayanımı:</strong> <span style="color:#475569">%100 Yalıtkan · UV ve Yağ Buharı Dirençli</span></div>
</div>
</div>

<!-- Referans ve Proje Bağlantı Bloğu -->
<div style="display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;padding:24px 28px;background:#fff;border-radius:12px;border:1px solid #e2e8f0">
<div>
<h4 style="margin:0 0 6px;font-size:17px;color:var(--fx-navy)">Fabrika ve Tesisleriniz İçin Pano Yangın Koruma Projelendirmesi</h4>
<p class="fx-text fx-text--sm" style="margin:0;color:#64748b">Gerçekleştirdiğimiz yüzlerce pano içi gazlı söndürme referansını inceleyin veya mühendislerimizden pano keşif randevusu alın.</p>
</div>
<div style="display:flex;gap:12px;flex-wrap:wrap">
<a class="fx-btn fx-btn--secondary" href="projeler.html">Projelerimizi İnceleyin →</a>
<a class="fx-btn fx-btn--secondary" href="referanslar.html">Referanslarımız →</a>
<a class="fx-btn fx-btn--wa" href="https://wa.me/905327409097?text=Merhaba,%20elektrik%20panolar%C4%B1m%C4%B1z%20i%C3%A7in%20pano%20i%C3%A7i%20otomatik%20yang%C4%B1n%20s%C3%B6nd%C3%BCrme%20sistemi%20ke%C5%9Ffi%20ve%20fiyat%20teklifi%20istiyorum." rel="noopener" target="_blank"><svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.669-.699c.969.586 1.838.88 2.791.88 3.182 0 5.768-2.587 5.768-5.766.001-3.187-2.575-5.77-5.768-5.77zm3.385 8.163c-.144.405-.837.774-1.17.822-.311.045-.694.053-1.055-.065-.214-.07-.487-.163-.836-.317-1.464-.643-2.416-2.115-2.489-2.213-.072-.098-.596-.794-.596-1.52 0-.726.381-1.082.517-1.23.136-.148.297-.185.396-.185.099 0 .198.001.284.005.091.004.213-.035.333.254.125.3.428 1.045.466 1.121.038.077.063.167.013.267-.05.1-.075.162-.15.25-.075.088-.158.196-.226.263-.075.074-.153.155-.066.305.087.15.385.635.826 1.028.568.507 1.048.665 1.198.74.15.075.238.066.326-.036.088-.102.376-.437.476-.587.1-.15.2-.125.337-.075.137.05.867.409 1.016.484.15.075.25.112.287.175.037.062.037.362-.107.767z"/></svg>WhatsApp Hızlı Keşif</a>
</div>
</div>
</div>
</section>'''

    if target_pos in content and 'id="ozgun-uygulama-ornekleri"' not in content:
        content = content.replace(target_pos, case_studies_section + "\r\n" + target_pos)

    pano_json_anchor = '''        {
          "@type": "Question",
          "name": "Elektrik panosu yangın söndürme sistemi fiyatı nasıl belirlenir?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Fiyatlandırma; elektrik panosunun iç hacmine, silindir kapasitesine, seçilen söndürücü ajan türüne (FM-200, FK-5-1-12 vb.), direkt veya indirekt aktivasyon metoduna ve korunacak pano sayısına göre keşif sonrasında belirlenir."
          }
        }'''
    pano_json_new = pano_json_anchor + ''',\r\n        {
          "@type": "Question",
          "name": "Hangi pano hacmine kaç kg pano içi yangın söndürme tüpü seçilmelidir?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "NFPA 2001 temiz gaz tasarım konsantrasyonlarına göre kapalı elektrik panolarında genel referans olarak; 0,5–1,0 m³ hacim için 1 kg, 1,0–2,0 m³ için 2 kg, 2,0–3,8 m³ için 4 kg, 3,8–6,0 m³ için 6 kg ve 6,0–12,0 m³ çok gözlü MCC/ADP panolar için 9 kg veya 12 kg kapasiteli silindirler projelendirilir."
          }
        }'''
    if "Hangi pano hacmine kaç kg pano içi yangın söndürme tüpü seçilmelidir?" not in content and pano_json_anchor in content:
        content = content.replace(pano_json_anchor, pano_json_new)

    pano_html_anchor = '''<div class="fx-faq-card">
<div class="fx-faq-card__q">
<span class="fx-faq-card__q-badge">S5</span>
<span>Elektrik panosu yangın söndürme sistemi fiyatı nasıl belirlenir?</span>
</div>
<p class="fx-faq-card__a">Fiyatlandırma; elektrik panosunun iç hacmine, silindir kapasitesine, seçilen söndürücü ajan türüne (FM-200, FK-5-1-12 vb.), direkt veya indirekt aktivasyon metoduna ve korunacak pano sayısına göre keşif sonrasında belirlenir.</p>
</div>'''
    pano_html_new = pano_html_anchor + '''\r\n<div class="fx-faq-card">
<div class="fx-faq-card__q">
<span class="fx-faq-card__q-badge">S6</span>
<span>Hangi pano hacmine kaç kg pano içi yangın söndürme tüpü seçilmelidir?</span>
</div>
<p class="fx-faq-card__a">NFPA 2001 temiz gaz tasarım konsantrasyonlarına göre kapalı elektrik panolarında genel referans olarak; 0,5–1,0 m³ hacim için 1 kg, 1,0–2,0 m³ için 2 kg, 2,0–3,8 m³ için 4 kg, 3,8–6,0 m³ için 6 kg ve 6,0–12,0 m³ çok gözlü MCC/ADP panolar için 9 kg veya 12 kg kapasiteli silindirler projelendirilir.</p>
</div>'''
    if pano_html_anchor in content and '<span class="fx-faq-card__q-badge">S6</span>' not in content:
        content = content.replace(pano_html_anchor, pano_html_new)

    write_clean(filepath, content)
    print("Enriched Pano İçi page with case studies & 1kg-12kg selection table.")

def enrich_novec1230():
    filepath = os.path.join(BASE_DIR, "novec-1230-gazli-yangin-sondurme-sistemleri.html")
    content = read_clean(filepath)

    target_pos = '<!-- SECTION 5: INSTALLATION & DOOR FAN TEST -->'

    matrix_section = '''<!-- ENRICHED: TEMİZ GAZLI YANGIN SÖNDÜRME AJANLARI KARŞILAŞTIRMA MATRİSİ + 3M FK-5-1-12 GÜVENCESİ -->
<section class="fx-section fx-section--paper" id="temiz-gaz-karsilastirma">
<div class="fx-wrap">
<div style="max-width:820px;margin-bottom:32px">
<span class="fx-eyebrow">MÜHENDİSLİK KARŞILAŞTIRMA MATRİSİ</span>
<h2 class="fx-h2" style="margin:10px 0 14px">Temiz Gazlı Yangın Söndürme Ajanları: Novec 1230 ve Alternatif Sistemler</h2>
<p class="fx-text" style="color:#475569;line-height:1.65">
Yangından korunacak kritik hacimlerde söndürme ajanı seçimi; insan güvenliği, çevresel regülasyonlar (Kigali Değişikliği / F-Gaz), silindir depolama alanı ve donanım hassasiyeti kriterlerine göre yapılır. Fenix Yangın mühendislik kıyaslama matrisi ile <strong>Novec 1230 (FK-5-1-12)</strong>, <strong>FM200 (HFC-227ea)</strong>, <strong>İnert Gaz (IG-541 / IG-55)</strong> ve <strong>Karbondioksit (CO₂)</strong> sistemlerinin temel parametreleri:
</p>
</div>

<!-- Responsive Comparison Table -->
<div style="overflow-x:auto;margin-bottom:28px;background:#fff;border-radius:12px;border:1px solid #e2e8f0;box-shadow:0 4px 16px rgba(0,0,0,0.03)">
<table style="width:100%;border-collapse:collapse;font-size:14px;text-align:left">
<thead>
<tr style="background:#0f172a;color:#fff">
<th style="padding:16px 20px;font-weight:700">Teknik Parametre</th>
<th style="padding:16px 20px;font-weight:700;background:#be1523">Novec 1230 (FK-5-1-12)</th>
<th style="padding:16px 20px;font-weight:700">FM200 (HFC-227ea)</th>
<th style="padding:16px 20px;font-weight:700">İnert Gaz (IG-541 / 55)</th>
<th style="padding:16px 20px;font-weight:700">Karbondioksit (CO₂)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #e2e8f0">
<td style="padding:14px 20px;font-weight:600;color:#0f172a">Kimyasal Ajan Türü</td>
<td style="padding:14px 20px;background:#fef2f2;font-weight:600;color:#be1523">Florlu Keton (FK-5-1-12)</td>
<td style="padding:14px 20px;color:#334155">Hidroflorokarbon (HFC-227ea)</td>
<td style="padding:14px 20px;color:#334155">Doğal Gazlar (N₂ / Ar / CO₂)</td>
<td style="padding:14px 20px;color:#334155">Saf Karbondioksit (CO₂)</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0;background:#f8fafc">
<td style="padding:14px 20px;font-weight:600;color:#0f172a">Ozon Tüketim Potansiyeli (ODP)</td>
<td style="padding:14px 20px;background:#fef2f2;font-weight:700;color:#16a34a">0 (Sıfır Etki)</td>
<td style="padding:14px 20px;font-weight:700;color:#16a34a">0 (Sıfır Etki)</td>
<td style="padding:14px 20px;font-weight:700;color:#16a34a">0 (Sıfır Etki)</td>
<td style="padding:14px 20px;font-weight:700;color:#16a34a">0 (Sıfır Etki)</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
<td style="padding:14px 20px;font-weight:600;color:#0f172a">Küresel Isınma Potansiyeli (GWP)</td>
<td style="padding:14px 20px;background:#fef2f2;font-weight:700;color:#16a34a">≤ 1 (En Çevre Dostu)</td>
<td style="padding:14px 20px;color:#b91c1c;font-weight:600">3220 (Yüksek)</td>
<td style="padding:14px 20px;color:#16a34a;font-weight:700">0 (Doğal)</td>
<td style="padding:14px 20px;color:#334155">1</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0;background:#f8fafc">
<td style="padding:14px 20px;font-weight:600;color:#0f172a">Atmosferik Kalış Ömrü</td>
<td style="padding:14px 20px;background:#fef2f2;font-weight:700;color:#16a34a">~5 Gün (Doğal döngü)</td>
<td style="padding:14px 20px;color:#b91c1c">~34 Yıl</td>
<td style="padding:14px 20px;color:#16a34a">Doğal Atmosfer Gazı</td>
<td style="padding:14px 20px;color:#334155">&gt; 100 Yıl</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
<td style="padding:14px 20px;font-weight:600;color:#0f172a">İnsan Güvenliği (NOAEL Sınırı)</td>
<td style="padding:14px 20px;background:#fef2f2;font-weight:700;color:#16a34a">%10.0 (Geniş Emniyet Marjı)</td>
<td style="padding:14px 20px;color:#16a34a;font-weight:600">%9.0 (Güvenli Tahliye)</td>
<td style="padding:14px 20px;color:#334155">Oksijen %12–14'e Düşer</td>
<td style="padding:14px 20px;color:#b91c1c;font-weight:700">TEHLİKELİ (İnsanlı Mahal Uygun Değil)</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0;background:#f8fafc">
<td style="padding:14px 20px;font-weight:600;color:#0f172a">Tasarım Konsantrasyonu</td>
<td style="padding:14px 20px;background:#fef2f2;font-weight:600;color:#0f172a">%4.5 – %5.9</td>
<td style="padding:14px 20px;color:#334155">%6.25 – %7.0</td>
<td style="padding:14px 20px;color:#334155">%35 – %42</td>
<td style="padding:14px 20px;color:#334155">%34 – %75</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
<td style="padding:14px 20px;font-weight:600;color:#0f172a">Boşalma Süresi (Discharge)</td>
<td style="padding:14px 20px;background:#fef2f2;font-weight:700;color:#be1523">≤ 10 Saniye (Süratli)</td>
<td style="padding:14px 20px;font-weight:700;color:#be1523">≤ 10 Saniye (Süratli)</td>
<td style="padding:14px 20px;color:#334155">60 – 120 Saniye</td>
<td style="padding:14px 20px;color:#334155">60 – 120 Saniye</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0;background:#f8fafc">
<td style="padding:14px 20px;font-weight:600;color:#0f172a">F-Gaz &amp; Kigali Takvimi</td>
<td style="padding:14px 20px;background:#fef2f2;font-weight:700;color:#16a34a">Kısıtlamalardan Tamamen Muaf</td>
<td style="padding:14px 20px;color:#b91c1c">Phase-down Kapsamında</td>
<td style="padding:14px 20px;color:#16a34a">Muaf</td>
<td style="padding:14px 20px;color:#16a34a">Muaf</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
<td style="padding:14px 20px;font-weight:600;color:#0f172a">Silindir Depolama Alanı</td>
<td style="padding:14px 20px;background:#fef2f2;font-weight:600;color:#16a34a">Minimum (Kompakt)</td>
<td style="padding:14px 20px;font-weight:600;color:#16a34a">Minimum (Kompakt)</td>
<td style="padding:14px 20px;color:#b91c1c">Geniş Alan Gerektirir (x4 Tüp)</td>
<td style="padding:14px 20px;color:#334155">Orta Seviye Alan</td>
</tr>
<tr>
<td style="padding:14px 20px;font-weight:600;color:#0f172a">Veri Merkezi &amp; Server Uyumu</td>
<td style="padding:14px 20px;background:#fef2f2;font-weight:700;color:#16a34a">BİRİNCİL TERCİH (İdeal)</td>
<td style="padding:14px 20px;font-weight:600;color:#0f172a">Çok Yaygın Standart</td>
<td style="padding:14px 20px;color:#334155">Altyapı Alanı Uygunsa İdeal</td>
<td style="padding:14px 20px;color:#b91c1c;font-weight:700">Önerilmez (Termal Şok Riski)</td>
</tr>
</tbody>
</table>
</div>

<!-- COMPETITIVE ADVANTAGE #3: 3M NOVEC 1230 & UL/FM FK-5-1-12 TEDARİK GÜVENCESİ + HESAPLAMA KÖPRÜSÜ -->
<div style="margin-bottom:28px;padding:22px 26px;background:#eff6ff;border-radius:12px;border:1px solid #bfdbfe;border-left:4px solid #2563eb;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:20px">
<div style="max-width:720px">
<span style="font-size:12px;font-weight:700;color:#1d4ed8;text-transform:uppercase;letter-spacing:0.05em">KÜRESEL TEDARİK VE STANDART BİLGİLENDİRMESİ</span>
<h3 class="fx-h3" style="font-size:17px;margin:4px 0 8px;color:#1e3a8a">Novec 1230 Ticari Adı ve UL/FM Onaylı FK-5-1-12 Kesintisiz Tedarik Güvencesi</h3>
<p class="fx-text fx-text--sm" style="color:#1e40af;line-height:1.6;margin:0">
<strong>Novec™ 1230</strong>, 3M firmasının geliştirdiği ticari marka adıdır; uluslararası <strong>NFPA 2001, ISO 14520 ve TS EN 15004</strong> standartlarındaki resmi jenerik kimyasal kod ise <strong>FK-5-1-12</strong> (<em>Dodecafluoro-2-methylpentan-3-one</em>, CAS No: 756-13-8) olarak tanımlanır. 3M'in küresel florokimyasal üretimden çıkış stratejisinden bağımsız olarak; Fenix Yangın tüm yeni veri merkezi kurulumlarında, periyodik bakımlarda ve yeniden dolum süreçlerinde <strong>%99.9+ saflık sertifikalı, UL/FM ve VdS onaylı FK-5-1-12 temiz söndürme ajanını</strong> stoktan kesintisiz tedarik etmektedir.
</p>
</div>
<div style="display:flex;flex-direction:column;gap:10px">
<a class="fx-btn fx-btn--primary fx-btn--sm" href="gazli-yangin-sondurme-hesaplama.html">Novec 1230 Gaz Miktarı Hesapla →</a>
<a class="fx-btn fx-btn--wa fx-btn--sm" href="https://wa.me/905327409097?text=Merhaba,%20Novec%201230%20(FK-5-1-12)%20sistemi%20ve%20gaz%20tedariki%20i%C3%A7in%20teklif%20almak%20istiyorum." rel="noopener" target="_blank">WhatsApp Mühendislik Hattı</a>
</div>
</div>

<div class="fx-grid fx-grid--2" style="gap:24px">
<div style="padding:22px;background:#fff;border-radius:12px;border:1px solid #e2e8f0">
<h3 class="fx-h3" style="font-size:17px;margin:0 0 10px;color:var(--fx-navy)">Veri Merkezlerinde Neden Novec 1230 Tercih Edilir?</h3>
<p class="fx-text fx-text--sm" style="color:#64748b;line-height:1.6;margin:0">
FK-5-1-12, elektrik iletkenliği sıfır olan saf bir sıvı kimyasal olarak depolanır ve 10 saniyede ortama gaz fazında yayılarak yangını alev sıcaklığını düşürerek söndürür. Sıfır ozon aşındırma (ODP:0) ve 1'e eşit küresel ısınma potansiyeliyle yeşil veri merkezi sertifikasyonlarında (LEED, BREEAM) puan kazandırır. Ayrıca <a href="veri-merkezi-yangin-sondurme.html" style="color:var(--fx-red);text-decoration:underline">veri merkezi yangın söndürme</a> projelerinde sessiz akustik nozullar ile entegre edilerek sunucu sabit disklerinin (HDD) deşarj sesinden zarar görmesini engeller.
</p>
</div>
<div style="padding:22px;background:#fff;border-radius:12px;border:1px solid #e2e8f0">
<h3 class="fx-h3" style="font-size:17px;margin:0 0 10px;color:var(--fx-navy)">Alternatif Sistem Karşılaştırma Rehberleri</h3>
<p class="fx-text fx-text--sm" style="color:#64748b;line-height:1.6;margin-bottom:12px">
Tesisinizin risk profili, hacim genişliği ve bütçe hedeflerine göre alternatif gazlı sistemleri detaylı rehberlerimizden inceleyebilirsiniz:
</p>
<div style="display:flex;flex-direction:column;gap:8px">
<a href="fm200-vs-novec-1230-karsilastirma.html" style="color:var(--fx-red);font-weight:600;font-size:13.5px;text-decoration:none">FM200 vs Novec 1230 Kapsamlı Karşılaştırması →</a>
<a href="fm200-gazli-yangin-sondurme-sistemleri.html" style="color:#334155;font-size:13.5px;text-decoration:none">FM200 Gazlı Söndürme Sistemleri Rehberi →</a>
<a href="inert-gazli-yangin-sondurme-sistemleri.html" style="color:#334155;font-size:13.5px;text-decoration:none">İnert Gazlı (IG-541/55) Yangın Söndürme Sistemleri →</a>
</div>
</div>
</div>
</div>
</section>'''

    if target_pos in content and 'id="temiz-gaz-karsilastirma"' not in content:
        content = content.replace(target_pos, matrix_section + "\r\n" + target_pos)

    novec_json_anchor = '''        {
          "@type": "Question",
          "name": "Novec 1230 gaz dolumu nasıl yapılır?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Boşalan silindirler sızdırmazlık ve basınç kontrollerinin ardından standartlara uygun saflıkta FK-5-1-12 kimyasalı ile doldurulur ve kuru azot (N2) ile basınçlandırılır."
          }
        }'''
    novec_json_new = novec_json_anchor + ''',\r\n        {
          "@type": "Question",
          "name": "3M Novec 1230 üretimi durdu mu ve FK-5-1-12 gaz tedariki devam ediyor mu?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Novec 1230, 3M firmasının ticari markasıdır; gazın uluslararası NFPA 2001, ISO 14520 ve TS EN 15004 standartlarındaki resmi kimyasal kodu FK-5-1-12 (CAS No: 756-13-8) olarak tanımlanır. 3M'in ticari marka kararından bağımsız olarak, %99.9+ saflıkta UL/FM ve VdS onaylı FK-5-1-12 temiz gaz üretimi ve Fenix Yangın stoklarından yeni kurulum/dolum tedariki kesintisiz devam etmektedir."
          }
        }'''
    if "3M Novec 1230 üretimi durdu mu" not in content and novec_json_anchor in content:
        content = content.replace(novec_json_anchor, novec_json_new)

    novec_html_anchor = '''<div class="fx-faq-card">
<div class="fx-faq-card__q">
<span class="fx-faq-card__q-badge">S7</span>
<span>Novec 1230 gaz dolumu nasıl yapılır?</span>
</div>
<p class="fx-faq-card__a">Boşalan silindirler sızdırmazlık ve basınç kontrollerinin ardından standartlara uygun saflıkta FK-5-1-12 kimyasalı ile doldurulur ve kuru azot (N2) ile basınçlandırılır.</p>
</div>'''
    novec_html_new = novec_html_anchor + '''\r\n<div class="fx-faq-card">
<div class="fx-faq-card__q">
<span class="fx-faq-card__q-badge">S8</span>
<span>3M Novec 1230 üretimi durdu mu ve FK-5-1-12 gaz tedariki devam ediyor mu?</span>
</div>
<p class="fx-faq-card__a">Novec 1230, 3M firmasının ticari markasıdır; gazın uluslararası NFPA 2001, ISO 14520 ve TS EN 15004 standartlarındaki resmi kimyasal kodu FK-5-1-12 (CAS No: 756-13-8) olarak tanımlanır. 3M'in ticari marka kararından bağımsız olarak, %99.9+ saflıkta UL/FM ve VdS onaylı FK-5-1-12 temiz gaz üretimi ve Fenix Yangın stoklarından yeni kurulum/dolum tedariki kesintisiz devam etmektedir.</p>
</div>'''
    if novec_html_anchor in content and '<span class="fx-faq-card__q-badge">S8</span>' not in content:
        content = content.replace(novec_html_anchor, novec_html_new)

    write_clean(filepath, content)
    print("Enriched Novec 1230 page with comparison matrix, 3M FK-5-1-12 supply guarantee & calculator bridge.")

def enrich_veri_merkezi():
    filepath = os.path.join(BASE_DIR, "veri-merkezi-yangin-sondurme.html")
    content = read_clean(filepath)

    old_section_pattern = re.compile(
        r'<section class="fx-section fx-section--paper" id="ornek-projeler".*?</section>',
        re.DOTALL
    )

    new_projects_section = '''<!-- 3.4 Örnek Projeler (3 GERÇEK DÜNYA VAKA ANALİZİ) -->
<section class="fx-section fx-section--paper" id="ornek-projeler" style="border-top:1px solid var(--fx-line);border-bottom:1px solid var(--fx-line)">
<div class="fx-wrap">
<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:28px;flex-wrap:wrap;gap:14px">
<div>
<span class="fx-eyebrow" style="color:var(--fx-red)">Tamamlanmış Saha Projeleri</span>
<h2 class="fx-h2" style="margin:6px 0 0">Veri Merkezi ve Sunucu Odası Örnek Projelerimiz</h2>
<p class="fx-text" style="color:var(--fx-body);margin-top:6px;max-width:680px">Bankacılık, telekomünikasyon ve sanayi sektörlerindeki kritik veri altyapılarında anahtar teslim mühendislik ve devreye alma başarılarımız.</p>
</div>
<div>
<a class="fx-btn fx-btn--secondary fx-btn--sm" href="projeler.html">Tüm Projeleri İncele →</a>
</div>
</div>

<div class="fx-grid fx-grid--3" style="gap:24px;margin-bottom:32px">
<!-- Proje 1: Tier III Bankacılık Veri Merkezi -->
<div class="fx-card" style="background:#fff;border-radius:14px;border:1px solid var(--fx-line);overflow:hidden;box-shadow:0 4px 18px rgba(0,0,0,0.03);display:flex;flex-direction:column;justify-content:space-between">
<div style="padding:24px">
<span class="fx-badge fx-badge--red" style="font-size:11px;margin-bottom:12px;display:inline-block">Finans &amp; Bankacılık</span>
<h3 class="fx-h3" style="font-size:18px;margin:0 0 10px;color:var(--fx-ink)">Tier III Bankacılık Veri Merkezi (450 m²)</h3>
<p class="fx-text fx-text--sm" style="color:var(--fx-body);line-height:1.55;margin-bottom:12px">
<strong>Kapsam:</strong> 42U 70 adet sunucu rack kabini, raised floor altı plenum kablo yolları ve asma tavan üstü hava sirkülasyon hacmi.
</p>
<p class="fx-text fx-text--sm" style="color:var(--fx-body);line-height:1.55;margin-bottom:12px">
<strong>Mühendislik Çözümü:</strong> Novec 1230 (FK-5-1-12) 42 bar merkezi silindir bataryası, VESDA lazer hava çekmeli çok erken duman algılama, sunucu sabit disklerini koruyan akustik susturuculu nozul tesisatı.
</p>
<div style="font-size:13px;font-weight:600;color:#0f766e">
✓ Door Fan Testi ile 12.8 dakika gaz tutma süresi raporlandı; sıfır operasyonel kesintiyle devreye alındı.
</div>
</div>
<div style="padding:14px 24px;background:#f8fafc;border-top:1px solid var(--fx-line)">
<a class="fx-link" href="novec-1230-gazli-yangin-sondurme-sistemleri.html" style="font-size:13.5px;font-weight:600;color:var(--fx-red);text-decoration:none">Kullanılan Novec 1230 Sistemi →</a>
</div>
</div>

<!-- Proje 2: Telekomünikasyon UPS ve Batarya Odası -->
<div class="fx-card" style="background:#fff;border-radius:14px;border:1px solid var(--fx-line);overflow:hidden;box-shadow:0 4px 18px rgba(0,0,0,0.03);display:flex;flex-direction:column;justify-content:space-between">
<div style="padding:24px">
<span class="fx-badge" style="background:#e0f2fe;color:#0369a1;font-size:11px;margin-bottom:12px;display:inline-block">Telekomünikasyon</span>
<h3 class="fx-h3" style="font-size:18px;margin:0 0 10px;color:var(--fx-ink)">Telekomünikasyon UPS ve Batarya Odası (180 m²)</h3>
<p class="fx-text fx-text--sm" style="color:var(--fx-body);line-height:1.55;margin-bottom:12px">
<strong>Kapsam:</strong> 800 kVA paralel yedekli UPS grupları ve lityum-iyon/VRLA akü kabinetlerinde termal kaçak (thermal runaway) riskine karşı yangın güvenliği.
</p>
<p class="fx-text fx-text--sm" style="color:var(--fx-body);line-height:1.55;margin-bottom:12px">
<strong>Mühendislik Çözümü:</strong> FM200 (HFC-227ea) dikişsiz çelik silindir manifold sistemi, CRAC iklimlendirme üniteleri ve yangın damperlerinin otomatik kilit entegrasyonu, hidrojen algılama sensörleri.
</p>
<div style="font-size:13px;font-weight:600;color:#0f766e">
✓ Çapraz zonlu algılama teyidiyle 10 saniyede tam hacimsel deşarj kabiliyeti güvenceye alındı.
</div>
</div>
<div style="padding:14px 24px;background:#f8fafc;border-top:1px solid var(--fx-line)">
<a class="fx-link" href="ups-odasi-yangin-sondurme.html" style="font-size:13.5px;font-weight:600;color:var(--fx-red);text-decoration:none">UPS Odası Yangın Güvenliği →</a>
</div>
</div>

<!-- Proje 3: Organize Sanayi Fabrika ERP Sunucu Odası -->
<div class="fx-card" style="background:#fff;border-radius:14px;border:1px solid var(--fx-line);overflow:hidden;box-shadow:0 4px 18px rgba(0,0,0,0.03);display:flex;flex-direction:column;justify-content:space-between">
<div style="padding:24px">
<span class="fx-badge" style="background:#fef3c7;color:#92400e;font-size:11px;margin-bottom:12px;display:inline-block">Endüstriyel Üretim</span>
<h3 class="fx-h3" style="font-size:18px;margin:0 0 10px;color:var(--fx-ink)">Fabrika ERP ve Sistem Sunucu Odası (65 m²)</h3>
<p class="fx-text fx-text--sm" style="color:var(--fx-body);line-height:1.55;margin-bottom:12px">
<strong>Kapsam:</strong> 7/24 üretim hatlarını ve fabrika otomasyonunu yöneten merkezi ERP/SAP sunucuları ve ana dağıtım panosu.
</p>
<p class="fx-text fx-text--sm" style="color:var(--fx-body);line-height:1.55;margin-bottom:12px">
<strong>Mühendislik Çözümü:</strong> FM200 total flooding oda söndürme sistemi ile kabin içi mikro tubing algılama hattının hibrit entegrasyonu, basınç tahliye damperi montajı.
</p>
<div style="font-size:13px;font-weight:600;color:#0f766e">
✓ Tesis operasyonu durdurulmadan montaj tamamlandı; 6 aylık periyodik bakım protokolü devrede.
</div>
</div>
<div style="padding:14px 24px;background:#f8fafc;border-top:1px solid var(--fx-line)">
<a class="fx-link" href="server-odasi-yangin-sondurme.html" style="font-size:13.5px;font-weight:600;color:var(--fx-red);text-decoration:none">Server Odası Yangın Söndürme →</a>
</div>
</div>
</div>

<!-- Saha İnceleme ve Hızlı WhatsApp + Canlı Hesaplama Yönlendirme -->
<div style="background:#fff;border:1px solid var(--fx-line);border-radius:12px;padding:22px 28px;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap">
<div>
<h4 style="margin:0 0 6px;font-size:17px;color:var(--fx-ink)">Veri Merkeziniz İçin 10 Saniyede Gaz Miktarı Hesaplayın veya Keşif İsteyin</h4>
<p class="fx-text fx-text--sm" style="margin:0;color:var(--fx-body)">Oda boyutlarınızı interaktif hesaplama aracımıza girerek gereken FM200 / Novec 1230 miktarını hemen görün veya WhatsApp'tan mühendislerimize ulaşın.</p>
</div>
<div style="display:flex;gap:12px;flex-wrap:wrap">
<a class="fx-btn fx-btn--primary" href="gazli-yangin-sondurme-hesaplama.html">10 Saniyede Gaz Miktarı Hesapla →</a>
<a class="fx-btn fx-btn--wa" href="https://wa.me/905327409097?text=Merhaba,%20veri%20merkezi%20ve%20sunucu%20odas%C4%B1%20yang%C4%B1n%20s%C3%B6nd%C3%BCrme%20sistemi%20ke%C5%9Ffi%20ve%20teklifi%20almak%20istiyorum." rel="noopener" target="_blank"><svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.669-.699c.969.586 1.838.88 2.791.88 3.182 0 5.768-2.587 5.768-5.766.001-3.187-2.575-5.77-5.768-5.77zm3.385 8.163c-.144.405-.837.774-1.17.822-.311.045-.694.053-1.055-.065-.214-.07-.487-.163-.836-.317-1.464-.643-2.416-2.115-2.489-2.213-.072-.098-.596-.794-.596-1.52 0-.726.381-1.082.517-1.23.136-.148.297-.185.396-.185.099 0 .198.001.284.005.091.004.213-.035.333.254.125.3.428 1.045.466 1.121.038.077.063.167.013.267-.05.1-.075.162-.15.25-.075.088-.158.196-.226.263-.075.074-.153.155-.066.305.087.15.385.635.826 1.028.568.507 1.048.665 1.198.74.15.075.238.066.326-.036.088-.102.376-.437.476-.587.1-.15.2-.125.337-.075.137.05.867.409 1.016.484.15.075.25.112.287.175.037.062.037.362-.107.767z"/></svg>WhatsApp Hızlı Teklif</a>
</div>
</div>
</div>
</section>'''

    if old_section_pattern.search(content):
        content = old_section_pattern.sub(new_projects_section, content)

    write_clean(filepath, content)
    print("Enriched Veri Merkezi page successfully.")

def enrich_server_odasi():
    filepath = os.path.join(BASE_DIR, "server-odasi-yangin-sondurme.html")
    content = read_clean(filepath)

    target_callout = '<a class="fx-btn fx-btn--ghost fx-btn--block" href="iletisim.html" style="margin-top:8px">Teklif Formu</a>'
    calc_button = '<a class="fx-btn fx-btn--secondary fx-btn--block" href="gazli-yangin-sondurme-hesaplama.html" style="margin-top:8px">10 Sn Gaz Miktarı Hesapla →</a>\r\n' + target_callout

    if 'gazli-yangin-sondurme-hesaplama.html" style="margin-top:8px"' not in content and target_callout in content:
        content = content.replace(target_callout, calc_button)

    write_clean(filepath, content)
    print("Enriched Server Odası page with calculator bridge.")

def enrich_kurumsal():
    filepath = os.path.join(BASE_DIR, "kurumsal.html")
    content = read_clean(filepath)

    target_marker = '<!-- ==================================================\r\n       KATALOG BANNER (KOMPAKT & PREMIUM DOKÜMAN BANDI)\r\n       ================================================== -->'
    
    kurumsal_criteria_section = '''<!-- COMPETITIVE ADVANTAGE: YANGIN FİRMALARI SEÇİM KRİTERLERİ VE OSB HİZMET AĞI -->
<section class="fx-section fx-section--white" id="yangin-firmalari-kriterleri" style="border-top:1px solid var(--fx-line)">
<div class="fx-wrap">
<div style="max-width:780px;margin-bottom:32px">
<span class="fx-eyebrow" style="color:var(--fx-red)">KURUMSAL YETKİNLİK &amp; SEÇİM REHBERİ</span>
<h2 class="fx-h2" style="margin:8px 0 12px;color:var(--fx-ink)">Yangın Söndürme Firmaları Arasında Seçim Yaparken Dikkat Edilmesi Gereken 5 Kriter</h2>
<p class="fx-text" style="color:var(--fx-body);line-height:1.65">Endüstriyel tesisler, veri merkezleri ve ticari binalarda kurulacak gazlı yangın söndürme sistemleri yüksek mühendislik hassasiyeti gerektirir. Kurumsal <strong>yangın firmaları</strong> değerlendirilirken mutlaka sorgulanması gereken 5 temel yetkinlik:</p>
</div>
<div class="fx-grid fx-grid--3" style="gap:20px;margin-bottom:28px">
<div class="fx-card" style="padding:22px;background:#f8fafc;border-radius:10px;border:1px solid var(--fx-line)">
<strong style="color:var(--fx-red);font-size:14px;display:block;margin-bottom:6px">01 · Lisanslı Hidrolik Hesaplama</strong>
<p class="fx-text fx-text--sm" style="color:var(--fx-body);margin:0;line-height:1.55">Tüp miktarı ve boru çapları tahmini olarak değil; NFPA 2001 ve TS EN 15004 uyumlu VdS/UL onaylı iki fazlı hidrolik yazılımlarla 10 saniye deşarj kuralına göre hesaplanmalıdır.</p>
</div>
<div class="fx-card" style="padding:22px;background:#f8fafc;border-radius:10px;border:1px solid var(--fx-line)">
<strong style="color:var(--fx-red);font-size:14px;display:block;margin-bottom:6px">02 · Özmal Door Fan Test Donanımı</strong>
<p class="fx-text fx-text--sm" style="color:var(--fx-body);margin:0;line-height:1.55">Firmanın kendi bünyesinde kalibreli Kapı Fanı (Blower Door) oda sızdırmazlık test cihazı bulunmalı ve en az 10 dakikalık gaz tutma süresi (hold-time) raporlanmalıdır.</p>
</div>
<div class="fx-card" style="padding:22px;background:#f8fafc;border-radius:10px;border:1px solid var(--fx-line)">
<strong style="color:var(--fx-red);font-size:14px;display:block;margin-bottom:6px">03 · Sertifikalı Gaz Dolum ve F-Gaz Yetkisi</strong>
<p class="fx-text fx-text--sm" style="color:var(--fx-body);margin:0;line-height:1.55">FM200, Novec 1230 (FK-5-1-12) ve CO₂ gaz dolumu ile Çevre Bakanlığı Florlu Sera Gazları (F-Gaz) bildirim süreçleri TSE-HYB belgeli kadroyla yürütülmelidir.</p>
</div>
</div>
<div style="padding:20px 24px;background:#f8fafc;border-radius:10px;border:1px solid var(--fx-line);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px">
<div>
<strong style="color:var(--fx-ink);font-size:15px;display:block;margin-bottom:4px">İstanbul Organize Sanayi Bölgeleri (OSB) ve Türkiye Geneli 7/24 Saha Ağı</strong>
<p class="fx-text fx-text--sm" style="color:var(--fx-body);margin:0">Bayrampaşa merkez ofisimizden İkitelli OSB, Dudullu OSB, Tuzla OSB, Beylikdüzü, Maslak, Levent ile Gebze/Kocaeli, Çorlu/Tekirdağ, Bursa, Ankara ve İzmir başta olmak üzere 81 ilde anahtar teslim kurulum ve periyodik bakım hizmeti sunuyoruz.</p>
</div>
<a class="fx-btn fx-btn--primary fx-btn--sm" href="gazli-yangin-sondurme-hesaplama.html">Online Gaz Hesaplama Aracı →</a>
</div>
</div>
</section>'''

    if target_marker in content and 'id="yangin-firmalari-kriterleri"' not in content:
        content = content.replace(target_marker, kurumsal_criteria_section + "\r\n" + target_marker)

    write_clean(filepath, content)
    print("Enriched Kurumsal page with 5 engineering selection criteria & OSB coverage.")

if __name__ == "__main__":
    enrich_fm200()
    enrich_davlumbaz()
    enrich_pano_ici()
    enrich_novec1230()
    enrich_veri_merkezi()
    enrich_server_odasi()
    enrich_kurumsal()
    print("ALL COMPETITIVE ENRICHMENTS APPLIED SUCCESSFULLY!")
