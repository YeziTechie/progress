document.getElementById('next-btn').addEventListener('click', () => {
  const passwords = document.getElementById('passwords');
  const overlay = document.querySelector('.overlay');

  overlay.style.display = 'block';
  passwords.style.display = 'block';

  setTimeout(() => {
    overlay.style.backgroundColor = 'black';
    passwords.style.opacity = '1';
    passwords.style.border = '1px solid var(--theme-color)';
  }, 1);

});

document.querySelector('.back-btn').addEventListener('click', () => {
  const passwords = document.getElementById('passwords');
  const overlay = document.querySelector('.overlay');

  overlay.style.backgroundColor = 'transparent';
  passwords.style.opacity = '0';
  passwords.style.border = '1px solid transparent';

  setTimeout(() => {
    overlay.style.display = 'none';
    passwords.style.display = 'none';
  }, 1000);

});

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".desc-container").forEach(container => {
    if (container.querySelector(".error-msg")) {
      const input = container.querySelector("input, select, textarea");
      if (input) {
        input.style.borderBottom = "1px solid red";
      }
    }
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const usernameInput = document.querySelector("#id_username");

  if (!usernameInput) return;

  usernameInput.addEventListener("input", () => {
    const value = usernameInput.value.trim();
    const valid = /^[A-Za-z0-9-_]+$/.test(value) && value.length >= 3;
    usernameInput.style.transition = "border-color 0.3s ease, border-bottom-color 0.3s ease";


  if (value === "") {
    usernameInput.style.borderBottomColor = "";
  } else if (valid) {
    usernameInput.style.borderBottomColor = "#00cc66"; // green
  } else {
    usernameInput.style.borderBottomColor = "red"; // red
  }
  });
});