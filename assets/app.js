(() => {
  const wikiButtons = [...document.querySelectorAll('[data-wiki-target]')];
  const wikiEntries = [...document.querySelectorAll('[data-wiki-entry]')];

  function openWiki(id) {
    wikiButtons.forEach((button) => button.classList.toggle('active', button.dataset.wikiTarget === id));
    wikiEntries.forEach((entry) => entry.classList.toggle('active', entry.dataset.wikiEntry === id));
    const active = wikiButtons.find((button) => button.dataset.wikiTarget === id);
    if (active) active.setAttribute('aria-selected', 'true');
    wikiButtons.filter((button) => button !== active).forEach((button) => button.setAttribute('aria-selected', 'false'));
  }

  wikiButtons.forEach((button) => button.addEventListener('click', () => openWiki(button.dataset.wikiTarget)));

  const slides = [...document.querySelectorAll('.slide')];
  if (!slides.length) return;

  const counter = document.querySelector('.deck-counter');
  const bar = document.querySelector('.progress span');
  const prev = document.querySelector('[data-prev]');
  const next = document.querySelector('[data-next]');
  let index = Math.max(0, Math.min(slides.length - 1, Number(location.hash.replace('#', '')) - 1 || 0));

  function showSlide(nextIndex) {
    index = (nextIndex + slides.length) % slides.length;
    slides.forEach((slide, i) => slide.classList.toggle('active', i === index));
    counter.textContent = `${String(index + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
    bar.style.width = `${((index + 1) / slides.length) * 100}%`;
    history.replaceState(null, '', `#${index + 1}`);
  }

  function revealOrAdvance() {
    const hidden = slides[index].querySelector('.reveal:not(.shown)');
    if (hidden) hidden.classList.add('shown');
    else showSlide(index + 1);
  }

  prev.addEventListener('click', () => showSlide(index - 1));
  next.addEventListener('click', revealOrAdvance);
  document.addEventListener('keydown', (event) => {
    if (['ArrowRight', 'PageDown', ' '].includes(event.key)) { event.preventDefault(); revealOrAdvance(); }
    if (['ArrowLeft', 'PageUp'].includes(event.key)) { event.preventDefault(); showSlide(index - 1); }
    if (event.key === 'Home') showSlide(0);
    if (event.key === 'End') showSlide(slides.length - 1);
  });
  showSlide(index);
})();
