import re

with open('pages/projeler.html', 'r', encoding='utf-8') as f:
    content = f.read()

placeholders = re.findall(r'\[.*?\]', content)
with open('p_out.txt', 'w', encoding='utf-8') as out:
    for p in set(placeholders):
        out.write(p + '\n')
