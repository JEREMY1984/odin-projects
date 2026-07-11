// 1. Grab our HTML elements
const myButton = document.getElementById("action-btn");
const myHeading = document.getElementById("main-heading");

// 2. Create an array (a list) of status messages
const statusMessages = [
    "Status: Systems Online",
    "Status: Running Diagnostics",
    "Status: Data Pipeline Active",
    "Status: Automation Complete"
];

// Keep track of which message we are currently showing
let messageIndex = 0;

// 3. Set up the button click event
myButton.addEventListener("click", function() {
    // Change the heading text to the current item in our array
    myHeading.textContent = statusMessages[messageIndex];
    myHeading.style.color = "darkviolet";
    
    // Move to the next message index in the list
    messageIndex = messageIndex + 1;
    
    // If we reach the end of the list, loop back to the first message (index 0)
    if (messageIndex >= statusMessages.length) {
        messageIndex = 0;
    }
});