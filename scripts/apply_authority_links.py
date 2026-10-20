import os

# 1. Davlumbaz
p_dav = os.path.join(r'C:\Users\orkun\.gemini\antigravity\scratch\fenix-static-final', 'pages', 'davlumbaz-yangin-sondurme-sistemleri.html')
with open(p_dav, 'rb') as f:
    raw = f.read()

target1 = 'Davlumbaz yangın söndürme sistemi. Restoran, otel ve endüstriyel mutfaklar için BYKHY Madde 57 uyumlu itfaiye onaylı montaj, periyodik bakım ve WhatsApp teklifi.'.encode('utf-8')
repl1 = 'Davlumbaz yangın söndürme sistemi. Restoran, otel ve endüstriyel mutfaklar için BYKHY Madde 57 ve itfaiye onaylı montaj, periyodik bakım ve WhatsApp teklifi.'.encode('utf-8')

if target1 in raw:
    raw = raw.replace(target1, repl1)
    with open(p_dav, 'wb') as f:
        f.write(raw)
    print('Davlumbaz updated binary!')
else:
    print('Davlumbaz already updated.')

# 2. Gazli Hesaplama
p_calc = os.path.join(r'C:\Users\orkun\.gemini\antigravity\scratch\fenix-static-final', 'pages', 'gazli-yangin-sondurme-hesaplama.html')
with open(p_calc, 'rb') as f:
    raw = f.read()

target2 = 'Gazın odada 10 dakika kalabildiği akredite Door Fan testiyle kanıtlanır.'.encode('utf-8')
url2 = 'https://www.fenixyangin.com/teknik-icerikler/gazli-sondurme-ajan-miktari-hesabi/'.encode('utf-8')
if target2 in raw and url2 not in raw:
    repl2 = target2 + ' Ayrıntılı formül ve mühendislik şartnamesi için <a href="https://www.fenixyangin.com/teknik-icerikler/gazli-sondurme-ajan-miktari-hesabi/" target="_blank" rel="noopener noreferrer" style="color:var(--fx-red);font-weight:600;text-decoration:underline">NFPA 2001 Gazlı Söndürme Ajan Miktarı Hesabı</a> rehberini inceleyebilirsiniz.'.encode('utf-8')
    raw = raw.replace(target2, repl2, 1)
    with open(p_calc, 'wb') as f:
        f.write(raw)
    print('Hesaplama updated binary!')
else:
    print('Hesaplama already has cross-link.')

# 3. FM200
p_fm = os.path.join(r'C:\Users\orkun\.gemini\antigravity\scratch\fenix-static-final', 'pages', 'fm200-gazli-yangin-sondurme-sistemleri.html')
with open(p_fm, 'rb') as f:
    raw = f.read()

url3 = 'https://www.fenixyangin.com/fm-200-gazli-sondurme-sistemleri-teknik-sartnamesi/'.encode('utf-8')
if url3 not in raw:
    needle = 'Küresel Düzenleyici Teknik Not'.encode('utf-8')
    idx = raw.find(needle)
    if idx != -1:
        sec_end = raw.find(b'</section>', idx)
        div_end = raw.rfind(b'</div>', idx, sec_end)
        
        # detect line ending in this region
        nl = b'\r\r\n' if b'\r\r\n' in raw[idx:sec_end] else (b'\r\n' if b'\r\n' in raw[idx:sec_end] else b'\n')
        
        banner_text = (
            '\n'
            '<div style="margin-top:20px;padding:16px 20px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px">\n'
            '<div style="max-width:580px">\n'
            '<strong style="color:#0f172a;font-size:15px;display:block;margin-bottom:4px">Teknik Şartname &amp; İhale Kriterleri</strong>\n'
            '<p style="color:#64748b;font-size:13.5px;line-height:1.5;margin:0">NFPA 2001 ve ISO 14520 standartlarına uygun mimari ve mekanik ihale şartnamesi maddelerini mühendislik merkezimizden inceleyin.</p>\n'
            '</div>\n'
            '<a class="fx-btn fx-btn--outline" href="https://www.fenixyangin.com/fm-200-gazli-sondurme-sistemleri-teknik-sartnamesi/" rel="noopener noreferrer" style="padding:10px 18px;font-size:13.5px;white-space:nowrap" target="_blank">Teknik Şartnameyi İncele &rarr;</a>\n'
            '</div>'
        ).replace('\n', nl.decode('latin1')).encode('utf-8')
        
        raw = raw[:div_end + 6] + banner_text + raw[div_end + 6:]
        with open(p_fm, 'wb') as f:
            f.write(raw)
        print('FM200 updated binary!')
else:
    print('FM200 already has cross-link.')
