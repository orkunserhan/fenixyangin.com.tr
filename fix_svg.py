import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace corrupted SVG paths
content = content.replace('çözüm-1.161', 'zm-1.161')
content = content.replace('çözüm9.545', 'zm9.545')
content = content.replace('çözüm12', 'zm12')
content = content.replace('çözüm0', 'zm0')
content = content.replace('çözüm6.406', 'zm6.406')
content = content.replace('zm', 'zm') # Also check for U+FFFD versions!

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
