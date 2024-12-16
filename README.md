# puzzles-minidsa01
# Puzzles#minidsa

This repository contains solutions to interesting programming puzzles and mini data structure & algorithm (DSA) problems. It is designed to help improve problem-solving skills and understanding of core DSA concepts.

---

## Problem: Filter Strings Containing 'a'

### Problem Statement
Write a function `filter_strings_containing_a` that takes a list of strings as input and returns a new list containing only the strings that have the letter `'a'`.

### Example
**Input**:
```python
["apple", "banana", "cherry", "date"]
output:
["apple", "banana", "date"]

def filter_strings_containing_a(input_strs):
    """
    Filters the strings in the input list and returns a new list containing only
    the strings that contain the letter 'a'.

    :param input_strs: list of strings
    :return: list of strings containing the letter 'a'
    """
    return [s for s in input_strs if 'a' in s]

# Example usage:
input_list = ["apple", "banana", "cherry", "date"]
result = filter_strings_containing_a(input_list)
print(result)  # Output: ['apple', 'banana', 'date']

How to Use This Repository
Clone the repository:
bash
Copy code
git clone https://github.com/YourUsername/puzzles-minidsa.git
Navigate to the folder:
bash
Copy code
cd puzzles-minidsa
Run the Python file:
bash
Copy code
python filter_strings.py
Contributing
Contributions are welcome! If you want to add new puzzles or improve the existing solutions:

Fork the repository.
Create a new branch:
bash
Copy code
git checkout -b feature-new-puzzle
Commit your changes and push them to your forked repository.
Submit a pull request.


