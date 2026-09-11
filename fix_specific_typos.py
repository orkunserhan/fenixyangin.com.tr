import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Safe replacements
content = content.replace('pages/Iletisim.html', 'pages/iletisim.html')
content = content.replace('Bizi arayin', 'Bizi arayın')
content = content.replace('>Iletisim<', '>İletişim<')
content = content.replace('>Iletisim', '>İletişim')

content = content.replace('Mhendislik', 'Mühendislik')
content = content.replace('sndrme', 'söndürme')
content = content.replace('Sektrler', 'Sektörler')
content = content.replace('Endstriyel', 'Endüstriyel')
content = content.replace('mze', 'müze')
content = content.replace('Pano ii', 'Pano içi')
content = content.replace('Tesisiniz iin dogru sistemi birlikte belirleyelim', 'Tesisiniz için doğru sistemi birlikte belirleyelim')

# Hero section typo:
content = content.replace('btn sreci', 'bütün süreci')
content = content.replace('yrtyoruz', 'yürütüyoruz')
content = content.replace('gvenirligin', 'güvenirliğin')
content = content.replace('gazli', 'gazlı')
content = content.replace('hesabindan devreye Almaya kadar', 'hesabından devreye almaya kadar')
content = content.replace('Sunucu odasi,', 'Sunucu odası,')

# Other
content = content.replace('lm ve tespit', 'Ölçüm ve tespit')
content = content.replace('Hacim llr', 'Hacim ölçülür')
content = content.replace('kaak', 'kaçak')
content = content.replace('Sistemi alisirken grn', 'Sistemi çalışırken görün')
content = content.replace('Mahal grlr', 'Mahal görülür')
content = content.replace('gerekesiyle nerilir', 'gerekçesiyle önerilir')
content = content.replace('Vaka alismalari', 'Vaka çalışmaları')
content = content.replace('ne ikan', 'Öne çıkan')
content = content.replace('alismasi rnegi', 'çalışması örneği')
content = content.replace('sresi', 'süresi')
content = content.replace('gsterilir', 'gösterilir')
content = content.replace('Trkiye', 'Türkiye')
content = content.replace('Sektrler  uygulama alanlari', 'Sektörler · uygulama alanları')
content = content.replace('dns', 'dönüşü')
content = content.replace('msait', 'müsait')
content = content.replace('szlesme', 'sözleşme')

# Yangin -> Yangın in titles
content = content.replace('Fenix Yangin', 'Fenix Yangın')
content = content.replace('Yangin s', 'Yangın s')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
