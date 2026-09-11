import re

with open('css/fenix-design.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace Desktop Logos CSS to be completely transparent
css = re.sub(r'\.fx-hero__logo-tse, \.fx-hero__logo-certs \{[\s\S]*?\}', 
'''\.fx-hero__logo-tse, .fx-hero__logo-certs {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  backdrop-filter: none !important;
  mix-blend-mode: normal !important;
  display: block;
}''', css)

# Replace Mobile Logos CSS to remove multiply
css = re.sub(r'mix-blend-mode: multiply !important;', 'mix-blend-mode: normal !important;', css)

with open('css/fenix-design.css', 'w', encoding='utf-8') as f:
    f.write(css)
