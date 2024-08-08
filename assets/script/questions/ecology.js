function showHelpText(i) {
  const moreInfoContainer = document.querySelector(`.more-info-container-js-${i}`);
  const container = document.querySelector('.container');
  container.style.filter = 'blur(6px)';
  moreInfoContainer.style.opacity = "100%";
  moreInfoContainer.style.top = '10%';
};

function hideHelpText(i) {
  const moreInfoContainer = document.querySelector(`.more-info-container-js-${i}`);
  const container = document.querySelector('.container');
  container.style.filter = 'blur(0px)';
  moreInfoContainer.style.opacity = "0%";
  moreInfoContainer.style.top = "-1000px";
  
};


for (var i = 0; i < 20; i++ ) {

  console.log(`more-info-container-js-${i}`)
  const moreInfoContainer = document.querySelector(`.more-info-container-js-${i}`);
  const moreInfo = document.querySelector(`.more-info-js-${i}`);


  // moreInfoContainer.addEventListener('click', hideHelpText(i=i));
  // moreInfo.addEventListener('click', showHelpText(i=i));
};