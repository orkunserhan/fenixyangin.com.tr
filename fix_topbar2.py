import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

topbar = '''<div class="fx-topbar" style="background:var(--fx-red); color:#fff; text-align:center; padding:12px 20px; font-size:14px; font-weight:500; display:flex; flex-direction:column; align-items:center; gap:12px; z-index:90; position:relative;">
  <div style="opacity:0.95; letter-spacing:0.3px;">Bizi arayın +90 212 618 07 01 - 02 <span style="margin:0 8px; opacity:0.5;">|</span> info@fenixyangin.com.tr</div>
  <div style="display:flex; gap:12px;">
    <a href="#" aria-label="X (Twitter)" style="display:inline-flex; align-items:center; justify-content:center; width:36px; height:36px; background:#fff; color:var(--fx-red); border-radius:50%; text-decoration:none;">
      <svg viewBox="0 0 24 24" style="width:18px; height:18px; fill:currentColor;"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
    </a>
    <a href="#" aria-label="Facebook" style="display:inline-flex; align-items:center; justify-content:center; width:36px; height:36px; background:#fff; color:var(--fx-red); border-radius:50%; text-decoration:none;">
      <svg viewBox="0 0 24 24" style="width:18px; height:18px; fill:currentColor;"><path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"/></svg>
    </a>
    <a href="#" aria-label="YouTube" style="display:inline-flex; align-items:center; justify-content:center; width:36px; height:36px; background:#fff; color:var(--fx-red); border-radius:50%; text-decoration:none;">
      <svg viewBox="0 0 24 24" style="width:18px; height:18px; fill:currentColor;"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.5 12 3.5 12 3.5s-7.505 0-9.377.55a3.016 3.016 0 0 0-2.122 2.136C0 8.07 0 12 0 12s0 3.93.501 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.55 9.377.55 9.377.55s7.505 0 9.377-.55a3.016 3.016 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zm9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    </a>
    <a href="#" aria-label="Instagram" style="display:inline-flex; align-items:center; justify-content:center; width:36px; height:36px; background:#fff; color:var(--fx-red); border-radius:50%; text-decoration:none;">
      <svg viewBox="0 0 24 24" style="width:18px; height:18px; fill:currentColor;"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zm12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>
    </a>
  </div>
</div>
'''

content = re.sub(r'<div class="fx-topbar".*?</div>\s*</div>\s*</div>', topbar, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
