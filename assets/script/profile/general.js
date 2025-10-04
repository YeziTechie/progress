
function borderSkirmish(direction, element) {
  function returnColor() {
    const color = '#' + Math.floor(Math.random()*16777215).toString(16);
    return color
  }
  function changeBorder () {
    if (direction == 'top') {
      element.style.borderTop = `solid 1px ${returnColor()}`;
    } else if (direction == 'bottom') {
      element.style.borderBottom = `solid 1px ${returnColor()}`;
    } else if (direction == 'right') {
      element.style.borderRight = `solid 1px ${returnColor()}`;
    } else if (direction == 'left') {
      element.style.borderLeft = `solid 1px ${returnColor()}`;
    } else if (direction == 'all') {
      element.style.border = `solid 1px ${returnColor()}`;
    }
  }

  return setInterval(changeBorder, 2000);
}

// const tasks = document.querySelectorAll('.task').forEach(element => {
//   borderSkirmish('all', element);
// })

// const outcomes = document.querySelectorAll('.outcome-name').forEach(element => borderSkirmish('right', element));

const level = document.querySelector('level');
borderSkirmish('all', level);


function BoxShadowSkirmish() {

  function changeBoxShadow() {
    const element = document.querySelectorAll('.chaotic-box-shadow');  

    const ran1 = '#' + Math.floor(Math.random()*16777215).toString(16);
    const ran4 = '#' + Math.floor(Math.random()*16777215).toString(16);
    const ran8 = '#' + Math.floor(Math.random()*16777215).toString(16);

    let data = `
    0px 0px 2px ${ran1},
    0px 0px 10px ${ran4},
    0px 0px 68px ${ran8}
    `;
  
    element.forEach(elem => {elem.style.boxShadow = data;})
  };

  return setInterval(changeBoxShadow, 500);

};

function fontColorSkirmish() {
  function returnColor() {
    const color = '#' + Math.floor(Math.random()*16777215).toString(16);
    return color
  }
  function changeFontColor() {
    const element = document.querySelectorAll('.chaotic-font-color');  
    element.forEach(value => value.style.color = returnColor())
  }

  return setInterval(changeFontColor, 2000);
};

function bgColorSkirmish() {
  function returnColor() {
    const color = '#' + Math.floor(Math.random()*16777215).toString(16);
    return color;
  }
  function changeBGColor() {
    const element = document.querySelectorAll('.chaotic-bg-color');  
    element.forEach(value => value.style.backgroundColor = returnColor());
  }
  
  return setInterval(changeBGColor, 2000);
};

function addHoverClass(event) {
  event.target.classList.add('chaotic-box-shadow');
  intervalNum = BoxShadowSkirmish()
 };

function removeHoverClass(event) {
  event.target.classList.remove('chaotic-box-shadow');
  event.target.style.boxShadow = '';
  clearInterval(intervalNum)
};

// document.querySelectorAll('.task').forEach(element => {
//   element.addEventListener('mouseenter', addHoverClass);
//   element.addEventListener('mouseleave', removeHoverClass);
// });

// document.querySelectorAll('.outcome').forEach(element => {
//   element.addEventListener('mouseenter', addHoverClass);
//   element.addEventListener('mouseleave', removeHoverClass);
// });


fontColorSkirmish();
bgColorSkirmish();
