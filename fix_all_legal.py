import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

for file in html_files:
    if file == 'index.html': continue
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        legal_pattern = r'<nav class="fx-footer__legal">.*?</nav>'
        new_legal = '''<nav class="fx-footer__legal">
        <a href="#">KVKK Aydınlatma Metni</a><a href="#">Çerez Politikası</a><a href="#">Site Haritası</a>
      </nav>'''
        
        if re.search(legal_pattern, content, flags=re.DOTALL):
            content = re.sub(legal_pattern, new_legal, content, flags=re.DOTALL)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
    except Exception as e:
        print(f"Error {file}: {e}")
