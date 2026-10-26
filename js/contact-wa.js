/**
 * fenixyangin.com.tr - İletişim Formu WhatsApp & E-posta Entegrasyonu
 * Form verilerini hiçbir harici sunucuya göndermeden doğrudan kullanıcının
 * WhatsApp veya e-posta uygulamasında hazır mesaj olarak açar.
 */
(function () {
  'use strict';

  var form = document.getElementById('teklif-formu');
  if (!form) return;

  var errorBox = document.getElementById('teklif-error');
  var confPanel = document.getElementById('teklif-confirmation');
  var confTitle = document.getElementById('conf-title');
  var confDesc = document.getElementById('conf-desc');
  var confBtnWa = document.getElementById('conf-btn-wa');
  var confBtnEmail = document.getElementById('conf-btn-email');
  var confBtnNew = document.getElementById('conf-btn-new');
  var fallbackEmailLink = document.getElementById('wa-fallback-email');

  var lastPreparedWaUrl = '';
  var lastPreparedMailtoUrl = '';

  function showError(msg) {
    if (errorBox) {
      errorBox.innerHTML = msg;
      errorBox.classList.remove('fx-hidden');
      errorBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }

  function clearError() {
    if (errorBox) {
      errorBox.innerHTML = '';
      errorBox.classList.add('fx-hidden');
    }
  }

  // Clear errors when interacting with fields
  var inputs = form.querySelectorAll('input, select, textarea');
  for (var i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener('input', function () {
      this.classList.remove('is-error');
      clearError();
    });
    inputs[i].addEventListener('change', function () {
      this.classList.remove('is-error');
      clearError();
    });
  }

  function validate() {
    clearError();

    var adEl = document.getElementById('ad');
    var telEl = document.getElementById('tel');
    var epostaEl = document.getElementById('eposta');
    var mesajEl = document.getElementById('mesaj');
    var kvkkCheck = document.getElementById('kvkk-onay');

    var ad = adEl ? adEl.value.trim() : '';
    var eposta = epostaEl ? epostaEl.value.trim() : '';
    var mesaj = mesajEl ? mesajEl.value.trim() : '';

    if (!ad || ad.length < 2) {
      if (adEl) adEl.classList.add('is-error');
      showError('<strong>Eksik Alan:</strong> Lütfen adınızı ve soyadınızı giriniz.');
      if (adEl) adEl.focus();
      return false;
    }

    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!eposta || !emailRegex.test(eposta)) {
      if (epostaEl) epostaEl.classList.add('is-error');
      showError('<strong>Geçersiz E-posta:</strong> Lütfen geçerli bir e-posta adresi giriniz.');
      if (epostaEl) epostaEl.focus();
      return false;
    }

    if (!mesaj || mesaj.length < 3) {
      if (mesajEl) mesajEl.classList.add('is-error');
      showError('<strong>Eksik Mesaj:</strong> Lütfen talebiniz veya projeniz ile ilgili bir mesaj yazınız.');
      if (mesajEl) mesajEl.focus();
      return false;
    }

    if (kvkkCheck && !kvkkCheck.checked) {
      showError('<strong>Onay Gereklidir:</strong> Formu gönderebilmek için lütfen KVKK Aydınlatma Metni\'ni okuyup onaylayınız.');
      kvkkCheck.focus();
      return false;
    }

    return true;
  }

  function buildMessage() {
    var ad = (document.getElementById('ad') ? document.getElementById('ad').value : '').trim();
    var kurum = (document.getElementById('kurum') ? document.getElementById('kurum').value : '').trim();
    var tel = (document.getElementById('tel') ? document.getElementById('tel').value : '').trim();
    var eposta = (document.getElementById('eposta') ? document.getElementById('eposta').value : '').trim();

    var mahalEl = document.getElementById('mahal');
    var mahalText = (mahalEl && mahalEl.selectedIndex > 0) ? mahalEl.options[mahalEl.selectedIndex].text.trim() : '';

    var sistemEl = document.getElementById('sistem');
    var sistemText = (sistemEl && sistemEl.selectedIndex > 0) ? sistemEl.options[sistemEl.selectedIndex].text.trim() : '';

    var en = (document.getElementById('f-en') ? document.getElementById('f-en').value : '').trim();
    var boy = (document.getElementById('f-boy') ? document.getElementById('f-boy').value : '').trim();
    var yuk = (document.getElementById('f-yuk') ? document.getElementById('f-yuk').value : '').trim();

    var mesaj = (document.getElementById('mesaj') ? document.getElementById('mesaj').value : '').trim();

    var lines = [];
    lines.push('Merhaba Fenix Yangın, web sitenizden yazıyorum.');
    lines.push('');

    if (ad) lines.push('Ad Soyad: ' + ad);
    if (kurum) lines.push('Firma: ' + kurum);
    if (tel) lines.push('Telefon: ' + tel);
    if (eposta) lines.push('E-posta: ' + eposta);
    if (mahalText) lines.push('Mahal tipi: ' + mahalText);
    if (sistemText) lines.push('İstenen sistem: ' + sistemText);

    if (en || boy || yuk) {
      var dimStr = (en || '—') + ' × ' + (boy || '—') + ' × ' + (yuk || '—') + ' m';
      lines.push('Ölçüler: ' + dimStr);
    }

    lines.push('');
    lines.push('Mesaj:');
    lines.push(mesaj);
    lines.push('');
    lines.push('— fenixyangin.com.tr iletişim formu');

    var fullText = lines.join('\n');
    var subject = 'Web sitesi talebi: ' + (mahalText || ad);

    return {
      text: fullText,
      subject: subject
    };
  }

  function showConfirmation(mode, waUrl, mailtoUrl) {
    lastPreparedWaUrl = waUrl;
    lastPreparedMailtoUrl = mailtoUrl;

    if (confBtnEmail) {
      confBtnEmail.href = mailtoUrl;
    }

    if (mode === 'whatsapp') {
      if (confTitle) confTitle.textContent = 'Mesajınız WhatsApp\'ta hazır';
      if (confDesc) confDesc.textContent = 'Göndermek için WhatsApp\'ta Gönder\'e basın. WhatsApp açılmadıysa aşağıdaki seçeneklerden birini kullanın.';
      if (confBtnWa) confBtnWa.style.display = 'inline-flex';
    } else {
      if (confTitle) confTitle.textContent = 'E-postanız hazır';
      if (confDesc) confDesc.textContent = 'Göndermek için e-posta uygulamanızda Gönder\'e basın. E-posta açılmadıysa aşağıdaki seçeneklerden birini kullanın.';
      if (confBtnWa) confBtnWa.style.display = 'none';
    }

    form.style.display = 'none';
    if (confPanel) {
      confPanel.classList.remove('fx-hidden');
      confPanel.style.display = 'block';
      confPanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }

  function triggerOpen(url, isWa) {
    var a = document.createElement('a');
    a.href = url;
    if (isWa) {
      a.target = '_blank';
      a.rel = 'noopener';
    }
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }

  // Form submit -> WhatsApp flow
  form.addEventListener('submit', function (e) {
    e.preventDefault();

    if (!validate()) {
      return;
    }

    var msgData = buildMessage();
    var waUrl = 'https://wa.me/905327409097?text=' + encodeURIComponent(msgData.text);
    var mailtoUrl = 'mailto:info@fenixyangin.com.tr?subject=' + encodeURIComponent(msgData.subject) + '&body=' + encodeURIComponent(msgData.text);

    // Synchronously open WhatsApp link (real anchor click triggers existing consent.js click listener)
    triggerOpen(waUrl, true);

    // Push generate_lead event
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: 'generate_lead',
      method: 'whatsapp'
    });

    // Show confirmation panel
    showConfirmation('whatsapp', waUrl, mailtoUrl);
  });

  // Re-open WhatsApp button in confirmation panel
  if (confBtnWa) {
    confBtnWa.addEventListener('click', function () {
      if (lastPreparedWaUrl) {
        triggerOpen(lastPreparedWaUrl, true);
      }
    });
  }

  // Fallback: "WhatsApp kullanmıyorum, e-posta ile göndereceğim"
  if (fallbackEmailLink) {
    fallbackEmailLink.addEventListener('click', function (e) {
      e.preventDefault();

      if (!validate()) {
        return;
      }

      var msgData = buildMessage();
      var mailtoUrl = 'mailto:info@fenixyangin.com.tr?subject=' + encodeURIComponent(msgData.subject) + '&body=' + encodeURIComponent(msgData.text);
      var waUrl = 'https://wa.me/905327409097?text=' + encodeURIComponent(msgData.text);

      // Open mailto link
      triggerOpen(mailtoUrl, false);

      // Push generate_lead event for email
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        event: 'generate_lead',
        method: 'email'
      });

      // Show confirmation panel with email title
      showConfirmation('email', waUrl, mailtoUrl);
    });
  }

  // "Yeni mesaj yaz" link -> reset & restore form
  if (confBtnNew) {
    confBtnNew.addEventListener('click', function (e) {
      e.preventDefault();
      form.reset();
      clearError();
      if (confPanel) {
        confPanel.classList.add('fx-hidden');
        confPanel.style.display = 'none';
      }
      form.style.display = 'block';
      form.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });
  }
})();
