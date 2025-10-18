function showPopUp(messageDiv) {
  if (messageDiv.classList.contains('pop-up-1-hidden')) {
    messageDiv.classList.remove('pop-up-1-hidden');
    setTimeout(() => {
      messageDiv.classList.add('pop-up-1-hidden');
      setTimeout(() => {
      messageDiv.style.display = 'none';
    }, 2000);
    }, 5000);
    
  }
}

// On page load, show any Django messages automatically
document.addEventListener('DOMContentLoaded', () => {
  const messages = document.querySelectorAll('.js-django-message');
  messages.forEach(showPopUp);
});
