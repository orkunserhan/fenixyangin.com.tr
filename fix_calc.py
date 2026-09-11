import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Hacim hesaplayıcı to include the note
calc_title = '<h2 class="fx-h2" style="margin:14px 0">Hacim hesaplayıcı</h2>'
new_calc_title = '<h2 class="fx-h2" style="margin:14px 0">Hacim hesaplayıcı</h2>\n        <p class="fx-text fx-text--sm" style="color:var(--fx-red); font-weight:600; margin-bottom:14px;">*FM200 HESAPLAMASIDIR</p>'

content = content.replace(calc_title, new_calc_title)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
