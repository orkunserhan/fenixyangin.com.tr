(function () {
  'use strict';

  /* ---------- yardımcılar ---------- */
  function nf(v, d) { return v.toLocaleString('tr-TR', { minimumFractionDigits: d, maximumFractionDigits: d }); }
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }

  /* ---------- 0 · CENTRAL REFERENCE REGISTRY (SINGLE SOURCE OF TRUTH) ---------- */
  window.FENIX_VERIFIED_REFS = [
    { id: "baykar", name: "Baykar", cat: "havacilik-savunma", logo: "ref-01-baykar.webp" },
    { id: "turk-hava-yollari", name: "Türk Hava Yolları", cat: "havacilik-savunma", logo: "ref-02-turk-hava-yollari.webp" },
    { id: "pegasus", name: "Pegasus", cat: "havacilik-savunma", logo: "ref-03-pegasus.webp" },
    { id: "hermes", name: "Hermès", cat: "turizm-perakende", logo: "ref-04-hermes.webp" },
    { id: "aksa", name: "Aksa", cat: "enerji-sanayi", logo: "ref-05-aksa.webp" },
    { id: "havelsan", name: "Havelsan", cat: "havacilik-savunma", logo: "ref-06-havelsan.webp" },
    { id: "odeabank", name: "Odeabank", cat: "finans-teknoloji", logo: "ref-07-odeabank.webp" },
    { id: "merit-royal", name: "Merit Royal", cat: "turizm-perakende", logo: "ref-08-merit-royal.webp" },
    { id: "sheraton-hotel", name: "Sheraton Hotel", cat: "turizm-perakende", logo: "ref-09-sheraton-hotel.webp" },
    { id: "trendyol", name: "Trendyol", cat: "finans-teknoloji", logo: "ref-10-trendyol.webp" },
    { id: "paribu", name: "Paribu", cat: "finans-teknoloji", logo: "ref-11-paribu.webp" },
    { id: "iga", name: "İGA İstanbul Havalimanı", cat: "havacilik-savunma", logo: "ref-12-iga.webp" },
    { id: "tupras", name: "Tüpraş", cat: "enerji-sanayi", logo: "ref-13-tupras.webp" },
    { id: "tusas-turk-havacilik-uzay-sanayii", name: "Türk Havacılık Uzay Sanayii (TUSAŞ)", cat: "havacilik-savunma", logo: "ref-14-tusas-turk-havacilik-uzay-sanayii.webp" },
    { id: "iett", name: "İETT", cat: "havacilik-savunma", logo: "ref-15-iett.webp" },
    { id: "tc-ulastirma-ve-altyapi-bakanligi", name: "T.C. Ulaştırma ve Altyapı Bakanlığı", cat: "havacilik-savunma", logo: "ref-16-tc-ulastirma-ve-altyapi-bakanligi.webp" },
    { id: "turkiye-is-bankasi", name: "Türkiye İş Bankası", cat: "finans-teknoloji", logo: "ref-17-turkiye-is-bankasi.webp" },
    { id: "turk-telekom", name: "Türk Telekom", cat: "finans-teknoloji", logo: "ref-19-turk-telekom.webp" },
    { id: "iron-mountain", name: "Iron Mountain", cat: "finans-teknoloji", logo: "ref-20-iron-mountain.webp" },
    { id: "aselsan", name: "ASELSAN", cat: "havacilik-savunma", logo: "ref-21-aselsan.webp" },
    { id: "turkiye-maarif-vakfi", name: "Türkiye Maarif Vakfı", cat: "turizm-perakende", logo: "ref-22-turkiye-maarif-vakfi.webp" },
    { id: "philip-morris", name: "Philip Morris", cat: "enerji-sanayi", logo: "ref-23-philip-morris.webp" },
    { id: "tulomsas", name: "TÜLOMSAŞ", cat: "enerji-sanayi", logo: "ref-24-tulomsas.webp" },
    { id: "turkiye-denizcilik-isletmeleri", name: "Türkiye Denizcilik İşletmeleri", cat: "havacilik-savunma", logo: "ref-25-turkiye-denizcilik-isletmeleri.webp" },
    { id: "iski", name: "İSKİ", cat: "enerji-sanayi", logo: "ref-26-iski.webp" },
    { id: "mutfak-sanatlari-akademisi-msa", name: "Mutfak Sanatları Akademisi (MSA)", cat: "turizm-perakende", logo: "ref-27-mutfak-sanatlari-akademisi-msa.webp" },
    { id: "hurriyet", name: "Hürriyet", cat: "finans-teknoloji", logo: "ref-28-hurriyet.webp" },
    { id: "vodafone", name: "Vodafone", cat: "finans-teknoloji", logo: "ref-29-vodafone.webp" },
    { id: "brt-bayrak-radyo-televizyon", name: "Bayrak Radyo Televizyon Kurumu (BRT)", cat: "finans-teknoloji", logo: "ref-30-brt-bayrak-radyo-televizyon.webp" },
    { id: "gokbora-uluslararasi-nakliyat", name: "Gökbora Uluslararası Nakliyat", cat: "enerji-sanayi", logo: "ref-31-gokbora-uluslararasi-nakliyat.webp" },
    { id: "tc-cevre-sehircilik-ve-iklim-degisikligi-bakanligi", name: "T.C. Çevre, Şehircilik ve İklim Değişikliği Bakanlığı", cat: "enerji-sanayi", logo: "ref-32-tc-cevre-sehircilik-ve-iklim-degisikligi-bakanligi.webp" },
    { id: "hilton-garden-inn", name: "Hilton Garden Inn", cat: "turizm-perakende", logo: "ref-33-hilton-garden-inn.webp" },
    { id: "tc-adalet-bakanligi", name: "T.C. Adalet Bakanlığı", cat: "havacilik-savunma", logo: "ref-34-tc-adalet-bakanligi.webp" },
    { id: "bahcesehir-koleji", name: "Bahçeşehir Koleji", cat: "turizm-perakende", logo: "ref-35-bahcesehir-koleji.webp" },
    { id: "the-marmara-hotels", name: "The Marmara Hotels", cat: "turizm-perakende", logo: "ref-36-the-marmara-hotels.webp" },
    { id: "tubitak", name: "TÜBİTAK", cat: "finans-teknoloji", logo: "ref-37-tubitak.webp" },
    { id: "tc-gumrukler-muhafaza", name: "T.C. Ticaret Bakanlığı (Gümrükler Muhafaza)", cat: "havacilik-savunma", logo: "ref-38-tc-gumrukler-muhafaza.webp" },
    { id: "senpilic", name: "Şenpiliç", cat: "turizm-perakende", logo: "ref-39-senpilic.webp" },
    { id: "vakif-pazarlama", name: "Vakıf Pazarlama", cat: "finans-teknoloji", logo: "ref-40-vakif-pazarlama.webp" },
    { id: "tc-saglik-bakanligi", name: "T.C. Sağlık Bakanlığı", cat: "turizm-perakende", logo: "ref-41-tc-saglik-bakanligi.webp" },
    { id: "istanbul-bilgi-universitesi", name: "İstanbul Bilgi Üniversitesi", cat: "turizm-perakende", logo: "ref-42-istanbul-bilgi-universitesi.webp" },
    { id: "ford", name: "Ford", cat: "enerji-sanayi", logo: "ref-43-ford.webp" },
    { id: "mark-antalya", name: "MarkAntalya", cat: "turizm-perakende", logo: "ref-44-mark-antalya.webp" },
    { id: "istek-okullari", name: "İSTEK Okulları", cat: "turizm-perakende", logo: "ref-45-istek-okullari.webp" },
    { id: "ramada-hotels", name: "Ramada Hotels", cat: "turizm-perakende", logo: "ref-46-ramada-hotels.webp" },
    { id: "renaissance-hotels", name: "Renaissance Hotels", cat: "turizm-perakende", logo: "ref-47-renaissance-hotels.webp" },
    { id: "yapi-kredi", name: "Yapı Kredi", cat: "finans-teknoloji", logo: "ref-48-yapi-kredi.webp" },
    { id: "112-acil-cagri-merkezi", name: "112 Acil Çağrı Merkezi", cat: "havacilik-savunma", logo: "ref-49-112-acil-cagri-merkezi.webp" },
    { id: "aslan-cimento", name: "Aslan Çimento", cat: "enerji-sanayi", logo: "ref-50-aslan-cimento.webp" },
    { id: "kasap-doner", name: "Kasap Döner", cat: "turizm-perakende", logo: "ref-51-kasap-doner.webp" },
    { id: "batman-universitesi", name: "Batman Üniversitesi", cat: "turizm-perakende", logo: "ref-52-batman-universitesi.webp" },
    { id: "sushico", name: "SushiCo", cat: "turizm-perakende", logo: "ref-53-sushico.webp" },
    { id: "tavuk-dunyasi", name: "Tavuk Dünyası", cat: "turizm-perakende", logo: "ref-54-tavuk-dunyasi.webp" },
    { id: "durumle", name: "Dürümle", cat: "turizm-perakende", logo: "ref-55-durumle.webp" },
    { id: "simit-sarayi", name: "Simit Sarayı", cat: "turizm-perakende", logo: "ref-55-simit-sarayi.webp" },
    { id: "pizza-hut", name: "Pizza Hut", cat: "turizm-perakende", logo: "ref-56-pizza-hut.webp" },
    { id: "tefal", name: "Tefal", cat: "turizm-perakende", logo: "ref-57-tefal.webp" },
    { id: "turkiye-petrolleri", name: "Türkiye Petrolleri (TP)", cat: "enerji-sanayi", logo: "ref-58-turkiye-petrolleri.webp" },
    { id: "sofra-grup", name: "Sofra Grup", cat: "turizm-perakende", logo: "ref-59-sofra-grup.webp" },
    { id: "baydoner", name: "Baydöner", cat: "turizm-perakende", logo: "ref-60-baydoner.webp" },
    { id: "jandarma-genel-komutanligi", name: "Jandarma Genel Komutanlığı", cat: "havacilik-savunma", logo: "ref-61-jandarma-genel-komutanligi.webp" },
    { id: "kfc", name: "KFC", cat: "turizm-perakende", logo: "ref-62-kfc.webp" },
    { id: "gozen-air-services", name: "Gözen Air Services", cat: "havacilik-savunma", logo: "ref-63-gozen-air-services.webp" },
    { id: "excelsior-hotel-baku", name: "Excelsior Hotel Baku", cat: "turizm-perakende", logo: "ref-64-excelsior-hotel-baku.webp" },
    { id: "ensar-vakfi", name: "Ensar Vakfı", cat: "turizm-perakende", logo: "ref-65-ensar-vakfi.webp" },
    { id: "migros", name: "Migros", cat: "turizm-perakende", logo: "ref-66-migros.webp" },
    { id: "sinefekt", name: "Sinefekt", cat: "finans-teknoloji", logo: "ref-67-sinefekt.webp" },
    { id: "anadolu-universitesi", name: "Anadolu Üniversitesi", cat: "turizm-perakende", logo: "ref-68-anadolu-universitesi.webp" },
    { id: "mapfre-sigorta", name: "MAPFRE Sigorta", cat: "finans-teknoloji", logo: "ref-69-mapfre-sigorta.webp" },
    { id: "yildiz-teknik-universitesi", name: "Yıldız Teknik Üniversitesi", cat: "turizm-perakende", logo: "ref-70-yildiz-teknik-universitesi.webp" },
    { id: "ibb-sosyal-tesisleri", name: "İBB Sosyal Tesisleri", cat: "turizm-perakende", logo: "ref-71-ibb-sosyal-tesisleri.webp" },
    { id: "odtu", name: "Orta Doğu Teknik Üniversitesi (ODTÜ)", cat: "turizm-perakende", logo: "ref-72-odtu.webp" },
    { id: "eskisehir-buyuksehir-belediyesi", name: "Eskişehir Büyükşehir Belediyesi", cat: "enerji-sanayi", logo: "ref-73-eskisehir-buyuksehir-belediyesi.webp" },
    { id: "eti", name: "ETİ", cat: "enerji-sanayi", logo: "ref-74-eti.webp" },
    { id: "tursab", name: "TÜRSAB", cat: "turizm-perakende", logo: "ref-75-tursab.webp" },
    { id: "ibb-kultur-as", name: "İBB Kültür A.Ş.", cat: "turizm-perakende", logo: "ref-75-ibb-kultur-as.webp" },
    { id: "unilever", name: "Unilever", cat: "enerji-sanayi", logo: "ref-76-unilever.webp" },
    { id: "totalenergies", name: "TotalEnergies", cat: "enerji-sanayi", logo: "ref-77-totalenergies.webp" },
    { id: "istanbul-arel-universitesi", name: "İstanbul Arel Üniversitesi", cat: "turizm-perakende", logo: "ref-77-istanbul-arel-universitesi.webp" },
    { id: "grohe", name: "Grohe", cat: "enerji-sanayi", logo: "ref-78-grohe.webp" },
    { id: "firat-universitesi", name: "Fırat Üniversitesi", cat: "turizm-perakende", logo: "ref-79-firat-universitesi.webp" },
    { id: "wyndham-hotels-resorts", name: "Wyndham Hotels & Resorts", cat: "turizm-perakende", logo: "ref-80-wyndham-hotels-resorts.webp" },
    { id: "gulermak-agir-sanayi", name: "Gülermak Ağır Sanayi", cat: "enerji-sanayi", logo: "ref-81-gulermak-agir-sanayi.webp" },
    { id: "koctas", name: "Koçtaş", cat: "turizm-perakende", logo: "ref-81-koctas.webp" },
    { id: "yilmaz-reduktor", name: "Yılmaz Redüktör", cat: "enerji-sanayi", logo: "ref-83-yilmaz-reduktor.webp" },
    { id: "cengiz-makina", name: "Cengiz Makina", cat: "enerji-sanayi", logo: "ref-84-cengiz-makina.webp" },
    { id: "park-inn-by-radisson", name: "Park Inn by Radisson", cat: "turizm-perakende", logo: "ref-85-park-inn-by-radisson.webp" },
    { id: "hyundai", name: "Hyundai", cat: "enerji-sanayi", logo: "ref-86-hyundai.webp" }
  ];

  window.fxInitReferenceCounts = function () {
    var refs = window.FENIX_VERIFIED_REFS || [];
    var domCards = document.querySelectorAll('.fx-ref-card');
    var total = Math.max(refs.length, domCards.length);

    document.querySelectorAll('[data-fx-stat="ref-count"]').forEach(function (el) {
      el.textContent = total + '+ Seçkin Kurum';
    });
    document.querySelectorAll('[data-fx-stat="ref-count-num"]').forEach(function (el) {
      el.textContent = total + '+';
    });
    document.querySelectorAll('[data-fx-stat="ref-count-text"]').forEach(function (el) {
      el.textContent = total + ' Kurumsal Marka';
    });
    document.querySelectorAll('[data-fx-stat="ref-filter-all"]').forEach(function (el) {
      el.textContent = 'Tümü (' + total + ')';
    });
    document.querySelectorAll('[data-fx-stat="ref-summary"]').forEach(function (el) {
      el.textContent = 'Uluslararası standartlarda korunan ' + total + '+ seçkin referansımız.';
    });

    var catCounts = {};
    if (domCards.length > 0) {
      document.querySelectorAll('.fx-ref-group').forEach(function (g) {
        var grp = g.getAttribute('data-group');
        var c = g.querySelectorAll('.fx-ref-card').length;
        catCounts[grp] = c;
        var lbl = g.querySelector('.fx-ref-section-head .fx-label');
        if (lbl) lbl.textContent = c + ' Referans';
      });
    } else {
      refs.forEach(function (r) {
        catCounts[r.cat] = (catCounts[r.cat] || 0) + 1;
      });
    }
    Object.keys(catCounts).forEach(function (cat) {
      document.querySelectorAll('[data-fx-stat="ref-filter-' + cat + '"]').forEach(function (el) {
        var name = el.getAttribute('data-cat-name') || el.textContent.split('(')[0].trim();
        el.textContent = name + ' (' + catCounts[cat] + ')';
      });
    });

    if (window.location.hash) {
      var h = window.location.hash.replace('#', '').replace('group-', '');
      var matchBtn = document.querySelector('.fx-filters .fx-chip[data-ref-cat="' + h + '"]');
      if (matchBtn && window.fxFilterRefs) {
        window.fxFilterRefs(h, matchBtn);
      }
    }
  };

  window.fxFilterRefs = function (cat, btn) {
    var chips = document.querySelectorAll('.fx-filters .fx-chip');
    chips.forEach(function (c) { c.classList.remove('is-active'); });
    if (btn) btn.classList.add('is-active');
    var groups = document.querySelectorAll('.fx-ref-group');
    groups.forEach(function (g) {
      if (cat === 'all' || g.getAttribute('data-group') === cat) {
        g.style.display = 'block';
      } else {
        g.style.display = 'none';
      }
    });
  };

  window.addEventListener('hashchange', function () {
    if (window.location.hash) {
      var h = window.location.hash.replace('#', '').replace('group-', '');
      var matchBtn = document.querySelector('.fx-filters .fx-chip[data-ref-cat="' + h + '"]');
      if (matchBtn && window.fxFilterRefs) {
        window.fxFilterRefs(h, matchBtn);
      }
    }
  });


  /* ---------- HACİM HESAPLAYICI ----------
     hacim = en × boy × yükseklik
     gaz   = hacim × 0,625
     tüp   = CEILING(gaz / 180)
     Bu formül değiştirilemez.                       */
  var ORAN = 0.625, TUP_KG = 180;
  window.fxInitCalculator = function () {
    var calc = $('[data-fx-calc]');
    if (!calc || calc.getAttribute('data-fx-calc-ready')) return;
    calc.setAttribute('data-fx-calc-ready', 'true');
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
  };
  window.fxInitCalculator();

  /* ---------- MOBİL MENÜ ---------- (Managed centrally with overlay and X button) */

  /* ---------- AKORDİYON (mobil menü alt seviye + footer) ---------- */
  $$('.fx-mobilenav__item[aria-expanded], .fx-accordion__head').forEach(function (b) {
    b.addEventListener('click', function () {
      b.setAttribute('aria-expanded', b.getAttribute('aria-expanded') === 'true' ? 'false' : 'true');
    });
  });

  /* ---------- DİNAMİK SEKTÖR & MEDYA RAYI (PHOTO-FIRST MEDIA RAIL) ---------- */
  window.fxInitStrip = function (strip) {
    if (!strip) {
      $$('[data-fx-strip]').forEach(function (s) {
        window.fxInitStrip(s);
      });
      return;
    }
    var container = strip.closest('section') || strip.parentNode.parentNode;
    var nav = container.querySelector('.fx-strip-nav');
    var b = nav ? $$('.fx-strip-nav__btn', nav) : [];
    var bar = container.querySelector('.fx-strip-progress__bar');
    var progressText = container.querySelector('.fx-strip-progress__text');
    var cards = $$('.fx-sector:not(.fx-strip__ghost)', strip);
    var totalCards = cards.length;

    // Dynamically initialize card badges (e.g. 01 / 07, 02 / 07...)
    cards.forEach(function (card, idx) {
      var badge = card.querySelector('.fx-sector__badge');
      var numStr = (idx < 9 ? '0' + (idx + 1) : (idx + 1)) + ' / ' + (totalCards < 10 ? '0' + totalCards : totalCards);
      if (badge) badge.textContent = numStr;
    });

    function updateStrip() {
      var max = strip.scrollWidth - strip.clientWidth;
      if (bar) bar.style.width = (max > 0 ? Math.max(12, (strip.scrollLeft / max) * 100) : 100) + '%';
      if (progressText && cards.length) {
        var cardW = cards[0].offsetWidth + (parseFloat(window.getComputedStyle(cards[0]).marginRight) || 20);
        var current = Math.min(totalCards, Math.max(1, Math.round(strip.scrollLeft / (cardW || 300)) + 1));
        var str = (current < 10 ? '0' + current : current) + ' / ' + (totalCards < 10 ? '0' + totalCards : totalCards) + ' · kaydır';
        progressText.textContent = str;
      }
      if (b[0]) b[0].classList.toggle('is-disabled', strip.scrollLeft <= 5);
      if (b[1]) b[1].classList.toggle('is-disabled', strip.scrollLeft >= max - 5);
    }

    function step(d) {
      var cardW = cards[0] ? cards[0].offsetWidth + 20 : strip.clientWidth * 0.75;
      strip.scrollBy({ left: d * cardW, behavior: 'smooth' });
    }

    if (b[0]) {
      b[0].onclick = function () { step(-1); };
      b[0].setAttribute('aria-label', 'Önceki sektör');
    }
    if (b[1]) {
      b[1].onclick = function () { step(1); };
      b[1].setAttribute('aria-label', 'Sonraki sektör');
    }
    strip.addEventListener('scroll', updateStrip, { passive: true });
    updateStrip();
  };

  $$('[data-fx-strip]').forEach(function (strip) {
    window.fxInitStrip(strip);
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

  /* ---------- DECISION RAIL (Ne / Nerede / Neden) ---------- */
  $$('[data-fx-decision-rail]').forEach(function (rail) {
    var section = rail.closest('section') || rail.parentNode.parentNode;
    var prevBtn = $('.fx-decision-navbtn--prev', section);
    var nextBtn = $('.fx-decision-navbtn--next', section);
    var bar = $('.fx-decision-progress__bar', section);
    var text = $('.fx-decision-progress__text', section);
    var cards = $$('.fx-decision-card', rail);
    var total = cards.length || 8;

    function updateProgress() {
      var max = rail.scrollWidth - rail.clientWidth;
      var pct = max > 0 ? Math.min(100, Math.max(12, (rail.scrollLeft / max) * 100)) : 100;
      if (bar) bar.style.width = pct + '%';
      if (text && cards.length) {
        var cardW = cards[0].offsetWidth + 20;
        var current = Math.min(total, Math.max(1, Math.round(rail.scrollLeft / cardW) + 1));
        var str = (current < 10 ? '0' + current : current) + ' / ' + (total < 10 ? '0' + total : total) + ' · Sağa kaydırın';
        text.textContent = str;
      }
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', function () {
        var step = (cards[0] ? cards[0].offsetWidth + 20 : 360);
        rail.scrollBy({ left: -step, behavior: 'smooth' });
      });
    }
    if (nextBtn) {
      nextBtn.addEventListener('click', function () {
        var step = (cards[0] ? cards[0].offsetWidth + 20 : 360);
        rail.scrollBy({ left: step, behavior: 'smooth' });
      });
    }
    rail.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();
  });

  /* ---------- CALCULATOR PDF / PRINT ACTION ---------- */
  $$('[data-fx-action="pdf"]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      window.print();
    });
  });

  /* ---------- MARQUEE · dokunmatik durdurma ---------- */
  $$('[data-fx-marquee]').forEach(function (m) {
    var t = $('.fx-marquee__track', m);
    if (!t) return;
    m.addEventListener('touchstart', function () { t.style.animationPlayState = 'paused'; }, { passive: true });
    m.addEventListener('touchend', function () { t.style.animationPlayState = 'running'; }, { passive: true });
  });

  /* ---------- MOBİL HEADER LOGO SHINE (VISIBILITY AWARE) ---------- */
  (function () {
    var sheen = document.querySelector('.fx-header .fx-logo__shine');
    if (!sheen) return;
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) {
        sheen.style.animationPlayState = 'paused';
      } else {
        sheen.style.animationPlayState = 'running';
      }
    });
  })();

  /* ---------- MOBILE DRAWER NAVIGATION (SINGLETON SITEWIDE) ---------- */
  function getMobileNavElements() {
    var burger = document.querySelector('.fx-burger');
    var nav = document.getElementById('fx-mobilenav');
    var overlay = document.querySelector('.fx-mobilenav-overlay');
    if (!overlay && document.body) {
      overlay = document.createElement('div');
      overlay.className = 'fx-mobilenav-overlay';
      document.body.appendChild(overlay);
      overlay.addEventListener('click', function (e) {
        window.fxCloseNav(e);
      });
    }
    return { burger: burger, nav: nav, overlay: overlay };
  }

  window.fxOpenNav = function (e) {
    if (e) { e.preventDefault(); e.stopPropagation(); }
    var els = getMobileNavElements();
    if (els.nav) els.nav.classList.add('is-open');
    if (els.overlay) els.overlay.classList.add('is-visible');
    if (els.burger) els.burger.setAttribute('aria-expanded', 'true');
    document.body.classList.add('fx-nav-open');
  };

  window.fxCloseNav = function (e) {
    if (e) { e.preventDefault(); e.stopPropagation(); }
    var els = getMobileNavElements();
    if (els.nav) els.nav.classList.remove('is-open');
    if (els.overlay) els.overlay.classList.remove('is-visible');
    if (els.burger) els.burger.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('fx-nav-open');
  };

  window.fxToggleNav = function (e) {
    if (e) { e.preventDefault(); e.stopPropagation(); }
    var els = getMobileNavElements();
    if (!els.nav) return;
    if (els.nav.classList.contains('is-open')) {
      window.fxCloseNav(e);
    } else {
      window.fxOpenNav(e);
    }
  };

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      window.fxCloseNav();
    }
  });

  /* ---------- MOBILE LOGO CINEMATIC REVEAL: ONE-TIME PER SESSION (5s) ---------- */
  (function () {
    try {
      if (sessionStorage.getItem('fx_logo_revealed')) {
        document.documentElement.classList.add('fx-logo-revealed');
      } else {
        sessionStorage.setItem('fx_logo_revealed', 'true');
        setTimeout(function () {
          document.documentElement.classList.add('fx-logo-revealed');
        }, 5000);
      }
    } catch (err) {}
  })();

  /* ---------- SİSTEMLER NAVİGASYONU (HIZLI SEÇİM SİSTEMİ) ---------- */
  window.FENIX_SYSTEMS = [
    { name: 'FM200 Yangın Söndürme Sistemleri', short: 'FM200 Yangın Söndürme', sub: 'HFC-227ea temiz gazlı söndürme', slug: 'fm200-gazli-yangin-sondurme-sistemleri.html' },
    { name: 'Novec 1230 Gazlı Yangın Söndürme', short: 'Novec 1230 Gazlı Yangın Söndürme', sub: 'FK-5-1-12 çevre dostu koruma', slug: 'novec-1230-gazli-yangin-sondurme-sistemleri.html' },
    { name: 'CO₂ Gazlı Yangın Söndürme', short: 'CO₂ Gazlı Yangın Söndürme', sub: 'Karbondioksit yüksek güç koruma', slug: 'co2-gazli-yangin-sondurme-sistemleri.html' },
    { name: 'Pano İçi Yangın Söndürme', short: 'Pano İçi Yangın Söndürme', sub: 'Mikro hacim otomatik söndürme', slug: 'pano-ici-yangin-sondurme-sistemleri.html' },
    { name: 'Aerosol Yangın Söndürme', short: 'Aerosol Yangın Söndürme', sub: 'Kondanse aerosol jeneratörleri', slug: 'aerosol-gazli-yangin-sondurme-sistemleri.html' },
    { name: 'Davlumbaz Yangın Söndürme', short: 'Davlumbaz Yangın Söndürme', sub: 'Endüstriyel mutfak yangın koruma', slug: 'davlumbaz-yangin-sondurme-sistemleri.html' },
    { name: 'Lityum / Batarya Yangın Söndürme', short: 'Lityum / Batarya Yangın Söndürme', sub: 'ESS ve batarya odası koruma', slug: 'lityum-batarya-yangin-sondurme-sistemleri.html' }
  ];

  window.fxInitSystemsNav = function () {
    var systems = window.FENIX_SYSTEMS || [];
    var p = window.location.pathname || '';
    var isSubPage = p.indexOf('/pages/') !== -1 || p.indexOf('\\pages\\') !== -1;
    if (!isSubPage) {
      var scr = document.querySelector('script[src*="js/fenix.js"]');
      if (scr && (scr.getAttribute('src') || '').indexOf('../') === 0) isSubPage = true;
    }
    if (!isSubPage) {
      var lnk = document.querySelector('link[href*="css/fenix-design.css"]');
      if (lnk && (lnk.getAttribute('href') || '').indexOf('../') === 0) isSubPage = true;
    }
    var prefix = isSubPage ? '' : 'pages/';

    /* --- 1. DESKTOP DROPDOWN --- */
    var desktopNav = document.querySelector('.fx-nav');
    if (desktopNav) {
      var sistemLink = desktopNav.querySelector('a[href*="sistemler.html"]');
      if (sistemLink && !sistemLink.closest('.fx-nav__item--dropdown')) {
        var wrap = document.createElement('div');
        wrap.className = 'fx-nav__item fx-nav__item--dropdown';

        sistemLink.classList.add('fx-nav__link--has-dropdown');
        sistemLink.setAttribute('aria-haspopup', 'true');
        sistemLink.setAttribute('aria-expanded', 'false');

        // Add caret icon
        var caret = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        caret.setAttribute('class', 'fx-nav__caret');
        caret.setAttribute('viewBox', '0 0 12 12');
        caret.setAttribute('width', '10');
        caret.setAttribute('height', '10');
        caret.setAttribute('fill', 'none');
        caret.setAttribute('stroke', 'currentColor');
        caret.setAttribute('stroke-width', '1.8');
        caret.setAttribute('stroke-linecap', 'round');
        caret.setAttribute('stroke-linejoin', 'round');
        caret.setAttribute('aria-hidden', 'true');
        var poly = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
        poly.setAttribute('points', '3 4.5 6 7.5 9 4.5');
        caret.appendChild(poly);
        sistemLink.appendChild(caret);

        // Build dropdown menu
        var dropdown = document.createElement('div');
        dropdown.className = 'fx-dropdown';
        dropdown.setAttribute('role', 'menu');
        dropdown.setAttribute('aria-label', 'Sistemler alt menüsü');

        var inner = document.createElement('div');
        inner.className = 'fx-dropdown__inner';

        var head = document.createElement('div');
        head.className = 'fx-dropdown__head';
        var eyebrow = document.createElement('span');
        eyebrow.className = 'fx-dropdown__eyebrow';
        eyebrow.textContent = 'Gazlı Yangın Söndürme Sistemleri';
        head.appendChild(eyebrow);
        inner.appendChild(head);

        var menu = document.createElement('div');
        menu.className = 'fx-dropdown__menu';

        systems.forEach(function (sys) {
          var item = document.createElement('a');
          var isCurrent = p.indexOf(sys.slug) !== -1;
          item.className = 'fx-dropdown__item' + (isCurrent ? ' is-active' : '');
          if (isCurrent) item.setAttribute('aria-current', 'page');
          item.href = prefix + sys.slug;
          item.setAttribute('role', 'menuitem');

          var main = document.createElement('div');
          main.className = 'fx-dropdown__item-main';

          var title = document.createElement('span');
          title.className = 'fx-dropdown__item-title';
          title.textContent = sys.name;

          var sub = document.createElement('span');
          sub.className = 'fx-dropdown__item-sub';
          sub.textContent = sys.sub;

          main.appendChild(title);
          main.appendChild(sub);

          var arr = document.createElement('span');
          arr.className = 'fx-dropdown__item-arrow';
          arr.setAttribute('aria-hidden', 'true');
          arr.textContent = '→';

          item.appendChild(main);
          item.appendChild(arr);
          menu.appendChild(item);
        });
        inner.appendChild(menu);

        var foot = document.createElement('div');
        foot.className = 'fx-dropdown__foot';
        var allLink = document.createElement('a');
        var isAllCurrent = p.indexOf('sistemler.html') !== -1;
        allLink.className = 'fx-dropdown__all' + (isAllCurrent ? ' is-active' : '');
        allLink.href = prefix + 'sistemler.html';
        allLink.setAttribute('role', 'menuitem');
        allLink.innerHTML = '<span>Tüm Sistemleri İnceleyin</span>' +
          '<svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>';
        foot.appendChild(allLink);
        inner.appendChild(foot);

        dropdown.appendChild(inner);

        // Replace sistemLink with wrap containing sistemLink and dropdown
        sistemLink.parentNode.insertBefore(wrap, sistemLink);
        wrap.appendChild(sistemLink);
        wrap.appendChild(dropdown);

        // Desktop interaction handlers
        wrap.addEventListener('mouseenter', function () {
          sistemLink.setAttribute('aria-expanded', 'true');
        });
        wrap.addEventListener('mouseleave', function () {
          sistemLink.setAttribute('aria-expanded', 'false');
          dropdown.classList.remove('is-open');
        });

        sistemLink.addEventListener('click', function (e) {
          if (window.innerWidth >= 761 && !dropdown.classList.contains('is-open')) {
            e.preventDefault();
            dropdown.classList.add('is-open');
            sistemLink.setAttribute('aria-expanded', 'true');
          }
        });

        document.addEventListener('click', function (e) {
          if (!wrap.contains(e.target)) {
            dropdown.classList.remove('is-open');
            sistemLink.setAttribute('aria-expanded', 'false');
          }
        });

        document.addEventListener('keydown', function (e) {
          if (e.key === 'Escape') {
            dropdown.classList.remove('is-open');
            sistemLink.setAttribute('aria-expanded', 'false');
          }
        });
      }
    }

    /* --- 2. MOBILE DRAWER ACCORDION --- */
    var mobDrawer = document.getElementById('fx-mobilenav');
    if (mobDrawer) {
      var mobList = mobDrawer.querySelector('.fx-mobilenav__list');
      if (mobList) {
        var mobLink = mobList.querySelector('a[href*="sistemler.html"]');
        if (mobLink && !mobLink.classList.contains('fx-mobilenav__link--accordion')) {
          mobLink.classList.add('fx-mobilenav__link--accordion');
          mobLink.setAttribute('role', 'button');
          mobLink.setAttribute('aria-expanded', 'false');
          mobLink.setAttribute('aria-controls', 'fx-mobilenav-systems-sub');

          var subBox = document.createElement('div');
          subBox.className = 'fx-mobilenav__sub';
          subBox.id = 'fx-mobilenav-systems-sub';
          subBox.setAttribute('role', 'region');
          subBox.setAttribute('aria-label', 'Sistemler alt menüsü');

          systems.forEach(function (sys) {
            var subLink = document.createElement('a');
            var isCurrent = p.indexOf(sys.slug) !== -1;
            subLink.className = 'fx-mobilenav__sublink' + (isCurrent ? ' is-active' : '');
            if (isCurrent) subLink.setAttribute('aria-current', 'page');
            subLink.href = prefix + sys.slug;
            subLink.innerHTML = '<span>' + (sys.short || sys.name) + '</span>' +
              '<span class="fx-mobilenav__sublink-bullet" aria-hidden="true">&#8250;</span>';
            subLink.addEventListener('click', function () {
              window.fxCloseNav();
            });
            subBox.appendChild(subLink);
          });

          // "Tüm Sistemler →" option
          var allMobLink = document.createElement('a');
          var isAllCurrentMob = p.indexOf('sistemler.html') !== -1;
          allMobLink.className = 'fx-mobilenav__sublink fx-mobilenav__sublink--all' + (isAllCurrentMob ? ' is-active' : '');
          allMobLink.href = prefix + 'sistemler.html';
          allMobLink.innerHTML = '<span>Tüm Sistemler →</span>';
          allMobLink.addEventListener('click', function () {
            window.fxCloseNav();
          });
          subBox.appendChild(allMobLink);

          mobLink.parentNode.insertBefore(subBox, mobLink.nextSibling);

          // Click / Tap toggle handler
          mobLink.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            var isOpen = subBox.classList.contains('is-open');
            if (isOpen) {
              subBox.classList.remove('is-open');
              mobLink.setAttribute('aria-expanded', 'false');
            } else {
              var otherSubs = mobDrawer.querySelectorAll('.fx-mobilenav__sub.is-open');
              otherSubs.forEach(function (s) { s.classList.remove('is-open'); });
              var otherAccs = mobDrawer.querySelectorAll('.fx-mobilenav__link--accordion[aria-expanded="true"]');
              otherAccs.forEach(function (a) { a.setAttribute('aria-expanded', 'false'); });

              subBox.classList.add('is-open');
              mobLink.setAttribute('aria-expanded', 'true');
            }
          });
        }
      }
    }
  };

  /* ---------- HİZMETLER NAVİGASYONU (6 TEMEL HİZMET HİYERARŞİSİ) ---------- */
  window.FENIX_SERVICES = [
    { name: 'Mühendislik', short: 'Mühendislik', sub: 'Yangın danışmanlığı, hidrolik hesap ve projelendirme', slug: 'iletisim.html' },
    { name: 'Kurulum', short: 'Kurulum', sub: 'Anahtar teslim sistem kurulumu ve entegrasyon', slug: 'iletisim.html' },
    { name: 'Montaj', short: 'Montaj', sub: 'Standartlara uygun mekanik ve elektriksel montaj', slug: 'iletisim.html' },
    { name: 'Tedarik', short: 'Tedarik', sub: 'Onaylı silindir, vana, nozul ve ekipman temini', slug: 'iletisim.html' },
    { name: 'Dolum', short: 'Dolum', sub: 'FM200 ve Novec 1230 sertifikalı gaz dolumu', slug: 'iletisim.html' },
    { name: 'Bakım', short: 'Bakım', sub: 'TSE-HYB onaylı periyodik bakım ve kontrol', slug: 'iletisim.html' }
  ];

  window.fxInitServicesNav = function () {
    var services = window.FENIX_SERVICES || [];
    var p = window.location.pathname || '';
    var isSubPage = p.indexOf('/pages/') !== -1 || p.indexOf('\\pages\\') !== -1;
    if (!isSubPage) {
      var scr = document.querySelector('script[src*="js/fenix.js"]');
      if (scr && (scr.getAttribute('src') || '').indexOf('../') === 0) isSubPage = true;
    }
    if (!isSubPage) {
      var lnk = document.querySelector('link[href*="css/fenix-design.css"]');
      if (lnk && (lnk.getAttribute('href') || '').indexOf('../') === 0) isSubPage = true;
    }
    var prefix = isSubPage ? '' : 'pages/';

    /* --- 1. DESKTOP DROPDOWN --- */
    var desktopNav = document.querySelector('.fx-nav');
    if (desktopNav) {
      var hizmetLink = desktopNav.querySelector('a[href*="hizmetler.html"]');
      if (hizmetLink && !hizmetLink.closest('.fx-nav__item--dropdown')) {
        var wrap = document.createElement('div');
        wrap.className = 'fx-nav__item fx-nav__item--dropdown';

        hizmetLink.classList.add('fx-nav__link--has-dropdown');
        hizmetLink.setAttribute('aria-haspopup', 'true');
        hizmetLink.setAttribute('aria-expanded', 'false');

        // Add caret icon
        var caret = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        caret.setAttribute('class', 'fx-nav__caret');
        caret.setAttribute('viewBox', '0 0 12 12');
        caret.setAttribute('width', '10');
        caret.setAttribute('height', '10');
        caret.setAttribute('fill', 'none');
        caret.setAttribute('stroke', 'currentColor');
        caret.setAttribute('stroke-width', '1.8');
        caret.setAttribute('stroke-linecap', 'round');
        caret.setAttribute('stroke-linejoin', 'round');
        caret.setAttribute('aria-hidden', 'true');
        var poly = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
        poly.setAttribute('points', '3 4.5 6 7.5 9 4.5');
        caret.appendChild(poly);
        hizmetLink.appendChild(caret);

        // Build dropdown menu
        var dropdown = document.createElement('div');
        dropdown.className = 'fx-dropdown';
        dropdown.setAttribute('role', 'menu');
        dropdown.setAttribute('aria-label', 'Hizmetler alt menüsü');

        var inner = document.createElement('div');
        inner.className = 'fx-dropdown__inner';

        var head = document.createElement('div');
        head.className = 'fx-dropdown__head';
        var eyebrow = document.createElement('span');
        eyebrow.className = 'fx-dropdown__eyebrow';
        eyebrow.textContent = 'Yangın Söndürme Hizmetleri';
        head.appendChild(eyebrow);
        inner.appendChild(head);

        var menu = document.createElement('div');
        menu.className = 'fx-dropdown__menu';

        services.forEach(function (svc) {
          var item = document.createElement('a');
          item.className = 'fx-dropdown__item';
          item.href = prefix + svc.slug;
          item.setAttribute('role', 'menuitem');

          var main = document.createElement('div');
          main.className = 'fx-dropdown__item-main';

          var title = document.createElement('span');
          title.className = 'fx-dropdown__item-title';
          title.textContent = svc.name;

          var sub = document.createElement('span');
          sub.className = 'fx-dropdown__item-sub';
          sub.textContent = svc.sub;

          main.appendChild(title);
          main.appendChild(sub);

          var arr = document.createElement('span');
          arr.className = 'fx-dropdown__item-arrow';
          arr.setAttribute('aria-hidden', 'true');
          arr.textContent = '→';

          item.appendChild(main);
          item.appendChild(arr);
          menu.appendChild(item);
        });
        inner.appendChild(menu);

        var foot = document.createElement('div');
        foot.className = 'fx-dropdown__foot';
        var allLink = document.createElement('a');
        var isAllCurrent = p.indexOf('hizmetler.html') !== -1;
        allLink.className = 'fx-dropdown__all' + (isAllCurrent ? ' is-active' : '');
        allLink.href = prefix + 'hizmetler.html';
        allLink.setAttribute('role', 'menuitem');
        allLink.innerHTML = '<span>Tüm Hizmetleri İnceleyin</span>' +
          '<svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>';
        foot.appendChild(allLink);
        inner.appendChild(foot);

        dropdown.appendChild(inner);

        // Replace hizmetLink with wrap containing hizmetLink and dropdown
        hizmetLink.parentNode.insertBefore(wrap, hizmetLink);
        wrap.appendChild(hizmetLink);
        wrap.appendChild(dropdown);

        // Desktop interaction handlers
        wrap.addEventListener('mouseenter', function () {
          hizmetLink.setAttribute('aria-expanded', 'true');
        });
        wrap.addEventListener('mouseleave', function () {
          hizmetLink.setAttribute('aria-expanded', 'false');
          dropdown.classList.remove('is-open');
        });

        hizmetLink.addEventListener('click', function (e) {
          if (window.innerWidth >= 761 && !dropdown.classList.contains('is-open')) {
            e.preventDefault();
            dropdown.classList.add('is-open');
            hizmetLink.setAttribute('aria-expanded', 'true');
          }
        });

        document.addEventListener('click', function (e) {
          if (!wrap.contains(e.target)) {
            dropdown.classList.remove('is-open');
            hizmetLink.setAttribute('aria-expanded', 'false');
          }
        });

        document.addEventListener('keydown', function (e) {
          if (e.key === 'Escape') {
            dropdown.classList.remove('is-open');
            hizmetLink.setAttribute('aria-expanded', 'false');
          }
        });
      }
    }

    /* --- 2. MOBILE DRAWER ACCORDION --- */
    var mobDrawer = document.getElementById('fx-mobilenav');
    if (mobDrawer) {
      var mobList = mobDrawer.querySelector('.fx-mobilenav__list');
      if (mobList) {
        var mobLink = mobList.querySelector('a[href*="hizmetler.html"]');
        if (mobLink && !mobLink.classList.contains('fx-mobilenav__link--accordion')) {
          mobLink.classList.add('fx-mobilenav__link--accordion');
          mobLink.setAttribute('role', 'button');
          mobLink.setAttribute('aria-expanded', 'false');
          mobLink.setAttribute('aria-controls', 'fx-mobilenav-services-sub');

          var subBox = document.createElement('div');
          subBox.className = 'fx-mobilenav__sub';
          subBox.id = 'fx-mobilenav-services-sub';
          subBox.setAttribute('role', 'region');
          subBox.setAttribute('aria-label', 'Hizmetler alt menüsü');

          services.forEach(function (svc) {
            var subLink = document.createElement('a');
            subLink.className = 'fx-mobilenav__sublink';
            subLink.href = prefix + svc.slug;
            subLink.innerHTML = '<span>' + (svc.short || svc.name) + '</span>' +
              '<span class="fx-mobilenav__sublink-bullet" aria-hidden="true">&#8250;</span>';
            subLink.addEventListener('click', function () {
              window.fxCloseNav();
            });
            subBox.appendChild(subLink);
          });

          // "Tüm Hizmetler →" option
          var allMobLink = document.createElement('a');
          var isAllCurrentMob = p.indexOf('hizmetler.html') !== -1;
          allMobLink.className = 'fx-mobilenav__sublink fx-mobilenav__sublink--all' + (isAllCurrentMob ? ' is-active' : '');
          allMobLink.href = prefix + 'hizmetler.html';
          allMobLink.innerHTML = '<span>Tüm Hizmetler →</span>';
          allMobLink.addEventListener('click', function () {
            window.fxCloseNav();
          });
          subBox.appendChild(allMobLink);

          mobLink.parentNode.insertBefore(subBox, mobLink.nextSibling);

          // Click / Tap toggle handler
          mobLink.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            var isOpen = subBox.classList.contains('is-open');
            if (isOpen) {
              subBox.classList.remove('is-open');
              mobLink.setAttribute('aria-expanded', 'false');
            } else {
              var otherSubs = mobDrawer.querySelectorAll('.fx-mobilenav__sub.is-open');
              otherSubs.forEach(function (s) { s.classList.remove('is-open'); });
              var otherAccs = mobDrawer.querySelectorAll('.fx-mobilenav__link--accordion[aria-expanded="true"]');
              otherAccs.forEach(function (a) { a.setAttribute('aria-expanded', 'false'); });

              subBox.classList.add('is-open');
              mobLink.setAttribute('aria-expanded', 'true');
            }
          });
        }
      }
    }
  };

  window.addEventListener('pageshow', function () {
    if (window.fxCloseNav) window.fxCloseNav();
  });

  /* Auto-initialize dynamic services/systems nav, calculator and reference counts */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      window.fxInitCalculator && window.fxInitCalculator();
      window.fxInitServicesNav && window.fxInitServicesNav();
      window.fxInitSystemsNav && window.fxInitSystemsNav();
      window.fxInitReferenceCounts && window.fxInitReferenceCounts();
    });
  } else {
    window.fxInitCalculator && window.fxInitCalculator();
    window.fxInitServicesNav && window.fxInitServicesNav();
    window.fxInitSystemsNav && window.fxInitSystemsNav();
    window.fxInitReferenceCounts && window.fxInitReferenceCounts();
  }
})();


