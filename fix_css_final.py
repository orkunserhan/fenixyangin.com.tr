import re

with open('css/fenix-design.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove everything after the start of my custom hero scrim
idx = css.find('/* ---------- HERO SCRIM (Clean, Bright, Minimal) ---------- */')
if idx != -1:
    css = css[:idx]

new_css = '''
/* ---------- HERO SCRIM (Clean, Bright, Minimal) ---------- */
/* Masaüstü: Sol taraf aydınlık beyaz geçiş, fotoğrafa klas bir fade out */
.fx-hero--home .fx-hero__scrim {
  background: linear-gradient(90deg, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0.95) 30%, rgba(255, 255, 255, 0.7) 45%, transparent 65%) !important;
}

/* Mobil: Yukarıdan aşağıya aydınlık beyaz geçiş (yazıyı okutur, fotoyu kaybetmez) */
@media (max-width: 760px) {
  .fx-hero--home .fx-hero__scrim {
    background: linear-gradient(to bottom, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0.95) 50%, transparent 80%) !important;
  }
}

/* Ensure text is perfectly readable over the bright scrim */
.fx-hero--home .fx-hero__title {
  color: var(--fx-ink) !important;
}
.fx-hero--home .fx-hero__text {
  color: var(--fx-body) !important;
}

/* ---------- LOGO STYLES ---------- */
/* Desktop (Sağ Alt Köşe - Cam Efekti / Glassmorphism Çerçeve) */
.fx-hero__logo-tse, .fx-hero__logo-certs {
  background: rgba(255, 255, 255, 0.6) !important;
  backdrop-filter: blur(12px);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.8);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  mix-blend-mode: normal !important;
  display: block;
}

.fx-hero__logo-tse {
  height: 95px;
  padding: 12px 24px;
}
.fx-hero__logo-certs {
  height: 110px;
  padding: 12px 24px;
}

.fx-hero__aside {
  display: flex;
  gap: 16px;
  justify-content: flex-end;
  align-items: flex-end;
  height: 100%;
  padding-bottom: 40px;
  padding-right: 20px;
}

/* Mobile Visibility & Styles */
@media (max-width: 760px) {
  .fx-desktop-only { display: none !important; }
  
  /* Mobilde TSE logosu tam ortada, çerçevesiz, transparan (multiply) */
  .fx-hero__logo-tse { 
    height: 70px; 
    margin: 0 auto 16px auto; 
    background: transparent !important;
    border: none;
    box-shadow: none;
    backdrop-filter: none;
    mix-blend-mode: multiply !important;
    padding: 0;
  }
  
  /* Mobilde UL/FM logosu aşağıda, ortalanmış, çerçevesiz transparan */
  .fx-hero__logo-certs { 
    height: 75px; 
    margin: 24px auto 0 auto; 
    align-self: center; 
    background: transparent !important;
    border: none;
    box-shadow: none;
    backdrop-filter: none;
    mix-blend-mode: multiply !important;
    padding: 0;
  }
  
  .fx-hero__aside { justify-content: center; padding-bottom: 20px; padding-right: 0; }
}
@media (min-width: 761px) {
  .fx-mobile-only { display: none !important; }
}

/* ---------- FENIX LOGO SHINE EFFECT ---------- */
.fx-logo img {
  width: 175px !important;
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

/* Fix Mobile Burger Z-index and Click */
.fx-burger {
  position: relative;
  z-index: 1001 !important;
  cursor: pointer;
}
.fx-burger svg {
  pointer-events: none; /* Ensure click hits the button */
}
'''

with open('css/fenix-design.css', 'w', encoding='utf-8') as f:
    f.write(css + new_css)
