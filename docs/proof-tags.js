// Small scope explanations work with hover, keyboard focus, and tap.
for (const button of document.querySelectorAll('[data-proof-help]')) {
  const tip = document.getElementById(button.getAttribute('aria-describedby'));
  let pinned = false;
  function show() {
    tip.hidden = false;
    tip.style.left = '0px';
    const bounds = tip.getBoundingClientRect();
    if (bounds.right > window.innerWidth - 16) tip.style.left = `${window.innerWidth - 16 - bounds.right}px`;
    button.setAttribute('aria-expanded', 'true');
  }
  function hide() { tip.hidden = true; button.setAttribute('aria-expanded', 'false'); }
  button.addEventListener('pointerenter', show);
  button.addEventListener('focus', show);
  button.addEventListener('click', () => { pinned = !pinned; if (pinned) show(); else hide(); });
  button.parentElement.addEventListener('pointerleave', () => { if (!pinned && document.activeElement !== button) hide(); });
  button.addEventListener('blur', () => { pinned = false; hide(); });
  button.addEventListener('keydown', event => { if (event.key === 'Escape') { pinned = false; hide(); } });
  document.addEventListener('pointerdown', event => { if (!button.parentElement.contains(event.target)) { pinned = false; hide(); } });
}
