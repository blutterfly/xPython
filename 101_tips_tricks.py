
def walrus_operator():
    """
    1. Walrus Operator (Python 3.8+)
    The walrus operator := allows assignment expressions, 
    making it possible to assign a value to a variable as part of an expression.
    """
    # Without walrus operator
    n = 10
    result = []
    while n:
        square = n ** 2
        result.append(square)
        n -= 1
    print(result)

    # With walrus operator
    n = 10
    result = []
    while (square := n ** 2):
        result.append(square)
        n -= 1
    print(result)


def enumerate():
    """
    2. Enumerate
    Enumerate allows you to loop through an iterable with an index.
    """ 

    names = ["Alice", "Bob", "Charlie"]
    for index, name in enumerate(names):
        print(f"{index}: {name}")


def comprehensions():
    # List comprehension
    squares = [x ** 2 for x in range(10)]
 
    # Dictionary Comprehensions
    squares = {x: x ** 2 for x in range(10)}
    
    # Set Comprehensions    
    unique_lengths = {len(word) for word in ["apple", "banana", "cherry"]}


def itertools():
    # The itertools module provides powerful iterator building blocks.

    import itertools

    # Combining iterables
    combined = itertools.chain([1, 2, 3], [4, 5, 6])

    # Repeat an iterable
    repeated = itertools.cycle([1, 2, 3])
    
    # Generate permutations
    perms = itertools.permutations([1, 2, 3], 2)


def conditional_expressions():
    # Ternary Operator
    # Write short if-else statements in a single line.

    x = 10
    result = "even" if x % 2 == 0 else "odd"


def functools_partial():
    # Create a new function with some arguments pre-filled.

    from functools import partial

    def add(a, b):
        return a + b

    add_five = partial(add, 5)
    print(add_five(3))  # 8


def contextlib_suppress():
    # Suppress specific exceptions using a context manager.

    from contextlib import suppress

    with suppress(FileNotFoundError):
        os.remove("non_existent_file.txt")


def function_annotations():
    # Provide hints about the expected types of function arguments and return values.

    def greet(name: str) -> str:
        return f"Hello, {name}!"

    print(greet("Alice"))


def lambda_functions():
    # 11. One-Liner Functions (Lambda)
    # Create simple, anonymous functions using the lambda keyword.

    add = lambda x, y: x + y
    print(add(5, 3))  # 8


def underscore_large_numbers():
    # Improve the readability of large numbers by using underscores.

    large_number = 1_000_000_000


def pathlib_module():
    # 13. pathlib
    # Use the pathlib module to work with file paths in an OS-independent manner.

    from pathlib import Path

    path = Path("folder/subfolder/file.txt")
    print(path.resolve())  # Get the absolute path


def data_classes():    
    # 14. Data Classes (Python 3.7+)
    # Automatically generate special methods like __init__, __repr__, and __eq__ for classes that primarily store data.

    from dataclasses import dataclass

    @dataclass
    class Point:
        x: float
        y: float

    p1 = Point(1.0, 2.0)
    p2 = Point(1.0, 2.0)
    print(p1)  # Point(x=1.0, y=2.0)
    print(p1 == p2)  # True


def any_all_func():
    # 15. The 'any' and ‘all’ Built-in Functions
    # Check if any or all elements in an iterable meet a certain condition.

    nums = [1, 3, 5, 7]
    even_exists = any(x % 2 == 0 for x in nums)  # False
    all_odd = all(x % 2 != 0 for x in nums)  # True


def zip_func():

    # 16. Using ‘zip’ to Iterate Over Multiple Iterables
    # Combine multiple iterables and loop through them simultaneously.

    names = ["Alice", "Bob", "Charlie"]
    ages = [30, 25, 22]

    for name, age in zip(names, ages):
        print(f"{name} is {age} years old.")


