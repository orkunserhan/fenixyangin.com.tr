import re

with open('css/fenix-design.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Truncate everything after '/* ---------- HERO SCRIM (Glassmorphism Transition) ---------- */'
idx = css.find('/* ---------- HERO SCRIM (Glassmorphism Transition) ---------- */')
if idx != -1:
    css = css[:idx]

# 2. Add the new CSS
new_css = '''
/* ---------- HERO SCRIM (Clean, Bright, Minimal) ---------- */
/* Masaüstü: Sol taraf aydınlık beyaz geçiş, fotoğrafa klas bir fade out */
.fx-hero--home .fx-hero__scrim {
  background: linear-gradient(90deg, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0.95) 30%, rgba(255, 255, 255, 0.7) 45%, transparent 65%) !important;
}

/* Mobil: Yukarıdan aşağıya aydınlık beyaz geçiş (yazıyı okutur, fotoyu kaybetmez) */
@media (max-width: 760px) {
  .fx-hero--home .fx-hero__scrim {
    background: linear-gradient(to bottom, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0.9) 55%, transparent 75%) !important;
  }
}

/* ---------- LOGO STYLES (Solid, Premium, No Animation) ---------- */
.fx-hero__logo-tse {
  height: 90px;
  object-fit: contain;
  background: #fff !important;
  border-radius: 8px;
  padding: 12px 24px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  border: 1px solid rgba(0,0,0,0.05);
  display: block;
}

.fx-hero__logo-certs {
  height: 120px;
  max-width: 100%;
  object-fit: contain;
  background: #fff !important;
  border-radius: 8px;
  padding: 12px 24px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  border: 1px solid rgba(0,0,0,0.05);
  display: block;
}

.fx-hero__aside {
  display: flex;
  gap: 16px;
  justify-content: flex-end;
  align-items: flex-end;
  height: 100%;
  padding-bottom: 40px;
}

/* Mobile Visibility Utilities */
@media (max-width: 760px) {
  .fx-desktop-only { display: none !important; }
  .fx-hero__logo-tse { height: 75px; padding: 10px 20px; margin: 0 auto; }
  .fx-hero__logo-certs { height: 85px; padding: 10px 20px; margin-top: 16px; align-self: center; }
  .fx-hero__aside { justify-content: center; padding-bottom: 20px; }
}
@media (min-width: 761px) {
  .fx-mobile-only { display: none !important; }
}

/* Ensure text is perfectly readable over the bright scrim */
.fx-hero--home .fx-hero__title {
  color: var(--fx-ink) !important;
}

.fx-hero--home .fx-hero__text {
  color: var(--fx-body) !important;
}

/* ---------- FENIX LOGO SHINE EFFECT ---------- */
.fx-logo img {
  width: 175px !important; /* Bir tık daha büyük */
  height: auto;
}
.fx-logo {
  position: relative;
  display: inline-block;
  overflow: hidden;
}
.fx-logo::after {
  content: "";
  position: absolute;
  top: 0;
  left: -150%;
  width: 30%;
  height: 100%;
  background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,0.7) 50%, rgba(255,255,255,0) 100%);
  transform: skewX(-25deg);
  animation: fx-shine 15s infinite;
}
@keyframes fx-shine {
  0%, 85% { left: -150%; }
  95%, 100% { left: 200%; }
}

/* Fix Mobile Burger Z-index */
.fx-burger {
  position: relative;
  z-index: 1001; /* Ensure it's clickable above everything */
}
'''

with open('css/fenix-design.css', 'w', encoding='utf-8') as f:
    f.write(css + new_css)
