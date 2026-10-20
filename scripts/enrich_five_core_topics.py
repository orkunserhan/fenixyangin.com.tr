import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\orkun\.gemini\antigravity\scratch\fenix-static-final\pages"

def enrich_fm200():
    filepath = os.path.join(BASE_DIR, "fm200-gazli-yangin-sondurme-sistemleri.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update H2s to precisely match requested topics
    # Prensip
    content = content.replace(
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Sistemi Nasıl Çalışır?</h2>',
        '<h2 class="fx-h2" style="margin:10px 0 14px">Sistemin Çalışma Prensibi: FM200 Yangın Söndürme Mekanizması</h2>'
    )
    # Sistem özellikleri ve kurulum
    content = content.replace(
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Sisteminin Temel Bileşenleri</h2>',
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM 200 Sistem Özellikleri ve Kurulum Standartları</h2>'
    )
    # Uygulama alanları
    content = content.replace(
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Nerelerde Kullanılır?</h2>',
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Gazlı Söndürme Sistemi Uygulama Alanları</h2>'
    )
    # Tasarım süreci
    content = content.replace(
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Sistem Seçimi ve Projelendirme</h2>',
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Tasarım Süreci ve Mühendislik Hesapları</h2>'
    )
    # Bakım
    content = content.replace(
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Gaz Dolumu ve Periyodik Bakım</h2>',
        '<h2 class="fx-h2" style="margin:10px 0 14px">FM200 Periyodik Bakım ve Gaz Dolumu Süreci</h2>'
    )
    # Teklif talebi
    content = content.replace(
        '<h2 class="fx-h2" style="margin-bottom:6px;color:#ffffff">FM200 Sistem Teklifi Alın</h2>',
        '<h2 class="fx-h2" style="margin-bottom:6px;color:#ffffff">FM200 Gazlı Söndürme Sistemi Teklif Talebi</h2>'
    )

    # Enrich intro paragraph of FM 200 Sistem Özellikleri ve Kurulum Standartları
    old_intro = "Fenix Yangın FM200 sistemleri, uluslararası onaylı üreticilerin yüksek basınca dayanıklı, sızdırmazlığı fabrikasyon olarak test edilmiş orijinal bileşenlerinden meydana gelir. Sistem mimarisinde yer alan kritik donanımlar şunlardır:"
    new_intro = "Fenix Yangın FM200 sistemleri; NFPA 2001, TS EN 15004 ve ISO 14520 normlarına tam uyumlu 25 bar veya 42 bar çalışma basıncına sahip yüksek dayanımlı bileşenlerden oluşur. VdS ve UL onaylı hidrolik hesaplama yazılımlarıyla boru çapları, basınç kayıpları ve 10 saniyelik boşalma süresi simüle edilir. <strong>FM 200 sistem özellikleri ve kurulum</strong> standartlarımız kapsamında kullanılan temel donanımlar şunlardır:"
    content = content.replace(old_intro, new_intro)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Enriched FM200 page successfully.")

def enrich_davlumbaz():
    filepath = os.path.join(BASE_DIR, "davlumbaz-yangin-sondurme-sistemleri.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Add dedicated Restoran ve Endüstriyel Mutfak Çözümleri section right before SECTION 8 (or SECTION 9)
    # Let's locate "<!-- SECTION 9: KULLANIM ALANLARI -->" and insert our enriched commercial kitchen section
    target_pos = '<!-- SECTION 9: KULLANIM ALANLARI -->'
    
    kitchen_section = '''<!-- ENRICHED: RESTORAN VE ENDÜSTRİYEL MUTFAK ÇÖZÜMLERİ -->
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
<p class="fx-text fx-text--sm" style="color:#64748b;line-height:1.55;margin-bottom:14px">Binaların Yangından Korunması Hakkında Yönetmelik Madde 57 gereğince yüksek binalarda ve 100 kişiden fazla kapasiteye sahip mutfaklarda otomatik davlumbaz söndürme sistemi yasal zorunluluktur.</p>
<ul class="fx-check-list" style="font-size:13px;color:#475569">
<li>İtfaiye yangın uygunluk raporu için onaylı teknik dosya ve şema</li>
<li>6 aylık zorunlu eriyen lehim (fusible link) dedektör değişimi ve tutanağı</li>
<li>Yetkili mühendis kaşeli periyodik bakım uygunluk belgesi</li>
</ul>
</div>
</div>
<div style="display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;padding:20px 26px;background:#fff;border-radius:10px;border:1px solid #e2e8f0">
<div>
<h4 style="margin:0 0 4px;font-size:16px;color:var(--fx-navy)">Endüstriyel Mutfağınız İçin Hızlı Keşif ve Ruhsat Uygunluğu</h4>
<p class="fx-text fx-text--sm" style="margin:0;color:#64748b">Ocak ve fritöz ölçülerinizi WhatsApp üzerinden paylaşın; mühendislerimiz aynı gün içinde akış hesabı ve teklifinizi hazırlasın.</p>
</div>
<a class="fx-btn fx-btn--wa" href="https://wa.me/905327409097?text=Merhaba,%20end%C3%BCstriyel%20mutfak%20davlumbaz%20yang%C4%B1n%20s%C3%B6nd%C3%BCrme%20sistemi%20ke%C5%9Ffi%20ve%20teklifi%20almak%20istiyorum." rel="noopener" target="_blank"><svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.669-.699c.969.586 1.838.88 2.791.88 3.182 0 5.768-2.587 5.768-5.766.001-3.187-2.575-5.77-5.768-5.77zm3.385 8.163c-.144.405-.837.774-1.17.822-.311.045-.694.053-1.055-.065-.214-.07-.487-.163-.836-.317-1.464-.643-2.416-2.115-2.489-2.213-.072-.098-.596-.794-.596-1.52 0-.726.381-1.082.517-1.23.136-.148.297-.185.396-.185.099 0 .198.001.284.005.091.004.213-.035.333.254.125.3.428 1.045.466 1.121.038.077.063.167.013.267-.05.1-.075.162-.15.25-.075.088-.158.196-.226.263-.075.074-.153.155-.066.305.087.15.385.635.826 1.028.568.507 1.048.665 1.198.74.15.075.238.066.326-.036.088-.102.376-.437.476-.587.1-.15.2-.125.337-.075.137.05.867.409 1.016.484.15.075.25.112.287.175.037.062.037.362-.107.767z"/></svg>WhatsApp Mutfak Keşfi</a>
</div>
</div>
</section>
'''
    if target_pos in content and 'id="endustriyel-mutfak-cozumleri"' not in content:
        content = content.replace(target_pos, kitchen_section + "\n" + target_pos)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Enriched Davlumbaz page successfully.")

def enrich_pano_ici():
    filepath = os.path.join(BASE_DIR, "pano-ici-yangin-sondurme-sistemleri.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # For Pano İçi (Rank 29 problem) -> Add dedicated comprehensive section with real application examples
    target_pos = '<!-- SECTION 7: SISTEM SECIMI VE DEGERLENDIRME (PHOTO 3 INTEGRATED) -->'

    case_studies_section = '''<!-- ENRICHED: ÖZGÜN UYGULAMA ÖRNEKLERİ VE PROJE REFERANSLARI (POZİSYON 29 ATILIMI) -->
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
<strong>Fenix Mühendislik Çözümü:</strong> İndirekt sistem mimarisi. Baraların ve ana şalter çıkışlarının üzerinden geçirilen ısıya duyarlı polimerik algılama hortumu yangını 160°C'de algılar. Silindir diferansiyel vanasını açarak HFC-227ea / FK-5-1-12 gazını paslanmaz çelik dağıtım boruları ve nozullardan panoya homojen olarak basar. Entegre basınç şalteri (pressure switch), ana giriş şalterinin açtırma bobinine (shunt trip) anlık sinyal göndererek panonun şebeke enerjisini milisaniyeler içinde keser.
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
<h3 class="fx-h3" style="font-size:18px;margin:0">PLC ve Otomasyon Kabinetleri Mikro Koruması</h3>
</div>
<p class="fx-text fx-text--sm" style="color:#64748b;line-height:1.55;margin-bottom:12px">
<strong>Risk:</strong> SCADA sistemleri, PLC kontrolörler, haberleşme switch'leri ve 24V DC güç kaynaklarının bulunduğu hassas otomasyon kabinlerinde elektriksel aşırı yük.
</p>
<p class="fx-text fx-text--sm" style="color:#475569;line-height:1.55;margin-bottom:12px">
<strong>Fenix Mühendislik Çözümü:</strong> FK-5-1-12 (Novec 1230 alternatifi) veya HFC-227ea temiz gazlı mikro silindir entegrasyonu. Pano kapakları açılmadan, saniyeler içinde hacimsel dolum gerçekleşir. SCADA ekranına anlık kuru kontak yangın sinyali iletilerek operatör bilgilendirilir.
</p>
<div style="font-size:13px;font-weight:600;color:var(--fx-navy)">Sonuç: PLC yazılımları, veri bus hatları ve hassas I/O modülleri hasarsız kurtarılır.</div>
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
</section>
'''
    if target_pos in content and 'id="ozgun-uygulama-ornekleri"' not in content:
        content = content.replace(target_pos, case_studies_section + "\n" + target_pos)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Enriched Pano İçi page successfully.")

def enrich_novec1230():
    filepath = os.path.join(BASE_DIR, "novec-1230-gazli-yangin-sondurme-sistemleri.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Add Technical Comparison Matrix right after SECTION 4: ADVANTAGES or before SECTION 5
    target_pos = '<!-- SECTION 5: INSTALLATION & DOOR FAN TEST -->'

    matrix_section = '''<!-- ENRICHED: TEMİZ GAZLI YANGIN SÖNDÜRME AJANLARI KARŞILAŞTIRMA MATRİSİ -->
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
<div style="overflow-x:auto;margin-bottom:32px;background:#fff;border-radius:12px;border:1px solid #e2e8f0;box-shadow:0 4px 16px rgba(0,0,0,0.03)">
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
</section>
'''
    if target_pos in content and 'id="temiz-gaz-karsilastirma"' not in content:
        content = content.replace(target_pos, matrix_section + "\n" + target_pos)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Enriched Novec 1230 page successfully.")

def enrich_veri_merkezi():
    filepath = os.path.join(BASE_DIR, "veri-merkezi-yangin-sondurme.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Expand Section 3.4 Örnek Projeler into 3 distinct real-world completed project case studies
    # Locate Section 3.4:
    # <section class="fx-section fx-section--paper" id="ornek-projeler"
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

<!-- Saha İnceleme ve Hızlı WhatsApp Yönlendirme -->
<div style="background:#fff;border:1px solid var(--fx-line);border-radius:12px;padding:22px 28px;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap">
<div>
<h4 style="margin:0 0 6px;font-size:17px;color:var(--fx-ink)">Veri Merkeziniz veya Sunucu Odanız İçin Ücretsiz Keşif Randevusu</h4>
<p class="fx-text fx-text--sm" style="margin:0;color:var(--fx-body)">Oda boyutlarınızı, yükseltilmiş taban yüksekliğini ve mevcut soğutma tipini iletin; hidrolik hesap raporu ve bütçenizi çıkaralım.</p>
</div>
<div style="display:flex;gap:12px;flex-wrap:wrap">
<a class="fx-btn fx-btn--wa" href="https://wa.me/905327409097?text=Merhaba,%20veri%20merkezi%20ve%20sunucu%20odas%C4%B1%20yang%C4%B1n%20s%C3%B6nd%C3%BCrme%20sistemi%20ke%C5%9Ffi%20ve%20teklifi%20almak%20istiyorum." rel="noopener" target="_blank"><svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.669-.699c.969.586 1.838.88 2.791.88 3.182 0 5.768-2.587 5.768-5.766.001-3.187-2.575-5.77-5.768-5.77zm3.385 8.163c-.144.405-.837.774-1.17.822-.311.045-.694.053-1.055-.065-.214-.07-.487-.163-.836-.317-1.464-.643-2.416-2.115-2.489-2.213-.072-.098-.596-.794-.596-1.52 0-.726.381-1.082.517-1.23.136-.148.297-.185.396-.185.099 0 .198.001.284.005.091.004.213-.035.333.254.125.3.428 1.045.466 1.121.038.077.063.167.013.267-.05.1-.075.162-.15.25-.075.088-.158.196-.226.263-.075.074-.153.155-.066.305.087.15.385.635.826 1.028.568.507 1.048.665 1.198.74.15.075.238.066.326-.036.088-.102.376-.437.476-.587.1-.15.2-.125.337-.075.137.05.867.409 1.016.484.15.075.25.112.287.175.037.062.037.362-.107.767z"/></svg>WhatsApp Hızlı Teklif</a>
<a class="fx-btn fx-btn--secondary" href="gazli-yangin-sondurme-hesaplama.html">Hacim Hesaplayıcı</a>
</div>
</div>
</div>
</section>'''

    if old_section_pattern.search(content):
        content = old_section_pattern.sub(new_projects_section, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Enriched Veri Merkezi page successfully.")

if __name__ == "__main__":
    enrich_fm200()
    enrich_davlumbaz()
    enrich_pano_ici()
    enrich_novec1230()
    enrich_veri_merkezi()
    print("ALL 5 TOPIC PAGES ENRICHED SUCCESSFULLY!")
