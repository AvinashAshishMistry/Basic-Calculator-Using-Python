# 🧮 Basic Calculator Using Python with GUI (Tkinter)

This project is a simple yet functional GUI calculator built using **Python** and **Tkinter**. It performs basic arithmetic operations like addition, subtraction, multiplication, division, percentage calculations, and includes features like clear and delete.

---

## 🚀 Features

- Interactive GUI built using Tkinter
- Handles real-time input display and expression evaluation
- Supports:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`x`)
  - Division (`÷`)
  - Percentage calculation (`%`)
  - Decimal input (`.`)
  - Deletion of characters (`DEL`)
  - Clearing all input (`AC`)
- Styled with bold fonts and vibrant color contrasts for better visibility
- Input validation with error handling (e.g., division by zero or syntax issues)

---

## 📁 Project Structure

This is a single-script project with the following layout:

    📁 Project Structure:
    └── calculator.py
        ├── """Docstring"""
        │   └── Project title, features, how to run, customization, and license
        ├── import statements
        │   └── from tkinter import *
        ├── show(value) function
        │   ├── Handles all input logic
        │   ├── Arithmetic operations (+, –, x, ÷, %)
        │   ├── Syntax parsing and evaluation
        │   └── Error handling for invalid inputs
        ├── Tkinter root window setup
        │   ├── Title, geometry, styling
        │   └── Screen input field
        ├── make_row() utility
        │   └── Dynamically generates rows of calculator buttons
        ├── Button layout
        │   └── Each row contains grouped buttons via Frames
        └── root.mainloop()
            └── Launches the GUI loop
    ---

🛠 How to Run:
1. Make sure you have Python 3.x installed
2. Run this script:
   python calculator.py

---

📌 Customization Ideas:
- Add keyboard bindings for convenience
- Expand to scientific calculator functions
- Integrate themes or mode switching (dark/light)
- Include history or memory functionality

---

📜 License:
This project is open source and free to use under the MIT License.
