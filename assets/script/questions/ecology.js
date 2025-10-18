function showHelpText(i) {
  const moreInfoContainer = document.querySelector(`.more-info-container-js-${i}`);
  const container = document.querySelector('.container');

  // blur background
  container.style.filter = 'blur(10px)';

  // show and center the info container
  moreInfoContainer.style.opacity = '1';
  moreInfoContainer.style.visibility = 'visible';
  moreInfoContainer.style.position = 'fixed';
  moreInfoContainer.style.top = '50%';
  moreInfoContainer.style.left = '50%';
  moreInfoContainer.style.width = '80%';
  moreInfoContainer.style.transform = 'translate(-50%, -50%)';
  moreInfoContainer.style.transition = 'all 2s ease';
}

function hideHelpText(i) {
  const moreInfoContainer = document.querySelector(`.more-info-container-js-${i}`);
  const container = document.querySelector('.container');

  // remove blur
  container.style.filter = 'blur(0px)';

  // hide the info container
  moreInfoContainer.style.opacity = '0';
  moreInfoContainer.style.visibility = 'hidden';
  moreInfoContainer.style.top = '-1000px';
}

