# Dictionaries and Data Science Intro (Python)

In Python, **dictionaries** are unordered collections of key-value pairs. They allow efficient data storage, retrieval, and manipulation using unique keys.

## Key Features

- **Unordered**: No specific order of elements.
- **Key-Value Pairs**: Each element consists of a key and a corresponding value.
- **Mutable**: Dictionaries can be modified (add, remove, update elements).
- **Unique Keys**: Keys must be unique; values can be duplicated.

## Syntax

```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

| Method                  | Description                                                     |
|-------------------------|-----------------------------------------------------------------|
| `dict.get(key, default)` | Returns the value for `key` if present, else `default`.         |
| `dict.keys()`            | Returns a view of the dictionary’s keys.                        |
| `dict.values()`          | Returns a view of the dictionary’s values.                      |
| `dict.items()`           | Returns a view of the dictionary’s key-value pairs.             |
| `dict.update(other_dict)`| Updates the dictionary with key-value pairs from `other_dict`.  |
| `dict.pop(key)`          | Removes the key and returns the corresponding value.            |
