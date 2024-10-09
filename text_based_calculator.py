# Text-Based Calculator

def calculate(expression):
    try:
        # Evaluate the mathematical expression
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception:
        return "Error: Invalid expression."

def main():
    print("Text-Based Calculator")
    print("Enter a mathematical expression (e.g. 3 + 3) or type 'exit' to quit.")
    
    while True:
        # Prompt the user to enter a mathematical expression
        expression = input("Enter expression: ")
        
        # If the user types 'exit', the program terminates
        if expression.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        # Call the calculate function and display the result
        result = calculate(expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
