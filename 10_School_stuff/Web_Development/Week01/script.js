const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  let first_name = document.getElementById("first_name").value;
  let last_name = document.getElementById("last_name").value;

  localStorage.setItem("first_name", first_name);
  localStorage.setItem("last_name", last_name);

  window.location.href = 'index.html';
});
