//Get reference to the form and its input fields
const form = document.querySelector('form');
const usernameInput = document.getElementById('uname');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');

//Regular expressions for validation
const usernameRegex = /^[a-zA-Z0-9_]{5,20}$/;
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^\da-zA-Z]).{12,}$/;

//Function to validate form data
function validateForm(event){
    event.preventDefault(); //Prevent form submission

    //Validate username
    if (!usernameRegex.test(usernameInput.value)){
        alert('Please enter a valid username (alphanumeric and underscores only)');
        return;
    }

    //Check email
    if (!emailRegex.test(emailInput.value)){
        alert('Please enter a valid email address');
        return;
    }

    //Check password
    if (!passwordRegex.test(passwordInput.value)){
        alert('Please enter a valid password (12 characters minimum, lowercase, uppercase, digit, and symbol)');
        return;
    }

    //Submit form if all validations pass
    alert('Form submitted successfully!');
    form.submit();
}



//Attatch the validateForm function to the form's submit event
form.addEventListener('submit', validateForm);