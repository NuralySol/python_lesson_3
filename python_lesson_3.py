#! Dictionaries

# 1. Creating a dictionary
student_grades = {"Amy": 90, "Ben": 85, "Cal": 92}
print("Initial Dictionary:", student_grades)

# 2. Accessing a value by key
print("Amy's grade:", student_grades["Amy"])

# 3. Adding or updating values in the dictionary
student_grades["Dan"] = 88  # Adding a new key-value pair
student_grades["Ben"] = 89  # Updating an existing key's value
print("After adding/updating:", student_grades)

# 4. Removing key-value pairs
del student_grades["Cal"]  # Using 'del'
removed_value = student_grades.pop("Ben")  # Using 'pop' method
print("After deletion:", student_grades)
print("Popped value:", removed_value)

# 5. Checking if a key exists
if "Amy" in student_grades:
    print("Amy is in the dictionary.")

if "Cal" not in student_grades:
    print("Cal is not in the dictionary.")

# 6. Getting a value with a default (avoiding KeyError)
print("Eli's grade:", student_grades.get("Eli", "No grade found"))

# 7. Iterating through the dictionary
print("\nIterating through keys:")
for student in student_grades:
    print(student)

print("\nIterating through values:")
for grade in student_grades.values():
    print(grade)

print("\nIterating through key-value pairs:")
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

# 8. Dictionary Methods
print("\nDictionary Methods:")

# Copying a dictionary
copied_grades = student_grades.copy()
print("Copied Dictionary:", copied_grades)

# Clearing a dictionary
copied_grades.clear()
print("Cleared Dictionary:", copied_grades)

# Merging dictionaries using 'update()'
new_grades = {"Eli": 95, "Fay": 78}
student_grades.update(new_grades)
print("After merging with update:", student_grades)

# Getting all keys
print("Keys:", student_grades.keys())

# Getting all values
print("Values:", student_grades.values())

# Getting all key-value pairs
print("Items:", student_grades.items())

# Using 'fromkeys()' to create a dictionary with default values
default_scores = dict.fromkeys(["Amy", "Ben", "Cal"], 0)
print("From keys with default values:", default_scores)

# Setting a default value if the key doesn't exist using 'setdefault()'
amy_grade = student_grades.setdefault("Amy", 100)  # Amy already exists
eli_grade = student_grades.setdefault("Eli", 100)  # Eli doesn't exist, adds key
print(f"Amy's grade (setdefault): {amy_grade}")
print(f"Eli's grade (setdefault): {eli_grade}")
print("After setdefault:", student_grades)

# 9. Nested Dictionaries (Dictionary within a dictionary)
students = {
    "Amy": {"Math": 90, "Science": 88},
    "Ben": {"Math": 85, "Science": 90},
}
print("\nNested Dictionary:")
print("Amy's Math score:", students["Amy"]["Math"])

# 10. Sorting dictionary keys (produces a list of sorted keys)
sorted_keys = sorted(student_grades.keys())
print("Sorted Keys:", sorted_keys)

# 11. Dictionary Comprehension (Creating a dictionary using comprehension)
squared_numbers = {x: x**2 for x in range(1, 6)}
print("Dictionary Comprehension (squares):", squared_numbers)

# 12. Merging two dictionaries (Python 3.9+ method)
dict1 = {"A": 1, "B": 2}
dict2 = {"B": 3, "C": 4}
merged_dict = dict1 | dict2
print("Merged Dictionary using |:", merged_dict)


#! Flatten the nested dictionary needs a function to make it work and O(N) time complexity
#! Space complexity is O(N) as well depending on the size, due to required space for the flattened dict,


def flatten_dict(d, parent_key="", sep="_"):
    """
    Recursively flattens a nested dictionary.

    :param d: The dictionary to flatten
    :param parent_key: The base key (used for recursion)
    :param sep: Separator between keys (default is '_')
    :return: A flattened dictionary
    """
    items = []

    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k  # Create new key
        if isinstance(v, dict):
            #! Recursively flatten the dictionary (needs a recursion)
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            # If the value is not a dictionary, appends the key-value pair
            items.append((new_key, v))

    return dict(items)


#! Example of a nested dictionary ( can be any nested dictionary with any data types that accept dict.)
nested_dict = {
    "user": {
        "name": {"first": "Nuraly", "last": "Soltonbekov"},
        "location": "USA",
        "details": {"age": 33, "status": "active"},
    },
    "metadata": {"id": 101, "role": "admin"},
}

# Flattening the nested dictionary (call the function and assign it to flat_dict var)
flat_dict = flatten_dict(nested_dict)

# Output the flattened dictionary (prints the new flat dict data structure)
print(flat_dict)


#! Big O of unflattened Dict is O(n * k) k -> meaning the level of drilling
#! the below is the code to unflaten the dict.
def unflatten_dict(flat_dict, separator="."):
    unflattened_dict = {}

    for flat_key, value in flat_dict.items():
        keys = flat_key.split(separator)
        current = unflattened_dict
        #! the code snippet below for loop makes it 3 level dict. a.b.c. so 3 levels
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]

        current[keys[-1]] = value

    return unflattened_dict


#! Example usage: can be any single traversal dictionary with no drilling
flat_dict = {"a.b.c": 1, "a.b.d": 2, "e": 3}

nested_dict = unflatten_dict(flat_dict)
print(nested_dict)

#! employes dictionary iterations!
emps = [
    {"fname": "Amy", "lname": "Ames", "salary": 130000, "dept": "IT"},
    {"fname": "Bob", "lname": "Biggs", "salary": 93000, "dept": "Sales"},
    {"fname": "Cal", "lname": "Combs", "salary": 105000, "dept": "IT"},
    {"fname": "Dan", "lname": "Dunn", "salary": 78000, "dept": "Marketing"},
    {"fname": "Edna", "lname": "Evans", "salary": 89000, "dept": "Sales"},
]
# bonus_money given to employees!
for employee in emps:
    bonus_money = employee["salary"] * 0.1

    summary = f"{employee['fname']} {employee['lname']} works in the {employee['dept']} department and now gets the bonus of ${bonus_money:.2f}."

    print(summary)

