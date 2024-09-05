0x04. UTF-8 Validation
Overview
This project focuses on validating if a given dataset represents a valid UTF-8 encoding. UTF-8 is a variable-length character encoding scheme that uses 1 to 4 bytes to encode characters. You will implement a Python method that checks whether the input data is a valid UTF-8 encoding.

What the File Does
The script defines a function validUTF8(data) that returns True if the input dataset represents a valid UTF-8 encoding, and False otherwise.
The input data is a list of integers, where each integer represents a byte of data.
The function handles characters ranging from 1 to 4 bytes long and checks if each sequence follows the correct UTF-8 encoding rules.
