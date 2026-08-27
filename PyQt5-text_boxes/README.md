# 📝 PyQt5 Name Text Boxes Input GUI

A simple **Graphical User Interface (GUI) application built using Python and PyQt5** that allows the user to enter their name and submit it using a button.

When the user enters their name and clicks the **Submit** button, the program displays a greeting message in the terminal.

## 📌 Project Overview

This beginner-friendly project demonstrates how to use:

* `QLineEdit` for accepting user input
* `QPushButton` for submitting the input
* Signals and slots for handling button clicks
* Qt Style Sheets for customizing the interface
* Methods for retrieving text from a text input field

### Example

The GUI contains:

```text
┌────────────────────────────────────────────┐
│ Enter your name        [ Submit ]           │
└────────────────────────────────────────────┘
```

If the user enters:

```text
Gaurav
```

and clicks **Submit**, the terminal displays:

```text
HelloGaurav
```

> **Tip:** If you want a space between `Hello` and the name, change `print(f"Hello{text}")` to `print(f"Hello {text}")`.

## ✨ Features

* 📝 Name input field
* 🔘 Submit button
* 💬 Displays a greeting in the terminal
* 🎨 Custom font styling
* 📌 Placeholder text
* 🖥️ Simple desktop GUI
* 🐍 Beginner-friendly Python project

## 🛠️ Technologies Used

* **Python 3**
* **PyQt5**
* `QApplication`
* `QMainWindow`
* `QLineEdit`
* `QPushButton`

## 📂 Project Structure

```text
PyQt5-Name-Input-GUI/
│
├── PyQt5_lineedit.py
└── README.md
├── Output.png
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PyQt5-Name-Input-GUI.git
```

### 2. Navigate to the Project Directory

```bash
cd PyQt5-Name-Input-GUI
```

### 3. Install PyQt5

Install PyQt5 using pip:

```bash
pip install PyQt5
```

Or:

```bash
python -m pip install PyQt5
```

## ▶️ How to Run

Run the Python program:

```bash
python main.py
```

A GUI window will appear with:

* A text input field
* A **Submit** button

Enter your name into the input field and click **Submit**.

### Example Output

Input:

```text
Gaurav
```

Terminal output:

```text
HelloGaurav
```

## 🧠 How the Code Works

### 1. Import Required Libraries

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
```

* `sys` → Used to handle application arguments.
* `QApplication` → Manages the GUI application.
* `QMainWindow` → Creates the main window.
* `QLineEdit` → Provides a text input field.
* `QPushButton` → Creates the Submit button.

## 📝 Creating the Text Input

```python
self.line_edit = QLineEdit(self)
```

This creates a text input field where the user can enter their name.

## 💬 Adding Placeholder Text

```python
self.line_edit.setPlaceholderText("Enter your name")
```

This displays a hint inside the input field before the user enters any text.

## 🔘 Creating the Submit Button

```python
self.button = QPushButton("Submit", self)
```

This creates a button labeled:

```text
Submit
```

## 🔗 Connecting the Button

The button is connected to the `submit()` function:

```python
self.button.clicked.connect(self.submit)
```

When the user clicks the button, the `submit()` method is executed.

## 📥 Getting User Input

The entered text is retrieved using:

```python
text = self.line_edit.text()
```

The `text()` method returns the current contents of the `QLineEdit`.

## 👋 Displaying the Greeting

The program prints:

```python
print(f"Hello{text}")
```

For example, if the user enters `Gaurav`:

```text
HelloGaurav
```

For better formatting, you can use:

```python
print(f"Hello {text}")
```

which produces:

```text
Hello Gaurav
```

## 🎨 Styling the GUI

The text input uses:

```python
self.line_edit.setStyleSheet(
    "font-size:20px;"
    "font-family:Arial;"
)
```

The Submit button uses:

```python
self.button.setStyleSheet(
    "font-size:20px;"
    "font-family:Arial;"
)
```

This makes the text larger and sets the font to Arial.

## ⚠️ Troubleshooting

### PyQt5 Not Installed

If you receive:

```text
ModuleNotFoundError: No module named 'PyQt5'
```

install PyQt5:

```bash
pip install PyQt5
```

### Nothing Happens When You Click Submit

Make sure the button is connected to the function:

```python
self.button.clicked.connect(self.submit)
```

### Name Appears Without a Space

If the output is:

```text
HelloGaurav
```

change:

```python
print(f"Hello{text}")
```

to:

```python
print(f"Hello {text}")
```

## 🚀 Future Improvements

This project can be extended by adding:

* 👋 Display the greeting inside the GUI
* 🧹 Clear button
* ⌨️ Press Enter to submit
* ⚠️ Validation for empty input
* 🎨 Improved GUI design
* 🌙 Dark mode
* 📝 Multiple input fields
* 📧 Email input
* 🔐 Login form
* 📋 Form validation

## 🎯 Learning Objectives

This project helps beginners understand:

* Python GUI development
* PyQt5 fundamentals
* `QLineEdit`
* `QPushButton`
* Signals and slots
* Event handling
* User input
* `text()` method
* Qt Style Sheets
* Object-oriented programming

## 👨‍💻 Author

**Gaurav G Salian**

B.Tech – Artificial Intelligence & Machine Learning

## 📄 License

This project is created for **educational and learning purposes**.
