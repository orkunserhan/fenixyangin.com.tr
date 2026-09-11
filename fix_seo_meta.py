import os
import re

data = {
    'fm200-gazli-yangin-sondurme-sistemleri.html': {
        'title': 'FM200 Gazlı Yangın Söndürme Sistemleri | Fenix Yangın',
        'desc': '10 saniyede yangını kaynağında boğan FM200 gazlı yangın söndürme sistemleri. Veri merkezleri ve elektrik odaları için kalıntısız, insan sağlığına zararsız çözüm.'
    },
    'novec-1230-gazli-yangin-sondurme-sistemleri.html': {
        'title': 'Novec 1230 Gazlı Yangın Söndürme Sistemleri | Fenix Yangın',
        'desc': 'Sıfır ozon delme potansiyeli ve maksimum insan güvenliği sunan Novec 1230 sistemleri. Müzeler, arşivler ve sunucu odaları için en temiz söndürme teknolojisi.'
    },
    'davlumbaz-yangin-sondurme-sistemleri.html': {
        'title': 'Endüstriyel Davlumbaz Yangın Söndürme Sistemleri | Fenix Yangın',
        'desc': 'Endüstriyel mutfaklar, restoranlar ve oteller için tam otomatik davlumbaz içi yangın söndürme sistemleri. Mutfak yangınlarına karşı kesin çözüm.'
    },
    'pano-ici-yangin-sondurme-sistemleri.html': {
        'title': 'Pano İçi Mikro Yangın Söndürme Sistemleri | Fenix Yangın',
        'desc': 'Elektrik panoları, sunucu kabinleri ve CNC tezgahları için borulu (polimer) mikro söndürme sistemleri. Yangını tam başladığı noktada bitirin.'
    },
    'server-odasi-yangin-sondurme.html': {
        'title': 'Sunucu ve Sistem Odası Yangın Söndürme | Fenix Yangın',
        'desc': 'Veri merkezleri ve sistem odaları için kalıntı bırakmayan, cihazlara zarar vermeyen FM200 ve Novec 1230 yangın güvenlik çözümleri.'
    },
    'aerosol-yangin-sondurme-sistemleri.html': {
        'title': 'Aerosol Yangın Söndürme Sistemleri | Fenix Yangın',
        'desc': 'Dar hacimler, telekom dolapları ve araç motorin kabinleri için borulama gerektirmeyen kompakt aerosol yangın söndürme sistemleri.'
    },
    'co2-gazli-yangin-sondurme-sistemleri.html': {
        'title': 'CO2 Karbondioksit Yangın Söndürme Sistemleri | Fenix Yangın',
        'desc': 'Büyük endüstriyel tesisler ve trafo odaları için ekonomik, güçlü ve kalıntısız CO2 gazlı yangın söndürme sistemleri.'
    },
    'lityum-batarya-yangin-sondurme-sistemleri.html': {
        'title': 'Lityum Batarya Yangın Söndürme Sistemleri | Fenix Yangın',
        'desc': 'Termal kaçak (thermal runaway) riskine karşı, erken algılama ve anında soğutma sağlayan lityum iyon batarya yangın güvenlik sistemleri.'
    },
    'trafo-odasi-yangin-sondurme.html': {
        'title': 'Trafo Odası Yangın Söndürme Sistemleri | Fenix Yangın',
        'desc': 'Yüksek gerilim trafoları ve jeneratör odaları için iletkenlik yaratmayan, kısa devre riskini sıfırlayan gazlı söndürme kalkanları.'
    },
    'arsiv-muze-yangin-sondurme.html': {
        'title': 'Arşiv ve Müze Yangın Söndürme Sistemleri | Fenix Yangın',
        'desc': 'Paha biçilemez evraklar ve tarihi eserler için su hasarı yaratmayan, iz bırakmayan VESDA destekli gazlı söndürme sistemleri.'
    },
    'fm200-gaz-dolumu.html': {
        'title': 'FM200 Gaz Dolumu ve Test İşlemleri | Fenix Yangın',
        'desc': 'Boşalan sistemleriniz için orijinal, %99.9 saflıkta UL/FM onaylı FM200 gaz dolumu. Aynı gün teslimat ve yerinde montaj güvencesi.'
    },
    'novec-1230-gaz-dolumu.html': {
        'title': 'Novec 1230 Gaz Dolumu | Fenix Yangın',
        'desc': 'Söndürme sonrası Novec 1230 silindirleriniz için uluslararası standartlarda hassas dolum, hidrostatik test ve yeniden devreye alma hizmeti.'
    },
    'fm200-gazli-yangin-sondurme-sistemleri-bakimi.html': {
        'title': 'FM200 Sistem Bakımı ve Periyodik Kontrol | Fenix Yangın',
        'desc': 'FM200 yangın söndürme sistemlerinizin sıvı seviye ölçümleri, valf testleri ve pano simülasyonlarını kapsayan detaylı periyodik bakımları.'
    },
    'novec-1230-gazli-yangin-sondurme-sistemleri-bakimi.html': {
        'title': 'Novec 1230 Bakım ve Sızdırmazlık Testi | Fenix Yangın',
        'desc': 'Novec 1230 sistemleri için hayati önem taşıyan periyodik bakım, door-fan sızdırmazlık testleri ve elektro-mekanik valf kontrolleri.'
    }
}

for filename, meta in data.items():
    filepath = os.path.join('pages', filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'<title>.*?</title>', f'<title>{meta["title"]}</title>', content, flags=re.DOTALL)
        content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{meta["desc"]}">', content, flags=re.DOTALL)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated metadata for {filename}")

