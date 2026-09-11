import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('olc.txt', 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines):
        for word in re.findall(r'\b\w*Ölçüm\w*\b', line, re.IGNORECASE):
            out.write(f"Line {i+1}: {word}\n")
