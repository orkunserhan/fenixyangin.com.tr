import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            c = f.read()
        
        c = re.sub(r'Yildirim Mah\. Bugday Sok\.', 'Yıldırım Mah. Buğday Sok.', c)
        c = re.sub(r'Bayrampasa / Istanbul', 'Bayrampaşa / İstanbul', c)
        c = re.sub(r'Hacim hesaplayici', 'Hacim hesaplayıcı', c)
        c = re.sub(r'Basinda Biz', 'Basında Biz', c)
        c = re.sub(r'Arsiv, muze', 'Arşiv, müze', c)
        c = re.sub(r'Pano ici', 'Pano içi', c)
        c = re.sub(r'Sistem Yangin', 'Sistem Yangın', c)
        
        # Sadece index'in icindeki Iletisim'leri degistir, URL bozmamak icin ozel regex
        c = re.sub(r'>Iletisim<', '>İletişim<', c)
        c = re.sub(r'class="fx-footer__title">Iletisim<', 'class="fx-footer__title">İletişim<', c)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(c)
    except Exception as e:
        print(f"Error {file}: {e}")
