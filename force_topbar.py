import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

new_topbar = '''<div class="fx-topbar-contact" style="opacity:0.95; letter-spacing:0.3px; display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:8px;">
    <span class="fx-topbar-text">Bizi arayın:</span> 
    <a href="tel:+902126180701" style="color:#fff; text-decoration:none; font-weight:700;">0212 618 07 01</a>
    <span class="fx-topbar-dash" style="opacity:0.5;">-</span>
    <a href="tel:+902126180702" style="color:#fff; text-decoration:none; font-weight:700;" class="fx-topbar-tel2">0212 618 07 02</a>
    <span class="fx-topbar-email-divider" style="margin:0 4px; opacity:0.5;">|</span>
    <a class="fx-topbar-email" href="mailto:info@fenixyangin.com.tr" style="color:#fff; text-decoration:none;">info@fenixyangin.com.tr</a>
</div>'''

c = re.sub(r'<div style="opacity:0\.95; letter-spacing:0\.3px;">Bizi arayin.*?</div>', new_topbar, c, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
