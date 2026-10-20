import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r'C:\Users\orkun\.gemini\antigravity\scratch\fenix-static-final'

WA_SVG = '<svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.669-.699c.969.586 1.838.88 2.791.88 3.182 0 5.768-2.587 5.768-5.766.001-3.187-2.575-5.77-5.768-5.77zm3.385 8.163c-.144.405-.837.774-1.17.822-.311.045-.694.053-1.055-.065-.214-.07-.487-.163-.836-.317-1.464-.643-2.416-2.115-2.489-2.213-.072-.098-.596-.794-.596-1.52 0-.726.381-1.082.517-1.23.136-.148.297-.185.396-.185.099 0 .198.001.284.005.091.004.213-.035.333.254.125.3.428 1.045.466 1.121.038.077.063.167.013.267-.05.1-.075.162-.15.25-.075.088-.158.196-.226.263-.075.074-.153.155-.066.305.087.15.385.635.826 1.028.568.507 1.048.665 1.198.74.15.075.238.066.326-.036.088-.102.376-.437.476-.587.1-.15.2-.125.337-.075.137.05.867.409 1.016.484.15.075.25.112.287.175.037.062.037.362-.107.767z"/></svg>'

def update_file(rel_path, replacements):
    fpath = os.path.join(base_dir, rel_path)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    normalized = content.replace('\r\n', '\n')
    
    for old, new in replacements:
        old_norm = old.replace('\r\n', '\n')
        new_norm = new.replace('\r\n', '\n')
        if old_norm not in normalized:
            print(f"ERROR: Target block not found in {rel_path}!")
            print("Target was:\n" + old_norm[:160] + "...")
            return False
        normalized = normalized.replace(old_norm, new_norm, 1)
    
    final_content = normalized.replace('\n', '\r\n')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"SUCCESS: {rel_path} updated.")
    return True

# ==========================================
# 3. Davlumbaz Yangin Sondurme
# ==========================================
davlumbaz_reps = [
    (
        '<meta content="Endüstriyel mutfak ve davlumbazlar için otomatik yangın söndürme sistemleri. UL 300 kriterleri, çalışma prensibi, bakım ve projelendirme detayları." name="description"/>',
        '<meta content="Davlumbaz yangın söndürme sistemi. Restoran, otel ve endüstriyel mutfaklar için BYKHY Madde 57 uyumlu itfaiye onaylı montaj, periyodik bakım ve WhatsApp teklifi." name="description"/>'
    ),
    (
        '''<div class="fx-sys-hero__actions">
<a class="fx-btn fx-btn--primary" href="iletisim.html">Projeniz İçin Teklif Alın</a>
<a class="fx-btn fx-btn--ghost-dark" href="yangin-danismanligi.html">Mühendislik Danışmanlığı</a>
</div>''',
        '''<div class="fx-sys-hero__actions">
<a class="fx-btn fx-btn--primary" href="iletisim.html">Projeniz İçin Teklif Alın</a>
<a class="fx-btn fx-btn--wa" href="https://wa.me/905327409097?text=Merhaba,%20davlumbaz%20yang%C4%B1n%20s%C3%B6nd%C3%BCrme%20sistemi%20i%C3%A7in%20itfaiye%20uygunluk%20ve%20fiyat%20teklifi%20almak%20istiyorum." rel="noopener" target="_blank">''' + WA_SVG + '''WhatsApp Hızlı Teklif</a>
<a class="fx-btn fx-btn--ghost-dark" href="yangin-danismanligi.html">Mühendislik Danışmanlığı</a>
</div>'''
    ),
    (
        '''<div style="display:flex;gap:12px;flex-wrap:wrap">
<div class="fx-cta-phones fx-desktop-only" style="display:flex;gap:12px;flex-wrap:wrap;"><a class="fx-btn fx-btn--white" href="tel:+902126180701">+90 212 618 07 01</a> <a class="fx-btn fx-btn--white" href="tel:+902126180702">+90 212 618 07 02</a></div>
<a class="fx-btn fx-btn--ghost-dark" href="iletisim.html">Teklif Formu</a>
</div>''',
        '''<div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;">
<a class="fx-btn fx-btn--wa" href="https://wa.me/905327409097?text=Merhaba,%20davlumbaz%20yang%C4%B1n%20s%C3%B6nd%C3%BCrme%20sistemi%20i%C3%A7in%20fiyat%20ve%20itfaiye%20onay%20raporu%20teklifi%20almak%20istiyorum." rel="noopener" target="_blank">''' + WA_SVG + '''WhatsApp İle Teklif Alın</a>
<div class="fx-cta-phones fx-desktop-only" style="display:flex;gap:12px;flex-wrap:wrap;"><a class="fx-btn fx-btn--white" href="tel:+902126180701">+90 212 618 07 01</a></div>
<a class="fx-btn fx-btn--ghost-dark" href="iletisim.html">Teklif Formu</a>
</div>'''
    )
]

