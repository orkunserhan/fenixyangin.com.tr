import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Topbar fix for mobile
# Currently:
# <div style="opacity:0.95; letter-spacing:0.3px;">Bizi arayin +90 212 618 07 01 - 02 <span style="margin:0 8px; opacity:0.5;">|</span> info@fenixyangin.com.tr</div>
# We want to change this so on mobile it shows ONLY numbers, big and clickable, and on desktop it shows both nicely.
old_topbar_text = '<div style="opacity:0.95; letter-spacing:0.3px;">Bizi arayin +90 212 618 07 01 - 02 <span style="margin:0 8px; opacity:0.5;">|</span> info@fenixyangin.com.tr</div>'

new_topbar_text = '''
  <div class="fx-topbar-contact" style="opacity:0.95; letter-spacing:0.3px; display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:8px;">
    <span class="fx-topbar-text">Bizi arayın:</span> 
    <a href="tel:+902126180701" style="color:#fff; text-decoration:none; font-weight:700;">0212 618 07 01</a>
    <span style="opacity:0.5;">-</span>
    <a href="tel:+902126180702" style="color:#fff; text-decoration:none; font-weight:700;">02</a>
    <span class="fx-topbar-email-divider" style="margin:0 4px; opacity:0.5;">|</span>
    <a class="fx-topbar-email" href="mailto:info@fenixyangin.com.tr" style="color:#fff; text-decoration:none;">info@fenixyangin.com.tr</a>
  </div>
'''
c = c.replace(old_topbar_text, new_topbar_text)

# Also need to inject CSS for this so it hides email on mobile:
style_inject = '''
<style>
@media (max-width: 760px) {
  .fx-topbar-email, .fx-topbar-email-divider { display: none !important; }
  .fx-topbar-contact { flex-direction: row; gap: 6px; font-size: 15px; }
}
</style>
</head>
'''
c = c.replace('</head>', style_inject)

# 2. Add TSE logo to Hero section
hero_kicker = '<p class="fx-hero__kicker"><span style="color:var(--fx-red); font-weight:800; letter-spacing:3px; font-size:14px; text-transform:uppercase;">Güvenirlilik</span></p>'
new_hero_kicker = '''
        <div style="margin-bottom: 16px;">
            <img src="assets/img/tse-hyb.png" alt="TSE-HYB Güvenirlilik" style="height: 65px; object-fit: contain; mix-blend-mode: multiply;">
        </div>
        <p class="fx-hero__kicker" style="margin-bottom: 12px;"><span style="color:var(--fx-red); font-weight:800; letter-spacing:3px; font-size:14px; text-transform:uppercase;">Güvenilirliğin Adresi</span></p>
'''
c = c.replace(hero_kicker, new_hero_kicker)

# 3. Add UL/FM/NFPA logos to "Mühendislik süreci" or "Doğrulanabilir kurumsal kapasite"
# He said: "baret var ya fotoda oraya yerleştir"
# Is there a baret (helmet) photo? Let's check where the helmet photo is.

with open('index.html_temp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Temp created.")
