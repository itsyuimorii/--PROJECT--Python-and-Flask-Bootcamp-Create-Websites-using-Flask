# 100 Days of Python Bootcamp for 2023

## Pip Install and PyPi

 ```bash
 pip install requests

 pip install colorama

 ```

```bash
python
>>> from colorama import init
>>> init()
>>> from colorama import Fore
>>> print(Fore.RED + "some read text")
some read text
>>> quit()
```


```bash
pip install openpyxl

```

```bash
python

>>>import openpyxl
```



# __name__ = "__main__"

The line `__name__ = "__main__"` is a common construct used in Python to check whether the current script is being run directly as the main program or if it is being imported as a module.

In Python, every module has a built-in attribute called `__name__`, which represents the name of the module. When a Python script is executed directly, i.e., it is the entry point of the program, the value of `__name__` is set to `"__main__"`. On the other hand, when a module is imported by another script, the value of `__name__` is set to the actual name of the module.

By using the condition `if __name__ == "__main__":`, you can specify a block of code that should only be executed if the script is run directly as the main program. This allows you to have code in the script that won't be executed when the script is imported as a module.

Here's a simple example to illustrate its usage:

```
pythonCopy code
# myprogram.py

def greet():
    print("Hello, World!")

# Code block that will be executed only if this script is run directly
if __name__ == "__main__":
    greet()
```

In this example, the `greet()` function is defined, and then we use the `if __name__ == "__main__":` condition to call the `greet()` function only when the script is executed directly. If this script is imported as a module in another script, the `greet()` function will not be automatically called.

This construct is often used to provide a way to include test code, demonstration examples, or command-line interface functionality in a script while still allowing it to be imported as a module without executing that additional code.





The code you provided is for a Python script called "one.py." Let's break down the code and explain its functionality:

> one.py

```python
#one.py

# Define a function named 'func'
def func():
    print("func() in one.py is being called")

# Print a message indicating the top level of the script
print("Top level in one.py")

# Check if the script is being run directly
if __name__ == "__main__":
    # If it is being run directly, print a corresponding message
    print('one.py is being run directly')
else:
    # If it is being imported as a module, print a corresponding message
    print('one.py is being imported')

```

```python
#two.py

# Import the module 'one'
import one

# Print a message indicating the top level of the script
print("Top level in two.py")

# Call the function 'func' from the 'one' module
one.func()

# Check if the script is being run directly
if __name__ == "__main__":
    # If it is being run directly, print a corresponding message
    print("Two.py is being run directly")
else:
    # If it is being imported as a module, print a corresponding message
    print("Two.py is being imported")

```

Based on the updated code you provided for `one.py` and `two.py`, let's explain the execution and the resulting output:

**For `one.py`:**

```
Top level in one.py
one.py is being run directly
```

When you execute `python one.py`, the output begins with the line `Top level in one.py` because it is not inside any function or conditional statement. Then, since `__name__` is set to `"__main__"` when the script is run directly, the code block inside the `if __name__ == "__main__":` condition is executed, which prints the message "one.py is being run directly".

**For `two.py`:**

```
Top level in one.py
one.py is being imported
Top level in two.py
func() in one.py is being called
Two.py is being run directly
```

When you execute `python two.py`, it first imports `one.py` using the `import` statement. As a result, the top-level code in `one.py` is executed, printing `Top level in one.py`. Then, since `one.py` is being imported as a module, the `if __name__ == "__main__":` condition in `one.py` evaluates to `False`, and the code block inside the `else` statement is executed, printing the message "one.py is being imported".

After that, the execution moves to `two.py`, where it prints `Top level in two.py` to indicate the execution of top-level code in `two.py`. Then, `one.func()` is called, which invokes the `func()` function from `one.py`. This results in the message "func() in one.py" being printed.

Finally, since `two.py` is being run directly as the main program, the `if __name__ == "__main__":` condition in `two.py` evaluates to `True`, and it prints the message "Two.py is being run directly".

Overall, the output you observed is the result of executing both `one.py` and `two.py`, with `one.py` being imported as a module by `two.py`.