# ==========================================
# 4. Pano Ici Yangin Sondurme
# ==========================================
pano_reps = [
    (
        '<meta content="Elektrik panoları, MCC ve otomasyon kabinleri için mikro hacim otomatik gazlı yangın söndürme sistemleri. Doğrudan ve dolaylı tubing koruma çözümleri." name="description"/>',
        '<meta content="Pano içi yangın söndürme sistemi. Elektrik panoları, MCC ve kompanzasyon için direkt/indirekt tubing mikro söndürme, devreye alma ve anında WhatsApp teklifi." name="description"/>'
    ),
    (
        '''<div class="fx-sys-hero__actions">
<a class="fx-btn fx-btn--primary" href="iletisim.html">Teklif Alın</a>
<a class="fx-btn fx-btn--ghost-dark" href="yangin-danismanligi.html">Mühendislik Danışmanlığı</a>
</div>''',
        '''<div class="fx-sys-hero__actions">
<a class="fx-btn fx-btn--primary" href="iletisim.html">Teklif Alın</a>
<a class="fx-btn fx-btn--wa" href="https://wa.me/905327409097?text=Merhaba,%20pano%20i%C3%A7i%20yang%C4%B1n%20s%C3%B6nd%C3%BCrme%20sistemi%20i%C3%A7in%20fiyat%20ve%20ke%C5%9Fif%20almak%20istiyorum." rel="noopener" target="_blank">''' + WA_SVG + '''WhatsApp Hızlı Teklif</a>
<a class="fx-btn fx-btn--ghost-dark" href="yangin-danismanligi.html">Mühendislik Danışmanlığı</a>
</div>'''
    ),
    (
        '''<div style="display:flex;gap:12px;flex-wrap:wrap">
<div class="fx-cta-phones fx-desktop-only" style="display:flex;gap:12px;flex-wrap:wrap;"><a class="fx-btn fx-btn--white" href="tel:+902126180701">+90 212 618 07 01</a> <a class="fx-btn fx-btn--white" href="tel:+902126180702">+90 212 618 07 02</a></div>
<a class="fx-btn fx-btn--ghost-dark" href="iletisim.html">Teklif Formu</a>
</div>''',
        '''<div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;">
<a class="fx-btn fx-btn--wa" href="https://wa.me/905327409097?text=Merhaba,%20pano%20i%C3%A7i%20gazl%C4%B1%20s%C3%B6nd%C3%BCrme%20sistemi%20i%C3%A7in%20teklif%20almak%20istiyorum." rel="noopener" target="_blank">''' + WA_SVG + '''WhatsApp Hızlı Teklif</a>
<div class="fx-cta-phones fx-desktop-only" style="display:flex;gap:12px;flex-wrap:wrap;"><a class="fx-btn fx-btn--white" href="tel:+902126180701">+90 212 618 07 01</a></div>
<a class="fx-btn fx-btn--ghost-dark" href="iletisim.html">Teklif Formu</a>
</div>'''
    )
]

# ==========================================
# 7. Yangin Siniflari
# ==========================================
yangin_siniflari_reps = [
    (
        '<meta content="TS EN 2 standartlarına göre A, B, C, D, F yangın sınıfları, yakıt özellikleri, elektrik yangını riskleri ve doğru yangın söndürücü ajan seçimi rehberi." name="description"/>',
        '<meta content="Yangın sınıfları nelerdir? TS EN 2 standardına göre A, B, C, D ve F sınıfı yangınlar, doğru yangın söndürücü seçimi ve WhatsApp mühendislik desteği." name="description"/>'
    ),
    (
        '''<a class="fx-btn fx-btn--primary fx-btn--sm" href="iletisim.html" style="width:100%;text-align:center;">İletişim Sayfası</a>''',
        '''<a class="fx-btn fx-btn--primary fx-btn--sm" href="iletisim.html" style="width:100%;text-align:center;">İletişim Sayfası</a>
<a class="fx-btn fx-btn--wa fx-btn--sm" href="https://wa.me/905327409097?text=Merhaba,%20yang%C4%B1n%20s%C4%B1n%C4%B1flar%C4%B1%20ve%20s%C3%B6nd%C3%BCr%C3%BCc%C3%BC%20sistem%20se%C3%A7imi%20i%C3%A7in%20bilgi%20ve%20teklif%20almak%20istiyorum." target="_blank" rel="noopener" style="width:100%;text-align:center;justify-content:center;margin-top:8px;">''' + WA_SVG + '''WhatsApp Mühendislik Hattı</a>'''
    )
]

