# 1. Custom exception if data file is missing
class DataFileMissingError(Exception):
    pass

import os
def load_data_file(filename):
    if not os.path.exists(filename):
        raise DataFileMissingError(f"Data file '{filename}' is missing!")
    with open(filename, "r") as f:
        return f.read()


# 2. Raise exception on schema mismatch
class SchemaMismatchError(Exception):
    pass

def validate_schema(data, expected_keys):
    for record in data:
        if set(record.keys()) != set(expected_keys):
            raise SchemaMismatchError("Dataset schema does not match expected schema")
    return True


# 3. Handle KeyError when accessing dictionary values
def safe_access(data, key):
    try:
        return data[key]
    except KeyError:
        print(f"Key '{key}' not found in dataset")
        return None


# 4. Simulate ETL pipeline exception handling
class ExtractError(Exception): pass
class TransformError(Exception): pass
class LoadError(Exception): pass

def extract():
    raise ExtractError("Failed to extract data")

def transform(data):
    if not data:
        raise TransformError("No data to transform")
    return [d.upper() for d in data]

def load(data):
    if len(data) == 0:
        raise LoadError("No data to load")
    print("Data loaded successfully")

def etl_pipeline():
    try:
        data = extract()
        data = transform(data)
        load(data)
    except (ExtractError, TransformError, LoadError) as e:
        print("ETL Pipeline failed:", e)


# 5. Catch exceptions while reading data from an API
import requests

def fetch_api(url):
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("API request failed:", e)


# 6. Handle exceptions while connecting to Azure Blob Storage (mocked)
class AzureBlobConnectionError(Exception):
    pass

def connect_to_blob(success=False):
    if not success:
        raise AzureBlobConnectionError("Failed to connect to Azure Blob Storage")
    return "Connected successfully"


# 7. Handle corrupted JSON file
import json

def read_json(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print("Corrupted JSON file:", e)


# 8. Raise exception when duplicate data is found
class DuplicateDataError(Exception):
    pass

def check_duplicates(data):
    seen = set()
    for item in data:
        if item in seen:
            raise DuplicateDataError(f"Duplicate found: {item}")
        seen.add(item)
    return True


# 9. Catch exceptions while writing data into SQL database
def write_to_sql(data):
    try:
        # Simulated failure
        if not data:
            raise Exception("No data to write")
        print("Data written to SQL successfully")
    except Exception as e:
        print("SQL write failed:", e)


# 10. Retry failed API requests 3 times
def fetch_with_retries(url, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, timeout=2)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            attempt += 1
            print(f"Attempt {attempt} failed:", e)
    raise Exception("API request failed after 3 retries")

