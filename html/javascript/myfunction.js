// Define a function to multiply two numbers and display the result
function multiplyBy() {
    // Get the values of the input fields with the ids "firstNumber" and "secondNumber"
    num1 = document.getElementById("firstNumber").value;
    num2 = document.getElementById("secondNumber").value;

    // Set the inner HTML of the element with the id "result" to the product of the two numbers
    document.getElementById("result").innerHTML = num1 * num2;
}

// Define a function to divide two numbers and display the result
function divideBy() {
    // Get the values of the input fields with the ids "firstNumber" and "secondNumber"
    num1 = document.getElementById("firstNumber").value;
    num2 = document.getElementById("secondNumber").value;

    // Set the inner HTML of the element with the id "result" to the quotient of the two numbers
    document.getElementById("result").innerHTML = num1 / num2;
}

// Define a function to add two numbers and display the result
function addBy() {
    num1 = document.getElementById("firstNumber").value;
    num2 = document.getElementById("secondNumber").value;

    // Corrected sum calculation
    const sum = parseFloat(num1) + parseFloat(num2);  // Use parseFloat to ensure correct addition
    document.getElementById("result").innerHTML = sum;
}

// Define a function to subtract two numbers and display the result
function subtract() {
    num1 = document.getElementById("firstNumber").value;
    num2 = document.getElementById("secondNumber").value;

    // Corrected subtraction calculation
    const difference = parseFloat(num1) - parseFloat(num2);  // Use parseFloat to ensure correct subtraction
    document.getElementById("result").innerHTML = difference;
}
