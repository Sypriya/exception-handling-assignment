

### 1. Exception Propagation Across Multiple Functions


def level3():
    # This error will propagate up if not handled
    raise ValueError("Error occurred in level3")

def level2():
    level3()

def level1():
    try:
        level2()
    except ValueError as e:
        print("Caught exception in level1:", e)

level1()


### 2. Exception Chaining (`raise ... from ...`)


try:
    x = int("abc")  # ValueError
except ValueError as e:
    raise RuntimeError("Failed to convert string to int") from e

### 3. Simulating Database Connection with Custom Exceptions

class DatabaseError(Exception):
    pass

class ConnectionError(DatabaseError):
    pass

def connect_to_database():
    connected = False
    if not connected:
        raise ConnectionError("Failed to connect to the database")

try:
    connect_to_database()
except ConnectionError as e:
    print("Database Connection Error:", e)

### 4. File Reading with `with` and Error Handling

try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except IOError as e:
    print("I/O error:", e)

### 5. Skipping Bad Data Rows in CSV

import csv

with open("sample.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            value = int(row[1])  # assume second column should be int
            print("Processed:", row)
        except (IndexError, ValueError):
            print("Skipping bad row:", row)


### 6. Handle Timeout Error (Requests)


import requests

try:
    response = requests.get("https://httpbin.org/delay/5", timeout=2)
    print(response.text)
except requests.exceptions.Timeout:
    print("Request timed out.")


### 7. Exception Handling in Recursive Factorial

def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

try:
    print(factorial(5))
    print(factorial(-3))  # raises exception
except ValueError as e:
    print("Error:", e)

### 8. Simulating Transaction Rollback in Banking


class TransactionError(Exception):
    pass

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise TransactionError("Insufficient funds")
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

# simulate
account = BankAccount(100)
try:
    account.withdraw(150)
except TransactionError as e:
    print("Transaction failed:", e)
    print("Rolling back transaction... Balance:", account.balance)

### 9. Validate Credit Card Numbers


class InvalidCardError(Exception):
    pass

def validate_card(number):
    if not number.isdigit() or len(number) not in (13, 15, 16):
        raise InvalidCardError("Invalid credit card number format")
    print("Valid card number")

try:
    validate_card("1234abcd5678")
except InvalidCardError as e:
    print("Validation failed:", e)


### 10. Raise Exception on High Memory Usage

import psutil

class MemoryLimitExceeded(Exception):
    pass

def check_memory(threshold_mb):
    memory = psutil.virtual_memory()
    used_mb = memory.used / (1024 * 1024)
    if used_mb > threshold_mb:
        raise MemoryLimitExceeded(f"Memory usage exceeded: {used_mb:.2f} MB")
    print(f"Memory usage is safe: {used_mb:.2f} MB")

try:
    check_memory(200)  # set low threshold for testing
except MemoryLimitExceeded as e:
    print("Error:", e)
