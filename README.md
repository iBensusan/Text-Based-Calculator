# Text-Based Calculator

## Overview

This is a simple command-line text-based calculator written in Python. The program prompts the user to enter mathematical expressions, evaluates them, and displays the results. The calculator continues to accept new expressions until the user types `'exit'` to quit.

## Features

- Supports basic mathematical operations: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- Handles division by zero with an appropriate error message.
- Allows users to input complex mathematical expressions and provides instant evaluation.
- Loops continuously until the user decides to exit the program.

## Code Explanation

### `calculate()` Function

The `calculate()` function is responsible for evaluating the user input (mathematical expression). It uses Python's built-in `eval()` function to compute the result. The function handles the following:

- **Valid expressions**: It returns the result of the evaluated expression.
- **Division by zero**: Catches `ZeroDivisionError` and returns an appropriate error message.
- **Invalid expressions**: Catches any other exceptions and returns a generic error message (`"Error: Invalid expression"`).

### `main()` Function

This is the core of the program. It runs in a loop, prompting the user for input, passing the input to the `calculate()` function, and displaying the result. The loop continues until the user enters `'exit'`.

- **User Input**: The program asks for a mathematical expression.
- **Exit Command**: If the user enters `'exit'`, the program terminates.
- **Expression Evaluation**: The entered expression is passed to the `calculate()` function, which evaluates it and returns the result or an error message.

### `if __name__ == "__main__"` Block

This block ensures that the `main()` function is only executed when the script is run directly, not when it's imported as a module in another script.

## How to Use

1. Clone or download the script.
2. Make sure you have Python installed on your system.
3. Run the script using Python.
4. Enter mathematical expressions like `5 + 3`, `10 * 4`, etc., and press `Enter`.
5. To exit the program, type `'exit'` and press `Enter`.

## Example Usage

Here’s how the program will interact with the user:

- The program will prompt for a mathematical expression.
- After the expression is entered, the result will be displayed.
- If the user enters an invalid expression (e.g., dividing by zero), the program will display an error message.
- The loop will continue until the user types `'exit'`.