def collections_namedtuple():
    # 17. collections.namedtuple
    # Create simple classes with named fields, similar to a tuple.

    from collections import namedtuple

    Person = namedtuple("Person", ["name", "age"])

    alice = Person("Alice", 30)
    print(alice.name)  # Alice


""" TO BE CONTINUED
18. Using 'else’ with Loops
Execute a block of code if a loop completes without encountering a break.

for num in range(2, 10):
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
19. Generator Expressions
Create generators using a similar syntax to list comprehensions, but with parentheses.

squares = (x ** 2 for x in range(10))
for square in squares:
    print(square)
20. collections.defaultdict
A defaultdict automatically assigns a default value for nonexistent keys.

from collections import defaultdict

word_count = defaultdict(int)
words = ["apple", "banana", "apple", "orange"]

for word in words:
    word_count[word] += 1
21. Multiple Assignment
Assign values to multiple variables in a single line.

a, b, c = 1, 2, 3
22. Unpacking
Unpack elements from iterables.

nums = [1, 2, 3, 4, 5]
first, *middle, last = nums
print(first)  # 1
print(middle)  # [2, 3, 4]
print(last)  # 5
23. F-strings (Python 3.6+)
Easily format strings with variables.

name = "Alice"
age = 30
print(f"{name} is {age} years old.")  # Alice is 30 years old.
24. inspect.signature
Get the signature of a function or method, including its arguments and their default values.

import inspect

def example_function(a, b=5, c="hello"):
    pass

signature = inspect.signature(example_function)
print(signature)  # (a, b=5, c='hello')
25. functools.lru_cache
Add a Least Recently Used (LRU) cache to your functions to cache results and improve performance.

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))  # 354224848179261915075
26. functools.wraps
Preserve the original function’s metadata when using decorators.

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator called")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example_function():
    """This is an example function."""
    pass

print(example_function.__doc__)  # This is an example function.
27. getattr, setattr, and hasattr
Dynamically access, set, or check for attributes in objects.

class MyClass:
    def __init__(self):
        self.my_attr = "hello"

obj = MyClass()

print(getattr(obj, "my_attr"))  # hello
setattr(obj, "my_attr", "world")
print(getattr(obj, "my_attr"))  # world
print(hasattr(obj, "non_existent_attr"))  # False
28. operator.itemgetter
Get an item from an object, typically used with sorted, map, or filter.

from operator import itemgetter

data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 22}]
sorted_data = sorted(data, key=itemgetter("age"))
print(sorted_data)  # [{'name': 'Charlie', 'age': 22}, {'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
29. os.walk
Recursively traverse directories and their contents.

import os

for root, dirs, files in os.walk("my_directory"):
    for file in files:
        print(f"Processing {os.path.join(root, file)}")
30. 're' module
Use regular expressions to manipulate and search strings.

import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r"\b\w{5}\b"

five_letter_words = re.findall(pattern, text)
print(five_letter_words)  # ['quick', 'brown', 'jumps']
31. collections.Counter
Count the occurrences of elements in a list.

from collections import Counter

words = ["apple", "banana", "apple", "orange"]
word_count = Counter(words)
print(word_count)  # Counter({'apple': 2, 'banana': 1, 'orange': 1})
32. Chaining Comparison Operators
Chain multiple comparisons in a single expression.

x = 5
print(1 < x < 10)  # True
33. socket.gethostname and socket.gethostbyname
Get the hostname and IP address of the current machine.

import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
34. os.environ
Access environment variables from Python.

import os

path = os.environ.get("PATH")
print(f"PATH: {path}")
35. ‘shutil’ module
Perform high-level file operations, such as copying, moving, or deleting files and directories.

import shutil

# Copy a file
shutil.copy("source.txt", "destination.txt")

# Move a file
shutil.move("source.txt", "destination_folder/")

# Remove a directory and its contents
shutil.rmtree("directory_to_delete")
36. ‘tempfile' module
Create temporary files and directories.

import tempfile

with tempfile.TemporaryFile(mode="w+t") as temp_file:
    temp_file.write("Hello, temporary file!")
    temp_file.seek(0)
    content = temp_file.read()
    print(content)  # Hello, temporary file!

37. 'csv’ module
Read and write CSV files.

import csv

# Writing to a CSV file
with open("output.csv", "w", newline="") as csvfile:
    fieldnames = ["name", "age"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 30})
    writer.writerow({"name": "Bob", "age": 25})

# Reading from a CSV file
with open("output.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"{row['name']} is {row['age']} years old.")
38. 'glob' module
Find all files matching a pattern.

import glob

txt_files = glob.glob("*.txt")
for txt_file in txt_files:
    print(f"Found a text file: {txt_file}")
39. The ‘in’ keyword
Check if an element is in a list, set, or dictionary.

names = ["Alice", "Bob", "Charlie"]

# Check if an element is in a list
print("Alice" in names)  # True

# Check if a key is in a dictionary
ages = {"Alice": 30, "Bob": 25}
print("Charlie" in ages)  # False
40. 'pprint’ module
Pretty-print complex data structures.

from pprint import pprint

data = {
    "names": ["Alice", "Bob", "Charlie"],
    "ages": {"Alice": 30, "Bob": 25, "Charlie": 22},
}

pprint(data)
41. 'calendar' module
Work with dates and calendars.

import calendar

cal = calendar.month(2023, 4)
print(cal)
42. 'deque' from 'collections'
A double-ended queue allows efficient appending and popping from both ends.

from collections import deque

dq = deque([1, 2, 3])
dq.append(4)  # Add to the right end
dq.appendleft(0)  # Add to the left end
dq.pop()  # Remove from the right end
dq.popleft()  # Remove from the left end
43. 'queue’ module
Implement synchronized queues for communication between threads.

from queue import Queue
from threading import Thread

def worker(q):
    while not q.empty():
        item = q.get()
        print(f"Processing {item}")

q = Queue()
for i in range(10):
    q.put(i)

t = Thread(target=worker, args=(q,))
t.start()
t.join()
44. 'heapq' module
Implement heaps and priority queues.

import heapq

data = [4, 2, 6, 1, 8, 3]
heapq.heapify(data)  # Transform data into a heap

smallest = heapq.heappop(data)  # Pop the smallest element
heapq.heappush(data, 5)  # Push a new element into the heap
45. ‘timeit' module
Measure the execution time of code snippets.

import timeit

def slow_function():
    return sum(range(1000))

execution_time = timeit.timeit(slow_function, number=1000)
print(f"Execution time: {execution_time:.6f} seconds")
46. The ‘assert’ statement
Check if a condition is true, raising an AssertionError if it’s not.

def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

result = divide(4, 2)  # Works fine
result = divide(4, 0)  # Raises AssertionError: Cannot divide by zero
47. try-except-finally
Handle exceptions and ensure specific code is executed regardless of whether an exception occurred.

try:
    result = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always be executed")
48. 'with' statement
Simplify the use of context managers, such as file handling or acquiring and releasing locks.

with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# File is automatically closed when the block exits
49. 'json’ module
Encode and decode JSON data.

import json

data = {"name": "Alice", "age": 30}

# Encode Python object as JSON string
json_data = json.dumps(data)
print(json_data)  # {"name": "Alice", "age": 30}

# Decode JSON string to Python object
decoded_data = json.loads(json_data)
print(decoded_data)  # {'name': 'Alice', 'age': 30}
50. 'asyncio' module
Asynchronous programming with coroutines, allowing concurrent execution of tasks without threads.

import asyncio

async def my_coroutine():
    print("Starting the coroutine")
    await asyncio.sleep(1)
    print("Coroutine completed")

async def main():
    await asyncio.gather(my_coroutine(), my_coroutine())

asyncio.run(main())

"""