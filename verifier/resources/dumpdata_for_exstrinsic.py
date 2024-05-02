#!/usr/bin/env python3
import json
import sys

def process_json_object(data):
    try:
        # Pad each hex string to 64 characters
        proof_hex = [format(int(x), 'x').zfill(64) for x in data['proof']]
        inputs_hex = [format(int(x), 'x').zfill(64) for x in data['inputs']]
        concatenated_hex = ''.join(proof_hex + inputs_hex)
        return concatenated_hex
    except ValueError as e:
        print(f"An error occurred during conversion: {e}")
        return None
    except KeyError as e:
        print(f"Missing key in JSON data: {e}")
        return None

def convert_and_concatenate(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return process_json_object(data)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON. Please ensure the file is correctly formatted.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: script.py <path_to_json_file>")
    else:
        file_path = sys.argv[1]
        result = convert_and_concatenate(file_path)
        # Print the result in chunks of 64 characters
        for i in range(0, len(result), 64):
            print(result[i:i+64])