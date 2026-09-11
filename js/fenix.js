(function () {
  'use strict';

  /* ---------- yardımcılar ---------- */
  function nf(v, d) { return v.toLocaleString('tr-TR', { minimumFractionDigits: d, maximumFractionDigits: d }); }
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }

  /* ---------- HACİM HESAPLAYICI ----------
     hacim = en × boy × yükseklik
     gaz   = hacim × 0,625
     tüp   = CEILING(gaz / 180)
     Bu formül değiştirilemez.                       */
  var ORAN = 0.625, TUP_KG = 180;
  var calc = $('[data-fx-calc]');
  if (calc) {
    var st = { en: 8, boy: 5, yukseklik: 3.6 };
    var lim = { en: [1, 60], boy: [1, 60], yukseklik: [1.5, 12] };
    var view = 'iso';

    function isoGeo(w, d, h) {
      var C = Math.cos(Math.PI / 6), S = Math.sin(Math.PI / 6);
      var raw = [[0,0,0],[w,0,0],[w,d,0],[0,d,0],[0,0,h],[w,0,h],[w,d,h],[0,d,h]]
        .map(function (p) { return [(p[0] - p[1]) * C, (p[0] + p[1]) * S - p[2]]; });
      var xs = raw.map(function (p) { return p[0]; }), ys = raw.map(function (p) { return p[1]; });
      var bw = Math.max.apply(null, xs) - Math.min.apply(null, xs);
      var bh = Math.max.apply(null, ys) - Math.min.apply(null, ys);
      var k = Math.min(400 / bw, 250 / bh);
      var ox = 260 - (Math.min.apply(null, xs) + bw / 2) * k;
      var oy = 215 - (Math.min.apply(null, ys) + bh / 2) * k;
      var P = raw.map(function (p) { return [p[0] * k + ox, p[1] * k + oy]; });
      var f = function (i) { return P[i][0].toFixed(1) + ',' + P[i][1].toFixed(1); };
      var pl = function (a) { return a.map(f).join(' '); };
      var mid = function (i, j) { return [(P[i][0] + P[j][0]) / 2, (P[i][1] + P[j][1]) / 2]; };
      var nx = (P[4][0] + P[6][0]) / 2, ny = (P[4][1] + P[6][1]) / 2;
      var q = function (a, b, c, d2, e, f2) {
        return 'M ' + a.toFixed(1) + ' ' + b.toFixed(1) + ' Q ' + c.toFixed(1) + ' ' + d2.toFixed(1) + ' ' + e.toFixed(1) + ' ' + f2.toFixed(1);
      };
      var mEn = mid(0, 1), mBoy = mid(0, 3), mYuk = mid(0, 4);
      return {
        top: pl([4,5,6,7]), w1: pl([0,1,5,4]), w2: pl([0,3,7,4]),
        hid: pl([1,2,3]), hidV: pl([2,6]), edge: pl([3,0,1]),
        v0: pl([0,4]), v1: pl([1,5]), v3: pl([3,7]),
        nx: nx.toFixed(1), ny: ny.toFixed(1), ny2: (ny - 17).toFixed(1),
        arc1: q(nx - 26, ny + 15, nx, ny + 2, nx + 26, ny + 15),
        arc2: q(nx - 42, ny + 27, nx, ny + 6, nx + 42, ny + 27),
        enX: (mEn[0] + 4).toFixed(1), enY: (mEn[1] + 22).toFixed(1),
        boyX: (mBoy[0] - 6).toFixed(1), boyY: (mBoy[1] + 22).toFixed(1),
        yukX: (mYuk[0] - 16).toFixed(1), yukY: mYuk[1].toFixed(1)
      };
    }

    function planGeo(w, d) {
      var k = Math.min(400 / w, 250 / d);
      var pw = w * k, ph = d * k, x = 260 - pw / 2, y = 215 - ph / 2;
      return {
        x: x.toFixed(1), y: y.toFixed(1), w: pw.toFixed(1), h: ph.toFixed(1),
        cx: (x + pw / 2).toFixed(1), cy: (y + ph / 2).toFixed(1),
        topT: (y - 14).toFixed(1), botT: (y + ph + 26).toFixed(1),
        leftX: (x - 12).toFixed(1)
      };
    }

    function render() {
      var vol = st.en * st.boy * st.yukseklik;
      var gaz = vol * ORAN;
      var tup = Math.ceil(gaz / TUP_KG);
      var taban = st.en * st.boy;

      $$('[data-fx-dim]').forEach(function (i) { if (document.activeElement !== i) i.value = st[i.getAttribute('data-fx-dim')]; });
      $$('[data-fx-range]').forEach(function (i) { i.value = st[i.getAttribute('data-fx-range')]; });

      $('[data-fx-out="hacim"]').textContent = vol.toLocaleString('tr-TR', { maximumFractionDigits: vol < 100 ? 1 : 0 });
      $('[data-fx-out="formul"]').textContent = nf(st.en, 1) + ' × ' + nf(st.boy, 1) + ' × ' + nf(st.yukseklik, 1);
      $('[data-fx-out="taban"]').textContent = nf(taban, 1) + ' m²';
      $('[data-fx-out="gaz"]').textContent = nf(gaz, gaz < 100 ? 1 : 0) + ' kg';
      $('[data-fx-out="tup"]').textContent = tup;

      var svgIso = $('[data-fx-canvas="iso"]'), svgPlan = $('[data-fx-canvas="plan"]');
      svgIso.style.display = view === 'iso' ? 'block' : 'none';
      svgPlan.style.display = view === 'plan' ? 'block' : 'none';

      if (view === 'iso') {
        var g = isoGeo(st.en, st.boy, st.yukseklik);
        var p = $$('polygon,polyline,line,path,text', svgIso);
        svgIso.querySelector('[data-g="fill-top"]').setAttribute('points', g.top);
        svgIso.querySelector('[data-g="fill-w1"]').setAttribute('points', g.w1);
        svgIso.querySelector('[data-g="fill-w2"]').setAttribute('points', g.w2);
        svgIso.querySelector('[data-g="hid"]').setAttribute('points', g.hid);
        svgIso.querySelector('[data-g="hidv"]').setAttribute('points', g.hidV);
        svgIso.querySelector('[data-g="edge-top"]').setAttribute('points', g.top);
        svgIso.querySelector('[data-g="edge-base"]').setAttribute('points', g.edge);
        svgIso.querySelector('[data-g="v0"]').setAttribute('points', g.v0);
        svgIso.querySelector('[data-g="v1"]').setAttribute('points', g.v1);
        svgIso.querySelector('[data-g="v3"]').setAttribute('points', g.v3);
        var nz = svgIso.querySelector('[data-g="noz"]');
        nz.setAttribute('x1', g.nx); nz.setAttribute('x2', g.nx); nz.setAttribute('y1', g.ny2); nz.setAttribute('y2', g.ny);
        svgIso.querySelector('[data-g="arc1"]').setAttribute('d', g.arc1);
        svgIso.querySelector('[data-g="arc2"]').setAttribute('d', g.arc2);
        var tEn = svgIso.querySelector('[data-g="t-en"]'), tBoy = svgIso.querySelector('[data-g="t-boy"]'), tYuk = svgIso.querySelector('[data-g="t-yuk"]');
        tEn.setAttribute('x', g.enX); tEn.setAttribute('y', g.enY); tEn.textContent = 'En ' + nf(st.en, 1) + ' m';
        tBoy.setAttribute('x', g.boyX); tBoy.setAttribute('y', g.boyY); tBoy.textContent = 'Boy ' + nf(st.boy, 1) + ' m';
        tYuk.setAttribute('x', g.yukX); tYuk.setAttribute('y', g.yukY); tYuk.textContent = 'Yük. ' + nf(st.yukseklik, 1) + ' m';
      } else {
        var q = planGeo(st.en, st.boy);
        var r = svgPlan.querySelector('[data-g="rect"]');
        r.setAttribute('x', q.x); r.setAttribute('y', q.y); r.setAttribute('width', q.w); r.setAttribute('height', q.h);
        $$('[data-g^="ring"]', svgPlan).forEach(function (c) { c.setAttribute('cx', q.cx); c.setAttribute('cy', q.cy); });
        var pt = svgPlan.querySelector('[data-g="t-en"]'), pb = svgPlan.querySelector('[data-g="t-alan"]'), pv = svgPlan.querySelector('[data-g="t-boy"]');
        pt.setAttribute('x', q.cx); pt.setAttribute('y', q.topT); pt.textContent = 'En ' + nf(st.en, 1) + ' m';
        pb.setAttribute('x', q.cx); pb.setAttribute('y', q.botT); pb.textContent = nf(taban, 1) + ' m² · yük. ' + nf(st.yukseklik, 1) + ' m';
        pv.setAttribute('x', q.leftX); pv.setAttribute('y', q.cy); pv.textContent = 'Boy ' + nf(st.boy, 1) + ' m';
      }
    }

    function set(k, v) {
      var l = lim[k];
      st[k] = Math.min(l[1], Math.max(l[0], Math.round(v * 10) / 10));
      render();
    }

    $$('[data-fx-dim]').forEach(function (i) {
      i.addEventListener('input', function () { var v = parseFloat(i.value); if (!isNaN(v)) set(i.getAttribute('data-fx-dim'), v); });
    });
    $$('[data-fx-range]').forEach(function (i) {
      i.addEventListener('input', function () { set(i.getAttribute('data-fx-range'), parseFloat(i.value)); });
    });
    $$('[data-fx-step]').forEach(function (b) {
      b.addEventListener('click', function () {
        var a = b.getAttribute('data-fx-step').split(',');
        set(a[0], st[a[0]] + parseFloat(a[1]));
      });
    });
    $$('[data-fx-view]').forEach(function (b) {
      b.addEventListener('click', function () {
        view = b.getAttribute('data-fx-view');
        $$('[data-fx-view]').forEach(function (x) {
          var on = x === b;
          x.classList.toggle('is-active', on);
          x.setAttribute('aria-selected', on ? 'true' : 'false');
        });
        render();
      });
    });
    render();
  }

  /* ---------- MOBİL MENÜ ---------- (Managed centrally with overlay and X button) */

  /* ---------- AKORDİYON (mobil menü alt seviye + footer) ---------- */
  $$('.fx-mobilenav__item[aria-expanded], .fx-accordion__head').forEach(function (b) {
    b.addEventListener('click', function () {
      b.setAttribute('aria-expanded', b.getAttribute('aria-expanded') === 'true' ? 'false' : 'true');
    });
  });

  /* ---------- ŞERİT OKLARI ---------- */
  $$('[data-fx-strip]').forEach(function (strip) {
    var nav = strip.parentNode.parentNode.querySelector('.fx-strip-nav');
    if (!nav) return;
    var b = $$('.fx-strip-nav__btn', nav);
    function step(d) { strip.scrollBy({ left: d * strip.clientWidth * 0.7, behavior: 'smooth' }); }
    if (b[0]) b[0].addEventListener('click', function () { step(-1); });
    if (b[1]) b[1].addEventListener('click', function () { step(1); });
    var bar = strip.parentNode.querySelector('.fx-strip-progress__bar');
    if (bar) strip.addEventListener('scroll', function () {
      var max = strip.scrollWidth - strip.clientWidth;
      bar.style.width = (max > 0 ? Math.max(12, (strip.scrollLeft / max) * 100) : 100) + '%';
    });
  });

  /* ---------- VİDEO · TIKLA-YÜKLE (ilk yüklemede iframe yok) ---------- */
  /* ---------- VİDEO · TIKLA-YÜKLE (ilk yüklemede iframe yok) ----------
     data-fx-yt herhangi bir YouTube biçimini kabul eder; ID'ye indirger.
     Ölçü/oran KODDA sabittir (.fx-video aspect-ratio) — Admin ölçü giremez. */
  function fxYtId(v) {
    if (!v) return '';
    v = String(v).trim();
    if (/^[\w-]{11}$/.test(v)) return v;
    var m = v.match(/(?:youtube\.com\/(?:watch\?(?:.*&)?v=|embed\/|shorts\/|live\/)|youtu\.be\/)([\w-]{11})/);
    return m ? m[1] : '';
  }

  $$('[data-fx-video]').forEach(function (box) {
    var btn = $('.fx-video__play', box);
    if (!btn) return;
    btn.addEventListener('click', function () {
      var id = fxYtId(box.getAttribute('data-fx-yt'));
      if (!id) return;
      var f = document.createElement('iframe');
      f.className = 'fx-video__frame';
      f.setAttribute('title', box.getAttribute('data-fx-title') || 'Fenix Yangın video');
      f.setAttribute('loading', 'lazy');
      f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0';
      f.setAttribute('allow', 'accelerometer; autoplay; encrypted-media; picture-in-picture');
      f.setAttribute('allowfullscreen', '');
      f.setAttribute('title', 'Video');
      box.appendChild(f);
      box.classList.add('is-playing');
    });
  });

  /* ---------- MARQUEE · dokunmatik durdurma ---------- */
  $$('[data-fx-marquee]').forEach(function (m) {
    var t = $('.fx-marquee__track', m);
    if (!t) return;
    m.addEventListener('touchstart', function () { t.style.animationPlayState = 'paused'; }, { passive: true });
    m.addEventListener('touchend', function () { t.style.animationPlayState = 'running'; }, { passive: true });
  });
})();
