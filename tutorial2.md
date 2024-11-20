## Data Structures in Python

---
## 1. Lists
Lists are used to store multiple items in a single variable.

**Creating a List**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

**Accessing Items**
```python
print(fruits[0])  # First item
print(fruits[-1])  # Last item
```

**Modifying Lists**
```python
fruits.append("orange")  # Add an item
fruits[1] = "blueberry"  # Change an item
print(fruits)
```

**Iterating Through a List**
```python
for fruit in fruits:
    print(fruit)
```

**Common List Methods**
append(item): Add an item
remove(item): Remove an item
len(list): Get the number of items
sort(): Sort the list

**Exercise:**
Create a list of your favorite hobbies.
Add a new hobby to the list.
Print each hobby using a loop.

## 2. Dictionaries
Dictionaries store data in key-value pairs.

Creating a Dictionary
python
Copy code
student = {"name": "Alex", "age": 16, "grade": "A"}
print(student)
Accessing Items
python
Copy code
print(student["name"])  # Access value by key
Adding/Updating Keys
python
Copy code
student["school"] = "High School"  # Add a new key
student["grade"] = "A+"  # Update value
print(student)
Iterating Through a Dictionary
python
Copy code
for key, value in student.items():
    print(key, ":", value)
Common Dictionary Methods
keys(): Get all keys
values(): Get all values
items(): Get all key-value pairs
Exercise:
Create a dictionary with details about your favorite book (title, author, year).
Add a new key for the genre.
Print all the keys and values.
3. DataFrames (Using pandas)
What is a DataFrame? A DataFrame is a 2-dimensional table-like data structure in the pandas library. Think of it as a spreadsheet.

Setting Up pandas
Make sure you have pandas installed:

bash
Copy code
pip install pandas
Creating a DataFrame
python
Copy code
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [16, 17, 16],
    "Grade": ["A", "B", "A"]
}

df = pd.DataFrame(data)
print(df)
Accessing Columns
python
Copy code
print(df["Name"])  # Access a single column
print(df[["Name", "Age"]])  # Access multiple columns
Filtering Rows
python
Copy code
print(df[df["Age"] > 16])  # Students older than 16
Adding a New Column
python
Copy code
df["Passed"] = [True, False, True]
print(df)
Iterating Through Rows
python
Copy code
for index, row in df.iterrows():
    print(row["Name"], "is", row["Age"], "years old.")
Exercise:
Create a DataFrame with data about your favorite movies (columns: Title, Year, Genre).
Add a new column for Rating.
Filter the movies to show only those released after 2010.
4. Comparing Lists, Dictionaries, and DataFrames
Feature	List	Dictionary	DataFrame
Data Organization	Ordered, items by index	Key-value pairs	Rows and columns
Access Method	By index	By key	By row/column
Ideal Use Case	Simple collections	Mapping relationships	Tabular data
5. Final Project Idea: Student Report System
Build a system that:

Stores student data in a DataFrame.
Allows adding a new student (Name, Age, Grade).
Filters students by a minimum grade.
Prints all student data.
Example Code for the System:
python
Copy code
import pandas as pd

# Initial data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [16, 17, 16],
    "Grade": ["A", "B", "A"]
}
df = pd.DataFrame(data)

# Add a new student
new_student = {"Name": "Daisy", "Age": 17, "Grade": "A+"}
df = df.append(new_student, ignore_index=True)

# Filter by grade
print("Students with grade A or higher:")
print(df[df["Grade"] >= "A"])
