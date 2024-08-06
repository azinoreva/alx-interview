Pascal's Triangle
This Python script generates Pascal's Triangle up to a specified number of rows. Pascal's Triangle is a triangular array of binomial coefficients, where each row corresponds to the coefficients of the binomial expansion.

Description
The pascal_triangle function takes an integer n as input and returns a list of lists representing Pascal's Triangle up to n rows. Each inner list represents a row of Pascal's Triangle. The script prints each row of the triangle as it is generated.

Usage
Function
python
Copy code
def pascal_triangle(n):
    """
    Takes an integer n and returns a list of lists representing Pascal's Triangle up to n rows.
    """
    # Function implementation
Example
To generate and print Pascal's Triangle with 8 rows:

python
Copy code
pascal_triangle(8)
Output
The output for pascal_triangle(8) will be:

csharp
Copy code
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
