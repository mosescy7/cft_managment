/* CFT Apartments & Shops — shared behaviour */
document.addEventListener('DOMContentLoaded', () => {

  /* Sticky header state */
  const header = document.querySelector('.site-header');
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 40);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* Mobile nav */
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
      toggle.textContent = open ? '✕' : '☰';
    });
    nav.querySelectorAll('a').forEach(a =>
      a.addEventListener('click', () => nav.classList.remove('open')));
  }

  /* Scroll reveal */
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  /* Gallery filters */
  const filterBtns = document.querySelectorAll('.gallery-filters button');
  const items = document.querySelectorAll('.g-item');
  filterBtns.forEach(btn => btn.addEventListener('click', () => {
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const cat = btn.dataset.filter;
    items.forEach(it =>
      it.classList.toggle('hidden', cat !== 'all' && it.dataset.cat !== cat));
  }));

  /* Lightbox */
  const lb = document.querySelector('.lightbox');
  if (lb) {
    const lbImg = lb.querySelector('img');
    const lbCap = lb.querySelector('.lb-caption');
    document.querySelectorAll('[data-lightbox]').forEach(el => {
      el.addEventListener('click', () => {
        const img = el.tagName === 'IMG' ? el : el.querySelector('img');
        lbImg.src = img.src;
        lbImg.alt = img.alt;
        if (lbCap) lbCap.textContent = el.dataset.caption || img.alt || '';
        lb.classList.add('open');
        document.body.style.overflow = 'hidden';
      });
    });
    const close = () => { lb.classList.remove('open'); document.body.style.overflow = ''; };
    lb.querySelector('.lb-close').addEventListener('click', close);
    lb.addEventListener('click', e => { if (e.target === lb) close(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  }

  /* Inquiry / booking forms */
  document.querySelectorAll('form[data-inquiry]').forEach(form => {
    form.addEventListener('submit', e => {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      const fields = form.querySelectorAll('input,select,textarea,button');
      fields.forEach(el => el.disabled = true);
      const ok = form.parentElement.querySelector('.form-success');
      const err = form.parentElement.querySelector('.form-error');
      if (err) err.classList.remove('visible');

      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { 'Accept': 'application/json' }
      }).then(res => {
        if (res.ok) {
          if (ok) { ok.classList.add('visible'); ok.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
        } else {
          throw new Error('Submission failed');
        }
      }).catch(() => {
        fields.forEach(el => el.disabled = false);
        if (err) { err.classList.add('visible'); err.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
      });
    });
  });

  /* Set min dates for date inputs */
  const today = new Date().toISOString().split('T')[0];
  document.querySelectorAll('input[type="date"]').forEach(d => d.min = today);

  /* Footer year */
  document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
});
