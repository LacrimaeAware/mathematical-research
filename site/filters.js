const controls = document.querySelector('[data-research-filters]');
const grid = document.querySelector('#research-list');
const count = document.querySelector('#research-count');
const empty = document.querySelector('#research-empty');

if (controls && grid && count && empty) {
  const cards = [...grid.querySelectorAll('[data-research]')];
  const groups = [...controls.querySelectorAll('[data-filter-group]')];
  const valid = Object.fromEntries(groups.map(group => [
    group.dataset.filterGroup,
    new Set([...group.querySelectorAll('button[data-value]')].map(button => button.dataset.value))
  ]));

  function readState() {
    const params = new URLSearchParams(location.search);
    return Object.fromEntries(groups.map(group => {
      const key = group.dataset.filterGroup;
      let value = params.get(key);
      if (key === 'proof') value = ({'lean-partial':'lean',formalized:'lean',idea:'explored',development:'explored'})[value] ?? value;
      return [key, valid[key].has(value) ? value : 'all'];
    }));
  }

  function apply(state) {
    let visible = 0;
    for (const card of cards) {
      const matches = groups.every(group => {
        const key = group.dataset.filterGroup;
        return state[key] === 'all' || card.dataset[key].split(' ').includes(state[key]);
      });
      card.hidden = !matches;
      if (matches) visible++;
    }
    for (const group of groups) {
      for (const button of group.querySelectorAll('button[data-value]')) {
        button.setAttribute('aria-pressed', String(button.dataset.value === state[group.dataset.filterGroup]));
      }
    }
    count.textContent = visible === cards.length
      ? `${visible} research topics`
      : `${visible} of ${cards.length} research topics`;
    empty.hidden = visible !== 0;
  }

  function select(state) {
    const url = new URL(location.href);
    for (const key of Object.keys(valid)) {
      if (state[key] === 'all') url.searchParams.delete(key);
      else url.searchParams.set(key, state[key]);
    }
    if (url.href !== location.href) history.pushState(null, '', url);
    apply(state);
  }

  controls.addEventListener('click', event => {
    const button = event.target.closest('button[data-value]');
    if (!button || !controls.contains(button)) return;
    const key = button.closest('[data-filter-group]').dataset.filterGroup;
    select({...readState(), [key]: button.dataset.value});
  });
  empty.querySelector('button').addEventListener('click', () => {
    select(Object.fromEntries(Object.keys(valid).map(key => [key, 'all'])));
    controls.querySelector('button[data-value="all"]').focus();
  });
  window.addEventListener('popstate', () => apply(readState()));

  apply(readState());
  controls.hidden = false;
}
