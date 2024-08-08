function selectTasks(taskType) {
  const selected = document.querySelector('.task-selected');
  const btn = document.querySelector(`.${taskType}-btn-js`);
  const taskContainer = document.querySelector(`.${taskType}-container-js`);

  if (selected) {
    selected.classList.remove('task-selected');
    const task = selected.classList[0];
    const prevTaskContainer = document.querySelector(`.${task}-container-js`);

    prevTaskContainer.style.opacity = '0';
    prevTaskContainer.style.display = 'none';
  }

  btn.classList.add('task-selected');
  taskContainer.style.display = 'flex';
  taskContainer.style.opacity = '100%';
}

function selectQuestions(number) {
  const selected = document.querySelector('.question-selected');
  const btn = document.querySelector(`.btn-${number}-js`);
  const questionContainer = document.querySelector(`.js-${number}`);

  if (selected) {
    selected.classList.remove('question-selected');
    const num = selected.classList[0][4];
    const prevQuestionContainer = document.querySelector(`.js-${num}`);
    prevQuestionContainer.style.opacity = '0';
    prevQuestionContainer.style.display = 'none';
  }

  btn.classList.add('question-selected');
  questionContainer.style.display = 'block';
  questionContainer.style.opacity = '100%';
}

function openQuestion (element) {
  const line = element.querySelector('.line');
  const answer = element.querySelector('.answer');

  if (line.style.height === '20px') {
    line.style.height = '3px';
    answer.style.fontSize = '1px';
  } else {
    line.style.height = '20px';
    answer.style.fontSize = '14px';
  }

}

const btn1 = document.querySelector('.btn-1-js');
const btn2 = document.querySelector('.btn-2-js');
const btn3 = document.querySelector('.btn-3-js');
const questions = document.querySelectorAll('.question');

const classicTaskBtn = document.querySelector('.classic-btn-js');
const timeTaskBtn = document.querySelector('.time-btn-js');
const countTaskBtn = document.querySelector('.count-btn-js');
const deadlineTaskBtn = document.querySelector('.deadline-btn-js');

questions.forEach(element => {
  element.addEventListener('click', () => openQuestion(element));
});

btn1.addEventListener('click', () => selectQuestions(1));
btn2.addEventListener('click', () => selectQuestions(2));
btn3.addEventListener('click', () => selectQuestions(3));

classicTaskBtn.addEventListener('click', () => selectTasks('classic'));
timeTaskBtn.addEventListener('click', () => selectTasks('time'));
countTaskBtn.addEventListener('click', () => selectTasks('count'));
deadlineTaskBtn.addEventListener('click', () => selectTasks('deadline'));



