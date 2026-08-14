

// let body= do

// let theme = localStorage.getItem('theme') || 'light

// document.body.classList.add('theme')

// const changeTheme = () =>{
//     theme = Select.value 
//     body.classList.toggle(theme)
//     localStorage.setItem('theme',Selection.value)
// }

// theme.addEventListener('change',changeTheme)

// let pattern = /\d{3}/

// console.log(pattern.test("192"))


// const name = document.getElementById("name")
// const phone = document.getElementById("phone")

// const error = document.getElementById("ifError")

// const PHONE = /^(?:\+251|0)9\d{8}$/;

// function validate(e) {
//     e.preventDefault()
//     if (name.value.trim().length < 2)
//         console.log("Enter your full name.") ;
//     if (!PHONE.test(phone))
//          console.log("Enter a valid phone.");
//     return

// }

// form.addEventListener("submit", validate)

// // const select = document.querySelector("#name", "phone")
// let input = []


// const saved = localStorage.setItem(name, phone)


// Get the form elements
const signupForm = document.getElementById("signupForm");
const nameInput = document.getElementById("name");
const phoneInput = document.getElementById("phone");
const errorArea = document.getElementById("error");
const signupCount = document.getElementById("signupCount");

// Ethiopian phone number regex
// Accepts:
// 0912345678
// 0712345678
// +251912345678
// +251712345678
const ethiopianPhoneRegex = /^(09|07)\d{8}$|^\+251(9|7)\d{8}$/;


// Load existing signups when the page loads
function loadSignups() {

    // Get saved data from localStorage
    const savedData = localStorage.getItem("signups");

    // If there is saved data, convert JSON back to an array
    const signups = savedData ? JSON.parse(savedData) : [];

    // Show number of people who have signed up
    signupCount.textContent =
        `Number of people signed up: ${signups.length}`;
}


// Handle form submission
signupForm.addEventListener("submit", function(event) {

    // Prevent the page from refreshing
    event.preventDefault();

    // Read and trim the input values
    const name = nameInput.value.trim();
    const phone = phoneInput.value.trim();

    // Clear previous error message
    errorArea.textContent = "";

    // Validate name first
    if (name.length < 2) {
        errorArea.textContent =
            "Error: Name must contain at least 2 characters.";
        return;
    }

    // Validate Ethiopian phone number
    if (!ethiopianPhoneRegex.test(phone)) {
        errorArea.textContent =
            "Error: Please enter a valid Ethiopian phone number, such as 0912345678 or +251912345678.";
        return;
    }

    // Get existing signups from localStorage
    const savedData = localStorage.getItem("signups");

    // Convert JSON to JavaScript array
    const signups = savedData ? JSON.parse(savedData) : [];

    // Create the new signup object
    const newSignup = {
        name: name,
        phone: phone
    };

    // Add the new person to the array
    signups.push(newSignup);

    // Convert the array to JSON and save it
    localStorage.setItem("signups", JSON.stringify(signups));

    // Clear the form
    signupForm.reset();

    // Show success message
    errorArea.textContent = "Signup successful!";

    // Update the number of signed-up people
    signupCount.textContent =
        `Number of people signed up: ${signups.length}`;
});


// Run when the page loads
loadSignups();