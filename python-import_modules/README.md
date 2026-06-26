# python-import_modules

Project on importing modules, functions, and variables in Python, plus
reading command-line arguments via sys.argv. Part of the ALU
alu-higher_level_programming curriculum.

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.x (hidden_4.pyc was compiled with 3.8)
- All files end with a new line
- First line of every file: #!/usr/bin/python3
- Code follows pycodestyle (PEP 8)
- All files are executable
- No code runs on import (guarded by if __name__ == "__main__")

## Tasks

- 0-add.py : Imports add() from add_0.py and prints 1 + 2 = 3.
- 1-calculation.py : Imports add/sub/mul/div from calculator_1.py and prints results.
- 2-args.py : Prints the number and list of command-line arguments.
- 3-infinite_add.py : Prints the sum of all command-line arguments (handles big numbers).
- 4-hidden_discovery.py : Prints the public names defined in hidden_4.pyc, alpha order.
- 5-variable_load.py : Imports variable a from variable_load_5.py and prints it.

## Helper files

add_0.py, calculator_1.py, and variable_load_5.py are provided by the course.
hidden_4.pyc must be downloaded (see curl command in setup).

## Author

ALU - Higher Level Programming
