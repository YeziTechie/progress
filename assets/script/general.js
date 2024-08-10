function BoxShadowSkirmish() {

  function changeBoxShadow() {
    const element = document.querySelector('.chaotic-box-shadow');  

    const ran1 = '#' + Math.floor(Math.random()*16777215).toString(16);
    const ran2 = '#' + Math.floor(Math.random()*16777215).toString(16);
    const ran3 = '#' + Math.floor(Math.random()*16777215).toString(16);
    const ran4 = '#' + Math.floor(Math.random()*16777215).toString(16);
    const ran5 = '#' + Math.floor(Math.random()*16777215).toString(16);
    const ran6 = '#' + Math.floor(Math.random()*16777215).toString(16);
    const ran7 = '#' + Math.floor(Math.random()*16777215).toString(16);
    const ran8 = '#' + Math.floor(Math.random()*16777215).toString(16);

    let data = `
    0px 0px 2px ${ran1},
    0px 0px 4px ${ran2},
    0px 0px 6px ${ran3},
    0px 0px 10px ${ran4},
    0px 0px 16px ${ran5},
    0px 0px 26px ${ran6},
    0px 0px 42px ${ran7},
    0px 0px 68px ${ran8}
    `;
  
    element.style.boxShadow = data;
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

function borderSkirmish(direction, element) {

  console.log('asdf')

  function returnColor() {
    const color = '#' + Math.floor(Math.random()*16777215).toString(16);
    return color;
  }
  function changeBorder() {
    if (direction === 'top') {
      element.style.borderTop = `solid 1px ${returnColor()}`
    } else if (direction === 'bottom') {
      element.style.borderBottom === `solid 1px ${returnColor()}`
    } else if (direction === 'left') {
      element.style.borderLeft === `solid 1px ${returnColor()}`
    } else if (direction === 'right') {
      element.style.borderRight === `solid 1px ${returnColor()}`
    }
  }
  return setInterval(changeBorder, 2000);
}

bgColorSkirmish();
fontColorSkirmish();
borderSkirmish('bottom', document.querySelector('.tasks'));