# ==========================================
# 8. Aerosol Gazli Yangin Sondurme
# ==========================================
aerosol_reps = [
    (
        '<meta content="Aerosol gazlı yangın söndürme sistemleri; endüstriyel tesisler ve teknik hacimler için kompakt söndürme çözümleri sunar. Detaylı bilgi ve teklif alın." name="description"/>',
        '<meta content="Aerosol yangın söndürme sistemleri. NFPA 2010 standartlarında borusuz kondanse aerosol jeneratörleri, trafo, pano ve rüzgar türbini koruması, WhatsApp teklifi." name="description"/>'
    ),
    (
        '''<div class="fx-sys-hero__actions">
<a class="fx-btn fx-btn--primary" href="iletisim.html">Teklif Alın</a>
<a class="fx-btn fx-btn--ghost-dark" href="yangin-danismanligi.html">Mühendislik Danışmanlığı</a>
</div>''',
        '''<div class="fx-sys-hero__actions">
<a class="fx-btn fx-btn--primary" href="iletisim.html">Teklif Alın</a>
<a class="fx-btn fx-btn--wa" href="https://wa.me/905327409097?text=Merhaba,%20aerosol%20yang%C4%B1n%20s%C3%B6nd%C3%BCrme%20sistemi%20i%C3%A7in%20teklif%20ve%20ke%C5%9Fif%20almak%20istiyorum." rel="noopener" target="_blank">''' + WA_SVG + '''WhatsApp Hızlı Teklif</a>
<a class="fx-btn fx-btn--ghost-dark" href="yangin-danismanligi.html">Mühendislik Danışmanlığı</a>
</div>'''
    ),
    (
        '''<div style="display:flex;gap:12px;flex-wrap:wrap">
<div class="fx-cta-phones fx-desktop-only" style="display:flex;gap:12px;flex-wrap:wrap;"><a class="fx-btn fx-btn--white" href="tel:+902126180701">+90 212 618 07 01</a> <a class="fx-btn fx-btn--white" href="tel:+902126180702">+90 212 618 07 02</a></div>
<a class="fx-btn fx-btn--ghost-dark" href="iletisim.html">Teklif Formu</a>
</div>''',
        '''<div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;">
<a class="fx-btn fx-btn--wa" href="https://wa.me/905327409097?text=Merhaba,%20aerosol%20yang%C4%B1n%20s%C3%B6nd%C3%BCrme%20sistemi%20i%C3%A7in%20fiyat%20ve%20ke%C5%9Fif%20teklifi%20almak%20istiyorum." rel="noopener" target="_blank">''' + WA_SVG + '''WhatsApp Hızlı Teklif</a>
<div class="fx-cta-phones fx-desktop-only" style="display:flex;gap:12px;flex-wrap:wrap;"><a class="fx-btn fx-btn--white" href="tel:+902126180701">+90 212 618 07 01</a></div>
<a class="fx-btn fx-btn--ghost-dark" href="iletisim.html">Teklif Formu</a>
</div>'''
    )
]

# ==========================================
# 9. Veri Merkezi Yangin Sondurme
# ==========================================
veri_merkezi_reps = [
    (
        '''<div style="display:flex;gap:12px;flex-wrap:wrap">
<div class="fx-cta-phones fx-desktop-only" style="display:flex;gap:12px;flex-wrap:wrap;">
<a class="fx-btn fx-btn--white" href="tel:+902126180701">+90 212 618 07 01</a>
<a class="fx-btn fx-btn--white" href="tel:+902126180702">+90 212 618 07 02</a>
</div>
<a class="fx-btn fx-btn--ghost-dark" href="iletisim.html">İletişime Geç →</a>
</div>''',
        '''<div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;">
<a class="fx-btn fx-btn--wa" href="https://wa.me/905327409097?text=Merhaba,%20veri%20merkezi%20ve%20server%20odas%C4%B1%20gazl%C4%B1%20s%C3%B6nd%C3%BCrme%20projesi%20i%C3%A7in%20teklif%20almak%20istiyoruz." target="_blank" rel="noopener">''' + WA_SVG + '''WhatsApp Hızlı Teklif</a>
<div class="fx-cta-phones fx-desktop-only" style="display:flex;gap:12px;flex-wrap:wrap;">
<a class="fx-btn fx-btn--white" href="tel:+902126180701">+90 212 618 07 01</a>
</div>
<a class="fx-btn fx-btn--ghost-dark" href="iletisim.html">İletişime Geç →</a>
</div>'''
    )
]

remaining_tasks = [
    ('pages/davlumbaz-yangin-sondurme-sistemleri.html', davlumbaz_reps),
    ('pages/pano-ici-yangin-sondurme-sistemleri.html', pano_reps),
    ('pages/yangin-siniflari.html', yangin_siniflari_reps),
    ('pages/aerosol-gazli-yangin-sondurme-sistemleri.html', aerosol_reps),
    ('pages/veri-merkezi-yangin-sondurme.html', veri_merkezi_reps)
]

all_success = True
for rel_path, reps in remaining_tasks:
    res = update_file(rel_path, reps)
    if not res:
        all_success = False

print("\n--- REMAINING STATUS ---")
if all_success:
    print("ALL REMAINING TARGET FILES UPDATED SUCCESSFULLY!")
else:
    print("CHECK REMAINING ISSUES ABOVE.")
