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

def func():
    print("func() in one.py")

print("Top level in one.py")

if __name__ == "__main__":
    print('one.py is being run directly')
else:
    print('one.py is being imported')
```

```python
#two.py
import one 
print("Top level in two.py")

one.func()

if __name__ == "__main__":
    print("Two.py is being run directly")
else:
    print("Two.py is being imported")
```

```bash
#output:
(base) itsyuimoriispace@itsyuimoriis-MacBook-Pro name_and_main % pyth
on one.py
Top level in one.py
one.py is being run directly
(base) itsyuimoriispace@itsyuimoriis-MacBook-Pro name_and_main % pyth
on two.py
Top level in one.py
one.py is being imported
Top level in two.py
func() in one.py
Two.py is being run directly
```

In this script:

1. The `func()` function is defined. It simply prints the message "func() in one.py". This function can be called from other parts of the script or from other scripts if this script is imported as a module.
2. The line `print("Top level in one.py")` is outside of any function or conditional statement. This line will be executed whenever the script is run, regardless of whether it is run directly or imported as a module.
3. The `if __name__ == "__main__":` condition checks if the script is being run directly as the main program or if it is being imported as a module. If the condition is true, the code block inside the if statement will be executed. Otherwise, the code block inside the else statement will be executed.
   - If the script is being run directly as the main program, it will print the message "one.py is being run directly."
   - If the script is being imported as a module by another script, it will print the message "one.py is being imported."

This construct allows you to distinguish between running a script directly or importing it as a module. It provides a way to include code that should only be executed when the script is run directly, while not executing that code when the script is imported as a module.
