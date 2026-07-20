# Fundamental Booster — Interactive Personal Data Collector

## Objective

This project is an **Interactive Personal Data Collector** built in Python. It captures, processes, and displays personal information from the user using fundamental Python concepts, including `print()` and `input()` functions, data types, variables, operators, type casting, and built-in functions like `id()` and `type()`.

## Features

- Collects the user's **name**, **age**, **height**, and **favourite number** using `input()`.
- Uses **type casting** to convert user input into the appropriate data types:
  - Name → `str`
  - Age → `int`
  - Height → `float`
  - Favourite number → `int`
- Performs an **arithmetic operation** to estimate the user's birth year based on their age.
- Displays each variable's **value**, **data type**, and **memory address** using `type()` and `id()`.
- Prints a clean, formatted summary of the collected information using **f-strings**.
- Greets the user with a welcome message and thanks them with a personalized closing message.

## Program Flow

1. **Welcome and Instructions** — Displays a welcome message describing the program.
2. **Collect Information** — Prompts the user to enter their name, age, height, and favourite number.
3. **Data Processing** — Casts each input to the correct type and calculates the user's approximate birth year.
4. **Display Results** — Prints a summary showing each variable's value, type, and memory address, along with the calculated birth year.
5. **Exit Message** — Thanks the user and ends the program.

## Concepts Demonstrated

| Concept | Where it's used |
|---|---|
| `print()` / `input()` | Collecting and displaying information throughout the program |
| Data types | `str`, `int`, `float` for name, age/favourite number, and height |
| Variables | Storing each piece of collected user data |
| Operators | Arithmetic operator (`-`) used to calculate birth year |
| Type casting | `int()` and `float()` used to convert raw input strings |
| `type()` | Displays the data type of each variable |
| `id()` | Displays the memory address of each variable |
| f-strings | Used to format and display output messages |

## How to Run

1. Make sure Python 3 is installed on your system.
2. Clone this repository:
   ```bash
   git clone <your-repository-link>
   cd <repository-folder>
   ```
3. Run the script:
   ```bash
   python fb_py.py
   ```
4. Follow the on-screen prompts to enter your name, age, height, and favourite number.

## Example Console Interaction

```
=========welcome to the interactive data colletor=========
please enter your name :Alice
please enter your age :25
please enter your height in meters :1.68
please enter your favourite number :7

thank you ! Here is in the information we collectted
Alice:type :<class 'str'> : Memory address :140703847239568
25:type :<class 'int'>: Memory address :9793456
1.68:type :<class 'float'>: Memory address :140703847253232
7:type :<class 'int'> : Memory address :9793312

Here is your approximenty birth year : 2001 (based on your age) = 25

Thank you for using personal data colletor,Have a good day, Alice
```

*(Memory addresses will vary each time the program is run, since they are assigned dynamically by Python.)*

## Assumptions

- The birth year is calculated as an approximation using the current year (2026) minus the user's age, and does not account for whether the user has already had their birthday this year.
- The program assumes the user enters valid input (e.g., a numeric value for age, height, and favourite number). No input validation or error handling is implemented, as it was not part of the assigned requirements.
- Memory addresses returned by `id()` are specific to the CPython implementation and will differ across runs and machines.

## Project Structure

```
├── fb_py.py       # Main Python script for the Personal Data Collector
└── README.md      # Project documentation
```

## Fun Fact 🎉

This program can tell you your `type()`, your `id()`, and even your approximate birth year — the one thing it *can't* tell you is why your favourite number is your favourite number. Some mysteries are beyond `int()`.

## Author

This project was completed as part of the **Fundamental Booster** exam assignment. All code is original and written independently as per the assignment's academic integrity requirements.
