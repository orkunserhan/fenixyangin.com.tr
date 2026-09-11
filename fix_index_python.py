import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the absolute text in video cards
content = re.sub(r'<span class="fx-media__note".*?</span>', '', content)
content = content.replace('background:linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.8) 100%);', 'background:linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.8) 100%); pointer-events:none;')

# 2. Add red tint to Hero scrim and make it look clean
old_scrim = 'style="background:linear-gradient(97deg, var(--fx-paper) 0%, rgba(245,246,246,0.95) 44%, rgba(245,246,246,0.5) 74%, rgba(245,246,246,0) 100%);"'
new_scrim = 'style="background:linear-gradient(97deg, var(--fx-paper) 0%, rgba(245,246,246,0.95) 40%, rgba(220,38,38,0.05) 70%, rgba(220,38,38,0.1) 100%);"'
content = content.replace(old_scrim, new_scrim)

# 3. Fix Footer Legal text exactly
legal_pattern = r'<nav class="fx-footer__legal">.*?</nav>'
new_legal = '''<nav class="fx-footer__legal">
        <a href="#">KVKK Aydınlatma Metni</a><a href="#">Çerez Politikası</a><a href="#">Site Haritası</a>
      </nav>'''
content = re.sub(legal_pattern, new_legal, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

