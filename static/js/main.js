const header = document.querySelector('.nav-links');
let condition = false;

const toggleNavbar = () => {
  if (condition) {
    header.classList.toggle('translate-x-[-100%]', false);
    condition = true;
  } else {
    header.classList.toggle('translate-x-[-100%]');
    condition = false;
  }
}