import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r'C:\Users\orkun\.gemini\antigravity\scratch\fenix-static-final'
fpath = os.path.join(base_dir, 'pages/iletisim.html')

WA_SVG = '<svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.669-.699c.969.586 1.838.88 2.791.88 3.182 0 5.768-2.587 5.768-5.766.001-3.187-2.575-5.77-5.768-5.77zm3.385 8.163c-.144.405-.837.774-1.17.822-.311.045-.694.053-1.055-.065-.214-.07-.487-.163-.836-.317-1.464-.643-2.416-2.115-2.489-2.213-.072-.098-.596-.794-.596-1.52 0-.726.381-1.082.517-1.23.136-.148.297-.185.396-.185.099 0 .198.001.284.005.091.004.213-.035.333.254.125.3.428 1.045.466 1.121.038.077.063.167.013.267-.05.1-.075.162-.15.25-.075.088-.158.196-.226.263-.075.074-.153.155-.066.305.087.15.385.635.826 1.028.568.507 1.048.665 1.198.74.15.075.238.066.326-.036.088-.102.376-.437.476-.587.1-.15.2-.125.337-.075.137.05.867.409 1.016.484.15.075.25.112.287.175.037.062.037.362-.107.767z"/></svg>'

with open(fpath, 'r', encoding='utf-8') as f:
    c = f.read()

normalized = c.replace('\r\n', '\n')

old_block = '''<div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap">
<button class="fx-btn fx-btn--primary" id="teklif-submit-btn" style="background:#BE1523;color:#ffffff;font-weight:700;padding:12px 26px;border-radius:8px;border:none;cursor:pointer;" type="submit">Talebi Gönder</button>
<span class="fx-label" id="teklif-submit-info" style="font-size:12.5px;color:#64748b;">En geç 1 iş günü içinde yanıt verilir</span>
</div>'''

new_block = '''<div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap">
<button class="fx-btn fx-btn--primary" id="teklif-submit-btn" style="background:#BE1523;color:#ffffff;font-weight:700;padding:12px 26px;border-radius:8px;border:none;cursor:pointer;" type="submit">Talebi Gönder</button>
<span style="color:#94a3b8;font-size:13px;font-weight:600;">veya</span>
<a class="fx-btn fx-btn--wa" href="https://wa.me/905327409097?text=Merhaba,%20yang%C4%B1n%20s%C3%B6nd%C3%BCrme%20sistemleri%20projemiz%20i%C3%A7in%20bilgi%20ve%20h%C4%B1zl%C4%B1%20teklif%20almak%20istiyoruz." target="_blank" rel="noopener">''' + WA_SVG + '''WhatsApp ile Hızlı İletişim</a>
<span class="fx-label" id="teklif-submit-info" style="font-size:12.5px;color:#64748b;">En geç 1 iş günü içinde yanıt verilir</span>
</div>'''

assert old_block in normalized, 'old_block not found in iletisim.html'
normalized = normalized.replace(old_block, new_block, 1)

final_c = normalized.replace('\n', '\r\n')
with open(fpath, 'w', encoding='utf-8') as f:
    f.write(final_c)
print('Successfully updated iletisim.html with WhatsApp quote CTA!')
