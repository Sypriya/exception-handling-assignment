# 1. Withdraw money and raise exception if balance < withdrawal
def withdraw(balance, amount):
    if amount > balance:
        raise Exception("Insufficient Balance!")
    return balance - amount

# 2. Validate age and raise exception if age < 18
def validate_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    return True

# 3. Validate email format and raise a custom exception
import re
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise InvalidEmailError("Invalid email format")
    return True

# 4. Custom exception NegativeNumberError in square root function
import math
class NegativeNumberError(Exception):
    pass

def safe_sqrt(number):
    if number < 0:
        raise NegativeNumberError("Cannot calculate square root of negative number")
    return math.sqrt(number)

# 5. Custom exception for InsufficientFundsError in banking system
class InsufficientFundsError(Exception):
    pass

def banking_withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough funds to withdraw")
    return balance - amount

# 6. Handle exceptions while parsing JSON
import json
def parse_json(data):
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        print("Invalid JSON:", e)

# 7. Retry dividing two numbers 3 times if error occurs
def safe_divide(a, b):
    attempts = 0
    while attempts < 3:
        try:
            return a / b
        except ZeroDivisionError:
            attempts += 1
            print(f"Attempt {attempts}: Division by zero error")
            b = int(input("Enter a non-zero divisor: "))
    raise Exception("Failed after 3 attempts")

# 8. Assert to validate positive numbers and handle AssertionError
def check_positive(number):
    try:
        assert number > 0, "Number must be positive"
        print("Valid positive number:", number)
    except AssertionError as e:
        print("AssertionError:", e)

# 9. Log exceptions to a file using logging module
import logging
logging.basicConfig(filename="errors.log", level=logging.ERROR)

def divide_and_log(a, b):
    try:
        return a / b
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        print("Error logged to file")

# 10. Raise multiple custom exceptions
class InvalidPasswordError(Exception):
    pass

class InvalidUsernameError(Exception):
    pass

def login(username, password):
    if username != "admin":
        raise InvalidUsernameError("Invalid Username")
    if password != "12345":
        raise InvalidPasswordError("Invalid Password")
    return "Login successful"
