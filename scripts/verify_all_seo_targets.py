import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r'C:\Users\orkun\.gemini\antigravity\scratch\fenix-static-final'

target_files = [
    'pages/fm200-gazli-yangin-sondurme-sistemleri.html',
    'pages/novec-1230-gazli-yangin-sondurme-sistemleri.html',
    'pages/davlumbaz-yangin-sondurme-sistemleri.html',
    'pages/pano-ici-yangin-sondurme-sistemleri.html',
    'pages/sistemler.html',
    'pages/kurumsal.html',
    'pages/iletisim.html',
    'pages/yangin-siniflari.html',
    'pages/aerosol-gazli-yangin-sondurme-sistemleri.html',
    'pages/veri-merkezi-yangin-sondurme.html',
    'pages/server-odasi-yangin-sondurme.html'
]

has_errors = False

for rel in target_files:
    fpath = os.path.join(base_dir, rel)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    title_m = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
    title = title_m.group(1).strip() if title_m else ''
    
    meta_tag_m = re.search(r'<meta\s+[^>]*name=["\']description["\'][^>]*>', html, re.I)
    meta_tag = meta_tag_m.group(0) if meta_tag_m else ''
    desc_m = re.search(r'content=["\'](.*?)["\']', meta_tag, re.I)
    desc = desc_m.group(1).strip() if desc_m else 'NO DESC'
    
    h1_m = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.I | re.S)
    h1_count = len(h1_m)
    h1_text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h1_m[0])).strip() if h1_count > 0 else 'NONE'
    
    wa_count = len(re.findall(r'href=["\']https://wa\.me/905327409097', html))
    
    print(f"FILE: {rel}")
    print(f"  Title ({len(title)} chars): {title}")
    if len(title) > 60:
        print(f"    WARNING: Title > 60 chars ({len(title)})")
        has_errors = True
    
    print(f"  Desc ({len(desc)} chars): {desc}")
    if len(desc) > 165:
        print(f"    WARNING: Description > 165 chars ({len(desc)})")
        has_errors = True
    
    print(f"  H1 count: {h1_count} | H1 text: {h1_text}")
    if h1_count != 1:
        print(f"    WARNING: H1 count is {h1_count} (expected 1)")
        has_errors = True
        
    print(f"  WhatsApp links found: {wa_count}")
    if wa_count < 2:
        print(f"    WARNING: Expected at least 2 WhatsApp links, found {wa_count}")
        has_errors = True
    
    print("-" * 50)

if has_errors:
    print("VERIFICATION FOUND WARNINGS / ERRORS!")
else:
    print("ALL 11 TARGET PAGES PASSED VERIFICATION WITH 0 ERRORS!")
