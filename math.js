/* KaTeX remains optional: readable source is retained if the CDN is unavailable. */
if (typeof renderMathInElement === 'function') {
  renderMathInElement(document.getElementById('main'), {
    delimiters: [
      { left: '$$', right: '$$', display: true },
      { left: '$', right: '$', display: false }
    ],
    throwOnError: false
  });
  document.querySelectorAll('.katex-display').forEach(function (formula) {
    formula.tabIndex = 0;
    formula.setAttribute('role', 'region');
    formula.setAttribute('aria-label', document.documentElement.lang === 'es'
      ? 'Fórmula matemática; desplazamiento horizontal disponible'
      : 'Mathematical formula; horizontal scrolling available');
  });
}
