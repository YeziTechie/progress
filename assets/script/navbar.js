let expanded = false;

function showNavButtons () {
  const navbtn = document.querySelector('.js-navbar-button');

  if (!expanded) {
    expanded = true;
    navbtn.classList.add('navbar-button-clicked');

    showProfileButton();
    showTasksButton();
    showOutcomesButton();
  } else {
    expanded = false;
    navbtn.classList.remove('navbar-button-clicked');

    hideProfileButton();
    hideTasksButton();
    hideOutcomesButton();
  };
};

function showNavText (px, opa) {

  const navTexts = document.querySelectorAll('.navbar-text')
  navTexts.forEach(text => {
    text.style.fontSize = px;
    // text.style.opacity = opa;
  });
};

function showProfileButton() {
  const element = document.querySelector('.js-navbar-profile');

  let i = 1;
  let b = 1;

  function updateProfileElement() {
    if (b > 80) {
      showNavText('20px', '100%');
    }

    if (i <= 60) {
      element.style.top = `${i}px`;
      element.style.left = `${i}px`;

      if (i < 12) {
        i += 3
      } else if   (i < 24) {
        i += 2
      } else if (i < 36) {
        i += 1.5
      } else if (i < 48) {
        i += 1
      } else if (i <= 60) {
        i += 0.5
      }
      
      console.log(i)

    }

    if (b <= 90) {
      element.style.width = `${b}px`;
      element.style.height = `${b}px`;

      if (b < 18) {
        b += 3
      } else if   (b < 36) {
        b += 2
      } else if (b < 54) {
        b += 1.5
      } else if (b < 72) {
        b += 1
      } else if (b<= 90) {
        b += 0.5
      }
    }
    if (i <= 60 || b <= 90) {
      requestAnimationFrame(updateProfileElement);
    }
  }
  requestAnimationFrame(updateProfileElement);
};

function hideProfileButton() {
  const element = document.querySelector('.js-navbar-profile');

  let i = 60;
  let b = 90;

  function shrinkProfileElement() {
    if (b < 90) {
      showNavText('0px', '0%');
    } 

    if (i > 0) {
      element.style.top = `${i}px`;
      element.style.left = `${i}px`;

      if (i > 48) {
        i -= 3;
      } else if (i > 36) {
        i -= 2;
      } else if (i > 24) {
        i -= 1.5;
      } else if (i > 12) {
        i -= 1;
      } else if (i > 0) {
        i -= 0.5;
      }
    }

    if (b > 0) {
      element.style.width = `${b}px`;
      element.style.height = `${b}px`;

      if (b > 72) {
        b -= 4;
      } else if (b > 54) {
        b -= 3;
      } else if (b > 36) {
        b -= 2;
      } else if (b > 18) {
        b -= 1.5;
      } else if (b > 0) {
        b -= 1;
      }
    }

    if (i > 0 || b > 0) {
      requestAnimationFrame(shrinkProfileElement);
    }
  }
  requestAnimationFrame(shrinkProfileElement);
};

function showTasksButton() {
  const element = document.querySelector('.js-navbar-tasks');
  let top = 0;
  let left = 0;
  let b = 0;

  function updateTasksElement() {
    if (top >= 0 && top <= 10) {
      element.style.top = `${top}px`;
      top = top + 1;
    }

    if (left <= 180) {
      element.style.left = `${left}px`;

      if (left < 36) {
        left += 4
      } else if   (left < 72) {
        left += 3
      } else if (left < 108) {
        left += 2
      } else if (left < 148) {
        left += 2
      } else if (left <= 180) {
        left += 1
      }

    }

    if (b <= 100) {
      element.style.width = `${b}px`;
      element.style.height = `${b}px`;

      if (b < 20) {
        b += 3
      } else if   (b < 40) {
        b += 2
      } else if (b < 60) {
        b += 1.5
      } else if (b < 80) {
        b += 1
      } else if (b <= 100) {
        b += 0.5
      }
    }

    if (left <= 180 || top <= 10 || b <= 100) {
      requestAnimationFrame(updateTasksElement);
    }
  }
  requestAnimationFrame(updateTasksElement);
};

function hideTasksButton() {
  const element = document.querySelector('.js-navbar-tasks');
  let top = 10;
  let left = 180;
  let b = 100;

  function shrinkTasksElement() {
    if (top > 0) {
      element.style.top = `${top}px`;
      top -= 1;
    }

    if (left > 0) {
      element.style.left = `${left}px`;

      if (left <= 180) {
        left -= 4;
      } else if (left < 148) {
        left -= 3;
      } else if (left < 108) {
        left -= 2;
      } else if (left < 72) {
        left -= 2;
      } else if (left <= 36) {
        left -= 1;
      }
    }

    if (b > 0) {
      element.style.width = `${b}px`;
      element.style.height = `${b}px`;

      if (b <= 100) {
        b -= 2;
      } else if   (b < 80) {
        b -= 1.8;
      } else if (b < 60) {
        b -= 1.5;
      } else if (b < 40) {
        b -= 1;
      } else if (b<= 20) {
        b -= 0.5;
      }
    }

    if (left > 0 || top > 0 || b > 0) {
      requestAnimationFrame(shrinkTasksElement);
    }
  }
  requestAnimationFrame(shrinkTasksElement);
};

function showOutcomesButton() {
  const element = document.querySelector('.js-navbar-outcomes');
  let top = 0;
  let left = 0;
  let b = 0;

  function updateOutcomesElement() {
    if (top <= 180) {
      element.style.top = `${top}px`;
      if (top < 36) {
        top += 4
      } else if   (top < 72) {
        top += 3
      } else if (top < 108) {
        top += 2
      } else if (top < 148) {
        top += 2
      } else if (top <= 180) {
        top += 1
      }
    }

    if (left <= 10) {
      element.style.left = `${left}px`;
      left ++;
    }

    if (b <= 100) {
      element.style.width = `${b}px`;
      element.style.height = `${b}px`;
      b = b + 1.8;
    }

    if (left <= 180 || top <= 10 || b <= 100) {
      requestAnimationFrame(updateOutcomesElement);
    }
  }
  requestAnimationFrame(updateOutcomesElement);
};

function hideOutcomesButton() {
  const element = document.querySelector('.js-navbar-outcomes');

  let left = 180;
  let top = 10;
  let b = 100;

  function shrinkTasksElement() {
    if (top > 0) {
      element.style.left = `${top}px`;
      top -= 1;
    }

    if (left > 0) {
      element.style.top = `${left}px`;

      if (left <= 180) {
        left -= 4;
      } else if (left < 148) {
        left -= 3;
      } else if (left < 108) {
        left -= 2;
      } else if (left < 72) {
        left -= 2;
      } else if (left <= 36) {
        left -= 1;
      }
    }

    if (b > 0) {
      element.style.width = `${b}px`;
      element.style.height = `${b}px`;

      if (b <= 100) {
        b -= 2;
      } else if   (b < 80) {
        b -= 1.8;
      } else if (b < 60) {
        b -= 1.5;
      } else if (b < 40) {
        b -= 1;
      } else if (b<= 20) {
        b -= 0.5;
      }
    }

    if (left > 0 || top > 0 || b > 0) {
      requestAnimationFrame(shrinkTasksElement);
    }
  }
  requestAnimationFrame(shrinkTasksElement);
};


document.querySelector('.js-navbar-button').addEventListener('click', showNavButtons);

