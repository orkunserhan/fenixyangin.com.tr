with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
    if 'Yıldırım' in c:
        print('SUCCESS: Yıldırım found')
