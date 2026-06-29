products=input("Enter list of products").split()
list=eval(input("enter "))
numbers=list(map(int,input("Enter the number :").split()))
difference in all these inputs

## Visual Comparison Table

| Line of Code | What You Type (Example) | What Python Creates | Data Type |
|---|---|---|---|
| products=input(...).split() | apple banana cherry     | ['apple', 'banana', 'cherry']   | List of Strings |
| list=eval(input(...))       | [10, 20, 30]            | [10, 20, 30]                    | Actual Python Object |
| numbers=list(map(...))      | 5 10 15                 | [5, 10, 15]                     | List of Integers |

------------------------------
## Detailed Differences## 1. The Word Splitter (products=...)

* How it works: It takes whatever text you type, looks for spaces, and cuts the text into separate words.
* Result: It always creates a list of strings.
* Example: If you type 1 2 3, it creates ['1', '2', '3'] (text, not numbers).

## 2. The Code Executor (list=eval(...))

* How it works: eval() treats your input text as actual Python code. You must type valid Python syntax (like brackets and commas) into the prompt.
* Result: It converts the text directly into a Python data structure (like a list, tuple, or dictionary).
* Example: If you type [1, 2], it builds a list. If you type {"a": 1}, it builds a dictionary.
* Note: Avoid using list as a variable name, as it overrides Python's built-in list() function.

## 3. The Number Converter (numbers=...)

* How it works: It splits your input by spaces, and then map(int, ...) forces every single item to convert from a string into a whole number (integer).
* Result: It creates a list of pure math numbers.
* Example: If you type 1 2 3, it creates [1, 2, 3]. If you type a word like apple, the program will crash with an error.

.upper() or .lower() after input helps u in using specific string in if function

