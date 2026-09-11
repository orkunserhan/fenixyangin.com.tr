import os
import glob
import re

html_files = glob.glob('pages/*.html')

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        basename = os.path.basename(file)
        name_no_ext = basename.replace('.html', '').replace('-', ' ').title()
        
        # Generic Placeholders
        content = content.replace('[breadcrumb]', f'Ana Sayfa › {name_no_ext}')
        content = content.replace('[arşiv başlığı]', f'{name_no_ext}')
        content = content.replace('[arşiv açıklaması]', 'Fenix Yangın kurumsal bilgi merkezi ve sektör detayları.')
        content = content.replace('[empty metni]', 'İçeriklerimiz güncelleniyor. Çok yakında yeni projelerimiz ve makalelerimizle karşınızda olacağız.')
        content = content.replace('[post count]', '12')
        content = content.replace('[found posts]', '12')
        content = content.replace('[sektor term]', 'Veri Merkezi')
        content = content.replace('[sistem term]', 'FM200')
        content = content.replace('[proje yil]', '2024')
        content = content.replace('[paged bilgisi]', 'Sayfa 1 / 1')
        content = content.replace('[the title]', 'Fenix Genel Kılavuz')
        content = content.replace('[grup adı]', 'Rehber')
        content = content.replace('[grup sayısı]', '4')
        content = content.replace('[yazı tipi]', 'Makale')
        content = content.replace('[blog cta metin]', 'Uzman mühendislerimiz, projenize en uygun sistemi tasarlamak için 7/24 hizmetinizde. Hemen ulaşın.')
        content = content.replace('[adres verisi]', 'Muratpaşa Mah. Kâmil Cad. No:64/A Bayrampaşa / İstanbul')
        content = content.replace('[proje hacim]', '450 m3')
        content = content.replace('[sistem]', 'FM200 Söndürme Sistemi')
        content = content.replace('[sektor]', 'Endüstriyel Tesis')

        # Partials
        cagri_partial = '''
        <div style="display:flex; flex-direction:column; align-items:center; text-align:center; padding:40px 20px; color:#fff;">
            <h2 class="fx-h2" style="margin-bottom:16px;">Projeleriniz için uzman desteği alın</h2>
            <p style="margin-bottom:24px; opacity:0.9;">Tesisinizin risk analizini yapalım, en doğru sistemi birlikte belirleyelim.</p>
            <a href="iletisim.html" class="fx-btn fx-btn--on-red">7/24 Bize Ulaşın</a>
        </div>
        '''
        
        proje_kart_partial = '''
        <a href="proje-single.html" class="fx-card">
            <div class="fx-media fx-media--4x3" style="background:#14181B; border-radius:12px; margin-bottom:16px;"></div>
            <h3 class="fx-h3">Global Veri Merkezi FM200 Projesi</h3>
            <p class="fx-text fx-text--sm" style="color:var(--fx-muted); margin-top:8px;">2024 • İstanbul</p>
        </a>
        <a href="proje-single.html" class="fx-card">
            <div class="fx-media fx-media--4x3" style="background:#14181B; border-radius:12px; margin-bottom:16px;"></div>
            <h3 class="fx-h3">Arşiv Odası Novec 1230 Kurulumu</h3>
            <p class="fx-text fx-text--sm" style="color:var(--fx-muted); margin-top:8px;">2023 • Ankara</p>
        </a>
        <a href="proje-single.html" class="fx-card">
            <div class="fx-media fx-media--4x3" style="background:#14181B; border-radius:12px; margin-bottom:16px;"></div>
            <h3 class="fx-h3">Otel Mutfak Davlumbaz Söndürme</h3>
            <p class="fx-text fx-text--sm" style="color:var(--fx-muted); margin-top:8px;">2024 • Antalya</p>
        </a>
        '''

        proje_one_cikan = '''
        <div class="fx-wrap" style="padding:40px 0;">
            <div class="fx-grid fx-grid--2">
                <div class="fx-media fx-media--16x9" style="background:#14181B; border-radius:16px;"></div>
                <div style="display:flex; flex-direction:column; justify-content:center;">
                    <span class="fx-badge fx-badge--red" style="align-self:flex-start; margin-bottom:16px;">Öne Çıkan Proje</span>
                    <h2 class="fx-h2">Uluslararası Telekomünikasyon Veri Merkezi</h2>
                    <p class="fx-text" style="margin:16px 0 24px; color:var(--fx-body);">Türkiye'nin en büyük telekomünikasyon altyapılarından birinin 15 farklı lokasyonunda, Novec 1230 gazlı söndürme sistemleri anahtar teslim projelendirildi.</p>
                    <a href="proje-single.html" class="fx-link-arrow">Proje detaylarını incele &#8594;</a>
                </div>
            </div>
        </div>
        '''

        content = content.replace('[PARTIAL: cagri]', cagri_partial)
        content = content.replace('[PARTIAL: proje-kart]', proje_kart_partial)
        content = content.replace('[PARTIAL: proje-serit]', proje_kart_partial)
        content = content.replace('[PARTIAL: proje-one-cikan]', proje_one_cikan)

        # FOTOĞRAF SLOTU removal
        content = re.sub(r'FOTOĞRAF SLOTU.*?sonra', '', content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except Exception as e:
        print(f"Error {file}: {e}")
