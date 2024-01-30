function validateForm() {
  var email = document.getElementById('email').value;
  var name = document.getElementById('fname').value;
  var password = document.getElementById('password').value;
  var confirmPassword = document.getElementById('password2').value;

  var nameError = document.querySelector('#register .form-floating:nth-child(1) .error');
  var emailError = document.querySelector('#register .form-floating:nth-child(2) .error');
  var passwordError = document.querySelector('#register .form-floating:nth-child(3) .error');
  var confirmPasswordError = document.querySelector('#register .form-floating:nth-child(4) .error');

  var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  var nameRegex = /^[A-Za-z]+(?: [A-Za-z]+)?$/;
  // Validate Name
  if(name ===""){
    nameError.innerHTML = 'Please enter fullname.';
  }
  else if (!nameRegex.test(name)) {
    nameError.innerHTML = 'Please enter a valid name.';
    return false;
  } else {
    nameError.innerHTML = '';
  }

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

  // Validate Confirm Password
  if (confirmPassword !== password) {
    confirmPasswordError.innerHTML = 'Passwords do not match.';
    return false;
  } else {
    confirmPasswordError.innerHTML = '';
  }
 
  // If all validations pass, submit the ;form

 window.location.href = 'Pages/LoginPage/signIn.html'; // Update the URL accordingly

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