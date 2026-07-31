# Python - Inheritance

Exercises on inheritance in Python: inspecting objects, subclassing built-in
types, checking class relationships, and building a small geometry class
hierarchy with shared validation.

## Files

| File | Description |
|------|-------------|
| `0-lookup.py` | Returns an object's attributes and methods |
| `1-my_list.py` | `MyList` subclass of `list` with `print_sorted()` |
| `2-is_same_class.py` | True if obj is exactly an instance of a class |
| `3-is_kind_of_class.py` | True if obj is an instance or subclass instance |
| `4-inherits_from.py` | True only if obj is a subclass instance |
| `5-base_geometry.py` | Empty `BaseGeometry` class |
| `6-base_geometry.py` | Adds `area()` that raises an Exception |
| `7-base_geometry.py` | Adds `integer_validator()` |
| `8-rectangle.py` | `Rectangle` inheriting from `BaseGeometry` |
| `9-rectangle.py` | Adds `area()` and string representation |
| `10-square.py` | `Square` inheriting from `Rectangle` |
| `11-square.py` | `Square` with its own string representation |

## Tests

- `tests/1-my_list.txt` — doctests for `MyList`
- `tests/7-base_geometry.txt` — doctests for `BaseGeometry`

Run with: `python3 -m doctest tests/1-my_list.txt -v`

## Requirements

- Python 3
- No external modules are imported
- All files are executable and PEP8-compliant

## Author

ALU - Higher Level Programming
