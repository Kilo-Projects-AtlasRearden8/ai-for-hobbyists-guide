// AI for Hobbyists — site behavior
// Credit: Asdale Dynamics, LLC (Indiana, formed October 2026)

(function () {
  var toggle = document.querySelector('.menu-toggle');
  var menu = document.getElementById('nav-menu');

  if (!toggle || !menu) return;

  toggle.addEventListener('click', function () {
    var open = menu.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Close menu when a link is tapped
  var links = menu.querySelectorAll('a');
  links.forEach(function (link) {
    link.addEventListener('click', function () {
      menu.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
})();
