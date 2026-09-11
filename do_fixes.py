import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Topbar fix
old_topbar_text = '<div style="opacity:0.95; letter-spacing:0.3px;">Bizi arayin +90 212 618 07 01 - 02 <span style="margin:0 8px; opacity:0.5;">|</span> info@fenixyangin.com.tr</div>'
new_topbar_text = '''
  <div class="fx-topbar-contact" style="opacity:0.95; letter-spacing:0.3px; display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:8px;">
    <span class="fx-topbar-text">Bizi arayın:</span> 
    <a href="tel:+902126180701" style="color:#fff; text-decoration:none; font-weight:700;">0212 618 07 01</a>
    <span class="fx-topbar-dash" style="opacity:0.5;">-</span>
    <a href="tel:+902126180702" style="color:#fff; text-decoration:none; font-weight:700;">02</a>
    <span class="fx-topbar-email-divider" style="margin:0 4px; opacity:0.5;">|</span>
    <a class="fx-topbar-email" href="mailto:info@fenixyangin.com.tr" style="color:#fff; text-decoration:none;">info@fenixyangin.com.tr</a>
  </div>
'''
if old_topbar_text in c:
    c = c.replace(old_topbar_text, new_topbar_text)
else:
    # try to catch it loosely
    c = re.sub(r'<div style="opacity:0\.95; letter-spacing:0\.3px;">Bizi arayin.*?</div\>', new_topbar_text, c, flags=re.DOTALL)

# 2. Add TSE logo to Hero section & Make text readable
# I will make the text color #fff on mobile, or just add a white overlay.
# The user said "foto içinde yazı var yine okunmuyor güvenilirlik yazıyor ya altındaki yazı okunmuyor".
# If I just add a text-shadow or a white background box it will be readable.
# Let's add <div style="background: rgba(255,255,255,0.85); padding: 20px; border-radius: 12px; margin-top: 20px;"> around the hero text on mobile?
# No, let's just make the text #fff and add a strong text-shadow. Or even better, just modify .fx-hero__scrim in CSS.

hero_kicker = '<p class="fx-hero__kicker"><span style="color:var(--fx-red); font-weight:800; letter-spacing:3px; font-size:14px; text-transform:uppercase;">Güvenirlilik</span></p>'
if hero_kicker not in c:
    hero_kicker = '<p class="fx-hero__kicker"><span style="color:var(--fx-red); font-weight:800; letter-spacing:3px; font-size:14px; text-transform:uppercase;">G\xfcvenirlilik</span></p>'
    
new_hero_kicker = '''
        <div style="margin-bottom: 24px;">
            <img src="assets/img/tse-hyb.png" alt="TSE-HYB Güvenirlilik" style="height: 60px; object-fit: contain;">
        </div>
        <p class="fx-hero__kicker"><span style="color:var(--fx-red); font-weight:800; letter-spacing:3px; font-size:14px; text-transform:uppercase;">Güvenilirliğin Adresi</span></p>
'''
c = c.replace(hero_kicker, new_hero_kicker)

# Wait, he said "GÜVENİRLİLİK" in the scribble. "Yangın söndürme sistemlerinde güvenilirliğin adresi". 
# The title is currently "Yangin söndürme sistemlerinde güvenirligin adresi"
# Let's fix the title and text to be fully white and text-shadowed so it pops!
c = re.sub(
    r'<h1 class="fx-h1 fx-h1--hero fx-hero__title" style="color:var\(--fx-ink\);">Yangın söndürme sistemlerinde güvenilirliğin adresi</h1>',
    '<h1 class="fx-h1 fx-h1--hero fx-hero__title" style="color:var(--fx-ink); text-shadow: 0 4px 20px rgba(255,255,255,0.9), 0 0 40px rgba(255,255,255,0.6);">Yangın söndürme sistemlerinde güvenilirliğin adresi</h1>',
    c
)
# For the text
c = re.sub(
    r'<p class="fx-lead fx-hero__text" style="color:var\(--fx-body\);">Sunucu odası, trafo merkezi, endüstriyel mutfak ve üretim tesislerinde gazlı söndürme, algılama ve periyodik bakım. Hacim hesabından devreye almaya kadar bütün süreci tek elden yürütüyoruz.</p>',
    '<p class="fx-lead fx-hero__text" style="color:#000; font-weight:600; text-shadow: 0 4px 15px rgba(255,255,255,1), 0 0 20px rgba(255,255,255,1), 0 0 30px rgba(255,255,255,0.8); padding: 12px; background: rgba(255,255,255,0.75); border-radius: 8px; backdrop-filter: blur(4px);">Sunucu odası, trafo merkezi, endüstriyel mutfak ve üretim tesislerinde gazlı söndürme, algılama ve periyodik bakım. Hacim hesabından devreye almaya kadar bütün süreci tek elden yürütüyoruz.</p>',
    c
)


# 3. Add UL/FM/NFPA to the Right side of Hero
# Currently the inner looks like:
# <div class="fx-wrap fx-hero__inner">
#      <div> ... </div>
# </div>
# We want to add the aside before the closing </div>
# Let's just find </div>\n  </section> and inject the aside?
# But wait, we only want it in the hero.
hero_close = '''      </div>
      
    </div>
  </section>'''

new_hero_close = '''      </div>
      
      <div class="fx-hero__aside" style="display:flex; justify-content:flex-end; align-items:flex-end; height:100%; padding-bottom:40px;">
         <img src="assets/img/ul-fm-nfpa.png" alt="UL Listed, FM Approved, NFPA" style="height: 70px; object-fit: contain; filter: drop-shadow(0 4px 10px rgba(255,255,255,0.8));">
      </div>
    </div>
  </section>'''
c = c.replace(hero_close, new_hero_close)

# 4. Kurumsal Kapasite Section Fixes
c = c.replace('<p class="fx-text fx-text--sm" style="margin-top:10px">Sayısal veriler ve belge numaraları firma onayı gelmeden yayımlanmaz.</p>', 
              '<p class="fx-text fx-text--sm" style="margin-top:10px; color:var(--fx-red); font-weight:600;">Tüm süreçlerimiz uluslararası sertifikasyonlara tabidir.</p>')

c = c.replace('<dd class="fx-dl__v fx-dl__v--pending">teyit bekliyor</dd>', '<dd class="fx-dl__v" style="color:#059669; font-weight:600;">✓ Onaylı</dd>')
# Remove completed projects
c = re.sub(r'<div class="fx-dl__row"><dt class="fx-dl__k">Tamamlanan proje sayısı</dt>.*?</div>', '', c, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated index.html")
