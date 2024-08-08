function showHelpText() {
  const moreInfoContainer = document.querySelector('.more-info-container-js');
  const container = document.querySelector('.container');
  container.style.filter = 'blur(6px)';
  moreInfoContainer.style.opacity = "100%";
  moreInfoContainer.style.top = '40%';
};

function hideHelpText() {
  const moreInfoContainer = document.querySelector('.more-info-container-js');
  const container = document.querySelector('.container');
  container.style.filter = 'blur(0px)';
  moreInfoContainer.style.opacity = "0%";
  moreInfoContainer.style.top = "-1000px";
};

const moreInfo = document.querySelector('.more-info-js');
const moreInfoContainer = document.querySelector('.more-info-container-js');

moreInfo.addEventListener('click', showHelpText);
moreInfoContainer.addEventListener('click', hideHelpText);

