import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove inline colors from hero title and text to let CSS handle it (white text over dark scrim)
c = re.sub(
    r'<h1 class="fx-h1 fx-h1--hero fx-hero__title" style=".*?">Yangın söndürme sistemlerinde güvenilirliğin adresi</h1>',
    '<h1 class="fx-h1 fx-h1--hero fx-hero__title">Yangın söndürme sistemlerinde güvenilirliğin adresi</h1>',
    c
)

c = re.sub(
    r'<p class="fx-lead fx-hero__text" style=".*?">Sunucu odası, trafo merkezi, endüstriyel mutfak ve üretim tesislerinde gazlı söndürme, algılama ve periyodik bakım. Hacim hesabından devreye almaya kadar bütün süreci tek elden yürütüyoruz.</p>',
    '<p class="fx-lead fx-hero__text">Sunucu odası, trafo merkezi, endüstriyel mutfak ve üretim tesislerinde gazlı söndürme, algılama ve periyodik bakım. Hacim hesabından devreye almaya kadar bütün süreci tek elden yürütüyoruz.</p>',
    c
)

# Wait, let's just make sure the hero scrim on mobile is also dark so white text is readable.
# Currently in fenix-design.css, mobile scrim is: background:rgba(255,255,255,0.85); (which is WHITE)
# If the text is white and the background is white, it will be invisible on mobile!
# So we must fix the mobile scrim in CSS.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

