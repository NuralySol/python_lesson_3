# Functions and all of the concise operations on functions


# 1. Function Definition
def greet(name):
    """This function greets the person passed in as a parameter."""
    return f"Hello, {name}!"


print(greet("Alice"))  # Output: Hello, Alice!


# 2. Function with Default Arguments
def power(base, exponent=2):
    """This function returns the base raised to the exponent (default: 2)."""
    return base**exponent


print(power(3))  # Output: 9 (default exponent 2)
print(power(3, 3))  # Output: 27


# 3. Function with Variable-length Arguments (*args and **kwargs)
def add(*numbers):
    """This function sums up all positional arguments."""
    return sum(numbers)


print(add(1, 2, 3, 4))  # Output: 10


def show_info(**kwargs):
    """This function displays keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_info(name="Bob", age=30)  # Output: name: Bob, age: 30


# 4. First-class Functions: Assigning a function to a variable
def square(x):
    """This function squares the input."""
    return x * x


sq = square  # Assign function to variable
print(sq(5))  # Output: 25


# 5. Passing Functions as Arguments
def apply(func, value):
    """This function applies a given function to the value."""
    return func(value)


print(apply(square, 4))  # Output: 16


# 6. Functions Returning Other Functions (Closures)
def outer_function(message):
    """This function returns a closure."""

    def inner_function():
        return f"Message: {message}"

    return inner_function


message_func = outer_function("Hello from closure!")
print(message_func())  # Output: Message: Hello from closure!

# 7. Lambda Functions (Anonymous Functions)
double = lambda x: x * 2
print(double(10))  # Output: 20

# Lambda functions with higher-order functions
nums = [1, 2, 3, 4]
doubled_nums = list(map(lambda x: x * 2, nums))
print(doubled_nums)  # Output: [2, 4, 6, 8]


# 8. Decorators (Functions modifying other functions)
def my_decorator(func):
    """This decorator adds extra behavior to a function."""

    def wrapper():
        print("Something extra before the function call")
        func()
        print("Something extra after the function call")

    return wrapper


@my_decorator
def simple_function():
    print("This is the core function.")


simple_function()
# Output:
# Something extra before the function call
# This is the core function.
# Something extra after the function call


# 9. Function with Keyword-Only Arguments (after *)
def introduction(*, name, age):
    """This function forces keyword-only arguments."""
    return f"Name: {name}, Age: {age}"


print(introduction(name="Alice", age=25))  # Output: Name: Alice, Age: 25


# 10. Recursive Functions
def factorial(n):
    """This function returns the factorial of a number."""
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # Output: 120

# 11. Scope of Variables (LEGB - Local, Enclosing, Global, Built-in)
x = 10  # Global variable


def scope_test():
    x = 5  # Local variable
    print(x)  # Output: 5 (Local scope)


scope_test()
print(x)  # Output: 10 (Global scope)


# 12. Function Annotations (optional metadata)
def multiply(a: int, b: int) -> int:
    """This function multiplies two numbers with type hints."""
    return a * b


print(multiply(3, 4))  # Output: 12


# 13. Docstrings (Documenting Functions)
def documented_function():
    """This is a function that does nothing but has a docstring."""
    pass


print(
    documented_function.__doc__
)  # Output: This is a function that does nothing but has a docstring.



#! stats_calculator function and it is a more encompassing function. 

def stats_calculator(
    operation="mean",
    *args,
    precision=2,
    custom_operation=None,
    **kwargs,
) -> float:
    """
    Calculate statistics for a list of numbers with optional custom operations.
    
    Args:
        operation (str): The operation to perform ('mean', 'sum', 'product', 'custom').
        *args: Variable-length argument list of numbers.
        precision (int, optional): Number of decimal places to round the result to. Default is 2.
        custom_operation (function, optional): A user-defined function for custom calculations.
        **kwargs: Additional keyword arguments for custom logic (e.g., power for exponentiation).
    
    Returns:
        float: The result of the statistical operation.
    
    Examples:
        - stats_calculator('mean', 1, 2, 3, 4) -> 2.5
        - stats_calculator('product', 1, 2, 3, 4) -> 24
        - stats_calculator('custom', 1, 2, custom_operation=lambda x: sum(x) ** 2) -> 9.0
    """

    # Nested helper functions (showing closure)
    def mean(numbers):
        return sum(numbers) / len(numbers)

    def product(numbers):
        result = 1
        for number in numbers:
            result *= number
        return result

    # Default operations as first-class functions
    operations = {
        "mean": mean,
        "sum": sum,
        "product": product,
    }

    # Recursion example (factorial of sum)
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    if operation not in operations and operation != "custom":
        raise ValueError(f"Operation '{operation}' is not supported.")

    # Keyword-only arguments enforcement with custom logic
    if operation == "custom" and custom_operation is None:
        raise ValueError("Custom operation requires a 'custom_operation' function.")

    # Calculating the result based on the operation
    if operation == "custom":
        result = custom_operation(args)
    else:
        result = operations[operation](args)

    # Handle additional custom logic with kwargs (e.g., power argument)
    if "power" in kwargs:
        result = result ** kwargs["power"]

    # Round the result with the specified precision
    return round(result, precision)


# Example use cases:

# 1. Basic usage with default 'mean'
print(stats_calculator("mean", 1, 2, 3, 4))  # 2.5

# 2. Using product operation
print(stats_calculator("product", 1, 2, 3, 4))  # 24

# 3. Custom operation: sum of numbers raised to a power
custom_func = lambda x: sum(x) ** 2
print(stats_calculator("custom", 1, 2, custom_operation=custom_func))  # 9.0

# 4. Using additional kwargs (e.g., applying power)
print(stats_calculator("sum", 1, 2, 3, 4, power=2))  # (1+2+3+4)^2 = 100

# 5. Factorial of sum (using recursion)
sum_of_numbers = sum([1, 2, 3])
print(f"Factorial of sum: {factorial(sum_of_numbers)}")  # 6! = 720

def greet(name=None):
    name = name or "Guest"  # If name is None (or any falsy value), it defaults to "Guest"
    print("Hello,", name)

greet()
greet("Nuraly")

#! function with a validator and user input (functions are first class citizen they can be fed inside of another function)
def validate_username(username):
    if not username or not username.isalpha(): 
        print("Invalid username! Please enter a valid username containing only letters.")
        return False
    return True

def greet(username=None):
    if not username:
        username = input("Enter your avatar username: ")
    
    if validate_username(username):
        print(f"Hello, {username}!")
    else:
        print("Hello, Player! Want to provide the username!?")

greet() 

#! lambda function
add = lambda x, y: x + y 

result = add(5, 3) 
print(result)

#! the regular function (can be called anywhere first-class citizen)

def multiply_def(x, y):
    return x * y

house_area = multiply_def(12, 10)
print("Area of the house:", house_area)

#! second lambda function area of the house

multiply = lambda x, y: x * y

result_house_area = multiply(12, 10)
print(result_house_area)