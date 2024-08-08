function selectOrUnselectDate() {
  const byDate = document.querySelector('.by-date-js');
  const byDuration = document.querySelector('.by-duration-js');
  const date = document.querySelector('.date-js');
  const duration = document.querySelector('.duration-js');


  if (byDate.classList.contains('selected')) {
    pass;
  } else {
    byDate.classList.add('selected');
    byDuration.classList.remove('selected');
    date.style.position = 'status';

    date.style.display = 'flex';
    duration.style.display = 'none';
  }
}

function selectOrUnselectDuration() {
  const byDate = document.querySelector('.by-date-js');
  const byDuration = document.querySelector('.by-duration-js');
  const date = document.querySelector('.date-js');
  const duration = document.querySelector('.duration-js');

  if (byDuration.classList.contains('selected')) {
    pass;
  } else {
    byDuration.classList.add('selected');
    byDate.classList.remove('selected');
    date.style.display = 'none';
    duration.style.display = 'flex';
  }
}


const byDate = document.querySelector('.by-date-js');
const byDuration = document.querySelector('.by-duration-js');

byDate.addEventListener('click', selectOrUnselectDate);
byDuration.addEventListener('click', selectOrUnselectDuration);