const navbar = document.getElementById('navbar');
const toggleBtn = document.getElementById('toggle-btn');

toggleBtn.addEventListener('click', () => {
  navbar.classList.toggle('open');

  if (navbar.classList.contains('open')) {
    navBtnOpen();
  } else {
    resetNavBtn(); // <— reset shapes when closing
  }
});

function navBtnOpen() {
  const a = document.querySelector(".v-l-1");
  const b = document.querySelector(".h-l-1");
  const c = document.querySelector(".h-l-2");
  const d = document.querySelector(".c-1");
  const e = document.querySelector(".l-l");
  const f = document.querySelector(".square");
  const g = document.querySelector(".r-l");
  const h = document.querySelector(".c-2");
  const i = document.querySelector(".second-v-l-1");
  const j = document.querySelector(".second-v-l-2");
  const k = document.querySelector(".second-v-l-3");
  const l = document.querySelector(".second-h-l-1");

  d.style.borderRadius = '0';
  h.style.borderRadius = '0';
  d.style.transform = 'rotate(315deg) scale(2, 2)';
  h.style.transform = 'rotate(-315deg) scale(2, 2)';

  f.style.transform = 'scale(0.9, 0.9)';
  f.style.borderRadius = '50%';

  b.style.transform = 'translate(0px, 5px) scale(3, 1)';
  c.style.transform = 'translate(0px, -5px) scale(3, 1)';
  // c.style.backgroundColor = 'var(--theme-color)';

  j.style.transform = 'translate(21px, 0px)';
  // j.style.backgroundColor = 'rgb(55,0,105)';
  k.style.transform = 'translate(-21px, 0px)';
  // k.style.backgroundColor = 'rgb(55,0,105)';

  l.style.transform = 'rotate(90deg) translate(0px, 0px)';
  // l.style.backgroundColor = 'rgb(55,0,105)';

  i.style.backgroundColor = 'transparent';
}

function resetNavBtn() {
  const elements = document.querySelectorAll(
    ".v-l-1, .h-l-1, .h-l-2, .c-1, .l-l, .square, .r-l, .c-2, .second-v-l-1, .second-v-l-2, .second-v-l-3, .second-h-l-1"
  );

  elements.forEach(el => {
    el.removeAttribute('style');
  });
}
