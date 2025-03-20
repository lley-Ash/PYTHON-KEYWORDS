# Import necessary modules
import math  # 'import' keyword to bring in a module
from random import randint  # 'from' and 'import' keywords

# Define a class using 'class' keyword
class SampleClass:
    def __init__(self, value):  # 'def' defines a function
        self.value = value
    
    def show_value(self):
        return self.value

# Function using 'lambda', 'return', and 'global'
global_var = 10  # 'global' keyword

def modify_global():
    global global_var
    global_var = 20  # Modifying the global variable

square = lambda x: x * x  # 'lambda' keyword

# Function demonstrating 'try', 'except', and 'finally'
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:  # 'except' keyword
        result = None  # 'None' keyword
    finally:  # 'finally' always executes
        print("Execution completed.")
    return result

# Function using 'assert', 'pass', and 'raise'
def check_positive(num):
    assert num >= 0, "Number must be positive!"  # 'assert' keyword
    if num == 0:
        pass  # 'pass' does nothing, used as a placeholder
    elif num < 0:
        raise ValueError("Negative number found!")  # 'raise' keyword
    return True

# Loop using 'for', 'while', 'break', and 'continue'
def loop_example():
    for i in range(5):  # 'for' loop
        if i == 3:
            break  # 'break' exits the loop
        elif i == 1:
            continue  # 'continue' skips this iteration
        print(i)

    j = 0
    while j < 3:  # 'while' loop
        print(j)
        j += 1

# Using 'with' statement to handle files
def file_example():
    with open("example.txt", "w") as file:  # 'with' ensures proper file handling
        file.write("Hello, World!")

# Using 'is', 'in', 'not', 'or', 'and', 'False', 'True'
def boolean_example():
    x = True  # 'True' keyword
    y = False  # 'False' keyword
    if x is True and y is not True:  # 'is' and 'not'
        print("x is True and y is False")
    if 2 in [1, 2, 3]:  # 'in' keyword
        print("2 is in the list")
    if y or x:  # 'or' and 'and' keywords
        print("At least one is True")

# Using 'del' and 'nonlocal'
def outer_function():
    a = 5
    
    def inner_function():
        nonlocal a  # 'nonlocal' keyword to modify the outer variable
        a += 1
    
    inner_function()
    return a

del global_var  # 'del' deletes a variable

# Using 'yield' in a generator
def generator_example():
    for i in range(3):
        yield i  # 'yield' produces a value

# Getting user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Sum: {num1 + num2}")

# Calling functions
modify_global()
print(square(int(input("Enter a number to square: "))))
print(divide(num1, num2))
check_positive(int(input("Enter a positive number: ")))
loop_example()
file_example()
boolean_example()
print(outer_function())
gen = generator_example()
print(next(gen))
print(next(gen))
print(next(gen))
