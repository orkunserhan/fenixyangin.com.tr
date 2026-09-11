with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('X (Twitter)')
if idx != -1:
    print(content[idx:idx+400])
