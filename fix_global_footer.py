import os
import glob

html_files = glob.glob('**/*.html', recursive=True)

for file in html_files:
    if file == 'index.html': continue
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace('Sektrler', 'Sektörler')
        content = content.replace('Endstriyel', 'Endüstriyel')
        content = content.replace('mze', 'müze')
        content = content.replace('Pano ii', 'Pano içi')
        content = content.replace('Mhendislik', 'Mühendislik')
        content = content.replace('sndrme', 'söndürme')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        pass
