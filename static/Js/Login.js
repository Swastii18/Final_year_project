function validateForm() {
    var email = document.getElementById('email').value;

    var password = document.getElementById('password').value;

    var emailError = document.querySelector('#register .form-floating:nth-child(1) .error');
    var passwordError = document.querySelector('#register .form-floating:nth-child(2) .error');
   

    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Validate Email
    if (!emailRegex.test(email)) {
      emailError.innerHTML = 'Please enter a valid email address.';
      return false;
    } else {
      emailError.innerHTML = '';
    }
    // Validate Password
    if (password.length < 7 || password.length > 15) {
      passwordError.innerHTML = 'Password must be between 7 and 15 characters.';
      return false;
    } else {
      passwordError.innerHTML = '';
    }
    // If all validations pass, submit the ;form
    return true;
  }

  
  ///togglePassword
const togglePassword = document.querySelector("#togglePassword");
const password = document.querySelector("#password");

togglePassword.addEventListener("click", function () {
// toggle the type attribute
const type = password.getAttribute("type") === "password" ? "text" : "password";
  password.setAttribute("type", type);
  // toggle the icon 
    this.classList.toggle("bi-eye");
  });

   // prevent form submit
 const form = document.querySelector("form");
  form.addEventListener('submit', function (e) {
   e.preventDefault();
  });