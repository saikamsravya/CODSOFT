# SIMPLE CALCULATOR PROGRAM
# FUNCTION FOR ADDITION
def add(a, b):
    return a + b
# FUNCTION FOR SUBTRACTION
def subtract(a, b):
    return a - b
# FUNCTION FOR MULTIPLICATION
def multiply(a, b):
    return a * b
# FUNCTION FOR DIVISION
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b
# MAIN PROGRAM
while True:
    print("\n====== SIMPLE CALCULATOR ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    # USER CHOICE
    choice = input("Enter your choice: ")
    # EXIT
    if choice == "5":
        print("Calculator closed successfully!")
        break
    # VALIDATION
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please try again.")
        continue
    try:
        # INPUT NUMBERS
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        # ADDITION
        if choice == "1":
            result = add(num1, num2)
            print("Result =", result)
        # SUBTRACTION
        elif choice == "2":
            result = subtract(num1, num2)
            print("Result =", result)
        # MULTIPLICATION
        elif choice == "3":
            result = multiply(num1, num2)
            print("Result =", result)
        # DIVISION
        elif choice == "4":
            result = divide(num1, num2)
            print("Result =", result)
    except:
        print("Please enter valid numbers.")