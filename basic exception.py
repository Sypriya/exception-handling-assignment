# 1. Handle division by zero
try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 2. Handle invalid user input (string instead of number)
try:
    num = int(input("Enter a number: "))
    print(f"You entered {num}")
except ValueError:
    print("Invalid input! Please enter a number.")

# 3. Catch IndexError when accessing a list element
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Error: Index out of range.")

# 4. Open a file and handle FileNotFoundError
try:
    with open("nonexistent.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("Error: File not found.")

# 5. Handle multiple exceptions (ZeroDivisionError, ValueError)
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")

# 6. try-except-else to check if a number is even
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

# 7. finally block to always display message
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print("Result:", x / y)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Execution Completed.")

# 8. Nested try-except blocks
try:
    num1 = int(input("Enter a number: "))
    try:
        result = num1 / int(input("Enter another number: "))
        print("Result:", result)
    except ZeroDivisionError:
        print("Inner Error: Cannot divide by zero.")
except ValueError:
    print("Outer Error: Invalid input, please enter a number.")

# 9. Ask for two numbers and handle division + conversion errors
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ValueError:
    print("Error: Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("Error: Division by zero is not possible.")

# 10. Raise and handle a TypeError
try:
    raise TypeError("This is a manually raised TypeError.")
except TypeError as e:
    print("Caught exception:", e)
