import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'<div style="margin-bottom: 24px;">\s*<img src="assets/img/tse-hyb.png" alt="TSE-HYB Güvenilirliğin Adresi" class="fx-hero__logo-tse">\s*</div>', '<div class="fx-mobile-only" style="margin-bottom: 24px;">\n            <img src="assets/img/tse-hyb.png" alt="TSE-HYB Güvenilirliğin Adresi" class="fx-hero__logo-tse">\n        </div>', c)

aside_pattern = r'<div class="fx-hero__aside".*?</div>'
new_aside = '''<div class="fx-hero__aside">
         <img src="assets/img/tse-hyb.png" alt="TSE-HYB Güvenilirliğin Adresi" class="fx-hero__logo-tse fx-desktop-only">
         <img src="assets/img/ul-fm-nfpa.png" alt="UL Listed, FM Approved, NFPA" class="fx-hero__logo-certs">
      </div>'''

c = re.sub(aside_pattern, new_aside, c, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
