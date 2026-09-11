import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the entire nav block inside footer
        new_nav = '''<nav class="fx-footer__legal">
        <a href="#">KVKK Aydınlatma Metni</a><a href="#">Çerez Politikası</a><a href="#">Site Haritası</a>
      </nav>'''
        
        content = re.sub(r'<nav class="fx-footer__legal">.*?</nav>', new_nav, content, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"Error {file}: {e}")
