/**
 * FENIX YANGIN — KVKK & GDPR Consent Manager (Görev 3 & Görev 5)
 * Handles Consent Mode v2 (Advanced Mode), banner rendering, preference modal,
 * localStorage persistence (12 months), and phone/WhatsApp/form interaction tracking.
 */
(function () {
  'use strict';

  var CONSENT_KEY = 'fx_consent';
  var TWELVE_MONTHS_MS = 365 * 24 * 60 * 60 * 1000;

  function getSavedConsent() {
    try {
      var item = localStorage.getItem(CONSENT_KEY);
      if (!item) return null;
      var parsed = JSON.parse(item);
      var ts = parsed.timestamp || parsed.ts;
      if (parsed && typeof ts === 'number' && (Date.now() - ts) < TWELVE_MONTHS_MS) {
        return parsed;
      }
    } catch (e) {}
    return null;
  }

  function saveConsent(analyticsGranted, adGranted) {
    var now = Date.now();
    var consentData = {
      ad: !!adGranted,
      analytics: !!analyticsGranted,
      timestamp: now,
      ts: now,
      version: 1,
      date: new Date().toISOString()
    };
    try {
      localStorage.setItem(CONSENT_KEY, JSON.stringify(consentData));
    } catch (e) {}

    // Apply Consent Mode Update
    if (typeof window.gtag === 'function') {
      window.gtag('consent', 'update', {
        'ad_storage': adGranted ? 'granted' : 'denied',
        'ad_user_data': adGranted ? 'granted' : 'denied',
        'ad_personalization': adGranted ? 'granted' : 'denied',
        'analytics_storage': analyticsGranted ? 'granted' : 'denied'
      });
    }

    // Trigger consent_update event on dataLayer
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: 'consent_update',
      consent_status: {
        analytics: analyticsGranted ? 'granted' : 'denied',
        ad: adGranted ? 'granted' : 'denied'
      }
    });
  }

  function getPolicyUrl() {
    var isPages = window.location.pathname.indexOf('/pages/') !== -1;
    return isPages ? 'cerez-politikasi.html' : 'pages/cerez-politikasi.html';
  }

  function createUI() {
    if (document.getElementById('fx-consent-banner')) return;

    var policyHref = getPolicyUrl();

    // 1. Bottom Banner
    var banner = document.createElement('div');
    banner.id = 'fx-consent-banner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', 'Çerez ve Gizlilik Tercihleri');
    banner.innerHTML =
      '<div class="fx-cb-inner">' +
        '<div class="fx-cb-content">' +
          '<p class="fx-cb-text">' +
            'Sitemizde temel fonksiyonların çalışması, kullanıcı deneyiminizin iyileştirilmesi ve ziyaret trafiğinin analizi için KVKK mevzuatına uygun çerezler kullanılmaktadır. Detaylar için <a href="' + policyHref + '">Çerez Politikamızı</a> inceleyebilirsiniz.' +
          '</p>' +
        '</div>' +
        '<div class="fx-cb-actions">' +
          '<button type="button" class="fx-cb-btn" id="fx-cb-accept">Tümünü Kabul Et</button>' +
          '<button type="button" class="fx-cb-btn" id="fx-cb-reject">Tümünü Reddet</button>' +
          '<button type="button" class="fx-cb-btn" id="fx-cb-prefs">Tercihleri Yönet</button>' +
        '</div>' +
      '</div>';

    // 2. Preferences Modal
    var modal = document.createElement('div');
    modal.id = 'fx-consent-modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-label', 'Çerez Tercihlerini Özelleştirin');
    modal.innerHTML =
      '<div class="fx-cm-card">' +
        '<div class="fx-cm-header">' +
          '<h3 class="fx-cm-title">Çerez Tercihleri</h3>' +
          '<button type="button" class="fx-cm-close" id="fx-cm-close" aria-label="Kapat">&times;</button>' +
        '</div>' +
        '<p class="fx-cm-desc">' +
          'Web sitemizdeki deneyiminizi geliştirmek ve hizmet kalitemizi artırmak için çerezleri yönetebilirsiniz. Zorunlu çerezler web sitesinin çalışması için gereklidir.' +
        '</p>' +
        '<div class="fx-cm-groups">' +
          '<div class="fx-cm-group">' +
            '<div class="fx-cm-group-info">' +
              '<div class="fx-cm-group-title">Gerekli Çerezler (Zorunlu)</div>' +
              '<p class="fx-cm-group-text">Sitenin güvenliği, gezinmesi ve temel fonksiyonları için zorunludur, kapatılamaz.</p>' +
            '</div>' +
            '<label class="fx-cm-switch">' +
              '<input type="checkbox" checked disabled>' +
              '<span class="fx-cm-slider"></span>' +
            '</label>' +
          '</div>' +
          '<div class="fx-cm-group">' +
            '<div class="fx-cm-group-info">' +
              '<div class="fx-cm-group-title">Analitik Çerezler</div>' +
              '<p class="fx-cm-group-text">Ziyaretçi sayılarını, trafik kaynaklarını ve sayfa etkileşimlerini ölçmemize yardımcı olur.</p>' +
            '</div>' +
            '<label class="fx-cm-switch">' +
              '<input type="checkbox" id="fx-cm-toggle-analytics">' +
              '<span class="fx-cm-slider"></span>' +
            '</label>' +
          '</div>' +
          '<div class="fx-cm-group">' +
            '<div class="fx-cm-group-info">' +
              '<div class="fx-cm-group-title">Pazarlama Çerezleri</div>' +
              '<p class="fx-cm-group-text">İlgi alanlarınıza uygun tanıtım sunmak ve kampanyaların performansını ölçmek için kullanılır.</p>' +
            '</div>' +
            '<label class="fx-cm-switch">' +
              '<input type="checkbox" id="fx-cm-toggle-ad">' +
              '<span class="fx-cm-slider"></span>' +
            '</label>' +
          '</div>' +
        '</div>' +
        '<div class="fx-cm-actions">' +
          '<button type="button" class="fx-cb-btn" id="fx-cm-save">Seçimi Kaydet</button>' +
        '</div>' +
      '</div>';

    document.body.appendChild(banner);
    document.body.appendChild(modal);

    function hideAll() {
      if (banner) banner.style.display = 'none';
      if (modal) modal.classList.remove('is-open');
    }

    function openModal() {
      var current = getSavedConsent();
      var analyticsToggle = document.getElementById('fx-cm-toggle-analytics');
      var adToggle = document.getElementById('fx-cm-toggle-ad');
      if (analyticsToggle) analyticsToggle.checked = current ? current.analytics : false;
      if (adToggle) adToggle.checked = current ? current.ad : false;
      modal.classList.add('is-open');
    }

    function closeModal() {
      modal.classList.remove('is-open');
    }

    document.getElementById('fx-cb-accept').addEventListener('click', function () {
      saveConsent(true, true);
      hideAll();
    });

    document.getElementById('fx-cb-reject').addEventListener('click', function () {
      saveConsent(false, false);
      hideAll();
    });

    document.getElementById('fx-cb-prefs').addEventListener('click', function () {
      openModal();
    });

    document.getElementById('fx-cm-close').addEventListener('click', function () {
      closeModal();
    });

    document.getElementById('fx-cm-save').addEventListener('click', function () {
      var aVal = !!(document.getElementById('fx-cm-toggle-analytics') && document.getElementById('fx-cm-toggle-analytics').checked);
      var adVal = !!(document.getElementById('fx-cm-toggle-ad') && document.getElementById('fx-cm-toggle-ad').checked);
      saveConsent(aVal, adVal);
      hideAll();
    });

    // Close modal on background click
    modal.addEventListener('click', function (e) {
      if (e.target === modal) {
        closeModal();
      }
    });

    // Close modal on Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modal.classList.contains('is-open')) {
        closeModal();
      }
    });

    // If user already had a valid consent, keep banner hidden initially
    var existing = getSavedConsent();
    if (existing) {
      banner.style.display = 'none';
    }
  }

  // Footer "Çerez tercihleri" trigger listener
  document.addEventListener('click', function (e) {
    var trigger = e.target.closest('.fx-consent-trigger, #fx-consent-settings, a[href*="cerez-tercihleri"]');
    if (trigger) {
      e.preventDefault();
      createUI();
      var banner = document.getElementById('fx-consent-banner');
      if (banner) banner.style.display = 'none';
      var modal = document.getElementById('fx-consent-modal');
      if (modal) {
        var current = getSavedConsent();
        var analyticsToggle = document.getElementById('fx-cm-toggle-analytics');
        var adToggle = document.getElementById('fx-cm-toggle-ad');
        if (analyticsToggle) analyticsToggle.checked = current ? current.analytics : false;
        if (adToggle) adToggle.checked = current ? current.ad : false;
        modal.classList.add('is-open');
      }
    }
  });

  // Initialize banner when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      var existing = getSavedConsent();
      if (!existing) {
        createUI();
      }
    });
  } else {
    var existing = getSavedConsent();
    if (!existing) {
      createUI();
    }
  }

    /* --------------------------------------------------------------------------
     CANONICAL CONVERSION TRACKING (SADECE dataLayer.push - TEK KAYNAK)
     -------------------------------------------------------------------------- */
  if (!window.__fenix_tracking_attached) {
    window.__fenix_tracking_attached = true;

    document.addEventListener('click', function (e) {
      var a = e.target.closest('a');
      if (!a) return;
      var href = a.getAttribute('href') || '';
      if (!href) return;

      if (/wa\.me|whatsapp\.com|api\.whatsapp\.com/i.test(href)) {
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
          event: 'whatsapp_tikla',
          click_url: a.href
        });
      } else if (/^tel:/i.test(href)) {
        var phoneNum = href.replace(/^tel:/i, '').trim();
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
          event: 'telefon_tikla',
          phone_number: phoneNum,
          click_url: a.href
        });
      } else if (/^mailto:/i.test(href)) {
        var email = href.replace(/^mailto:/i, '').split('?')[0].trim();
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
          event: 'eposta_tikla',
          email: email,
          click_url: a.href
        });
      }
    }, true);

    document.addEventListener('submit', function (e) {
      var form = e.target;
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        event: 'form_gonderimi',
        form_id: (form && form.id) || 'contact_form'
      });
    }, true);

    window.addEventListener('calculator_used', function (e) {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push(Object.assign({
        event: 'hesaplayici_kullanildi'
      }, (e && e.detail) || {}));
    });
  }

})();
