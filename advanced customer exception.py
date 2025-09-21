
### 1. Banking Custom Exception Hierarchy

class BankError(Exception):
    pass

class InsufficientFunds(BankError):
    pass

class InvalidAccount(BankError):
    pass

def withdraw(account_balance, amount):
    if account_balance < 0:
        raise InvalidAccount("Account balance is invalid")
    if amount > account_balance:
        raise InsufficientFunds("Not enough funds to withdraw")
    return account_balance - amount

try:
    balance = withdraw(500, 700)
except InsufficientFunds as e:
    print("Error:", e)
except InvalidAccount as e:
    print("Error:", e)

### 2. Weak Password Custom Exception

class WeakPasswordError(Exception):
    pass

def set_password(password):
    if len(password) < 6 or password.isdigit() or password.isalpha():
        raise WeakPasswordError("Password too weak! Must contain letters & numbers, and be at least 6 chars.")
    print("Password set successfully")

try:
    set_password("12345")
except WeakPasswordError as e:
    print("Error:", e)


### 3. E-commerce Multiple Custom Exceptions


class ECommerceError(Exception):
    pass

class OutOfStockError(ECommerceError):
    pass

class PaymentFailedError(ECommerceError):
    pass

def place_order(stock, quantity, payment_success):
    if quantity > stock:
        raise OutOfStockError("Item is out of stock")
    if not payment_success:
        raise PaymentFailedError("Payment could not be processed")
    print("Order placed successfully")

try:
    place_order(stock=2, quantity=3, payment_success=True)
except OutOfStockError as e:
    print("Error:", e)
except PaymentFailedError as e:
    print("Error:", e)

### 4. Machine Learning Model Training – Skip Invalid Rows


data = [["5", "3"], ["abc", "7"], ["8", "xyz"], ["4", "2"]]

clean_data = []
for row in data:
    try:
        nums = [int(x) for x in row]
        clean_data.append(nums)
    except ValueError:
        print("Skipping invalid row:", row)

print("Clean data:", clean_data)


### 5. Raise Exception on Missing Values in Dataset


class MissingValueError(Exception):
    pass

dataset = [10, 20, None, 40]

try:
    for i, val in enumerate(dataset):
        if val is None:
            raise MissingValueError(f"Missing value at index {i}")
except MissingValueError as e:
    print("Error:", e)


### 6. Handle Exceptions While Saving a Model

import pickle

def save_model(model, filename):
    try:
        with open(filename, "wb") as f:
            pickle.dump(model, f)
        print("Model saved successfully")
    except (IOError, pickle.PickleError) as e:
        print("Failed to save model:", e)

save_model({"model": "demo"}, "/invalid_path/model.pkl")

### 7. Catch Exceptions in Multi-threaded Execution

import threading

def worker(n):
    try:
        if n == 5:
            raise ValueError("Error in thread with n=5")
        print(f"Thread {n} finished successfully")
    except Exception as e:
        print(f"Exception in thread {n}: {e}")

threads = []
for i in range(1, 7):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


### 8. Global Exception Handler


import sys

def global_exception_handler(exc_type, exc_value, exc_traceback):
    print("Unhandled Exception:", exc_value)

sys.excepthook = global_exception_handler

# Example: This will trigger global handler
x = 1 / 0



### 9. Custom Exceptions for Invalid File Formats


class InvalidFileFormat(Exception):
    pass

def process_file(filename):
    if not (filename.endswith(".csv") or filename.endswith(".json") or filename.endswith(".xml")):
        raise InvalidFileFormat(f"Unsupported file format: {filename}")
    print("File format is valid:", filename)

try:
    process_file("data.txt")
except InvalidFileFormat as e:
    print("Error:", e)


### 10. Centralized Exception Logging


import logging

# Configure logger
logging.basicConfig(filename="app.log", level=logging.ERROR)

def risky_function(x):
    try:
        return 10 / x
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        print("An error occurred. Check logs.")

risky_function(0)

