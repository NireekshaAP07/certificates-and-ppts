# Basic Calculator with Error Handling

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def power(a, b):
    return a ** b


while True:
    print("\n===== BASIC CALCULATOR =====")
    print("1. Perform Calculation")
    print("2. Exit")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            print("\nAvailable Operations:")
            print("+  Addition")
            print("-  Subtraction")
            print("*  Multiplication")
            print("/  Division")
            print("^  Power")

            operation = input("Enter operation: ")

            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            elif operation == "/":
                result = divide(num1, num2)
            elif operation == "^":
                result = power(num1, num2)
            else:
                print("Error: Invalid operation!")
                continue

            print("Result =", result)

        except ValueError:
            print("Error: Please enter valid numeric values.")

        except ZeroDivisionError as e:
            print("Error:", e)

    elif choice == "2":
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid choice! Please enter 1 or 2.")