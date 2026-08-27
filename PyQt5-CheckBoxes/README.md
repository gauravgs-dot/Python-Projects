# ☑️ PyQt5 Checkbox GUI

A simple **Graphical User Interface (GUI) application built using Python and PyQt5** that demonstrates how to create and handle a checkbox.

The application asks the user **"Do you like food?"** and detects whether the checkbox is checked or unchecked. The result is displayed in the terminal.

## 📌 Project Overview

This beginner-friendly project demonstrates the use of the `QCheckBox` widget in PyQt5.

When the checkbox is:

* ☑️ **Checked** → The program prints `You like food`
* ⬜ **Unchecked** → The program prints `You don't like food`

It also demonstrates how to connect a checkbox's `stateChanged` signal to a custom function.

## ✨ Features

* 🖥️ Simple PyQt5 GUI
* ☑️ Interactive checkbox
* 🖱️ Detects checkbox state changes
* 💬 Displays the result in the terminal
* 🔗 Uses PyQt5 signals and slots
* 🐍 Beginner-friendly Python project

## 🛠️ Technologies Used

* **Python 3**
* **PyQt5**
* `QApplication`
* `QMainWindow`
* `QCheckBox`
* `Qt`

## 📂 Project Structure

```text id="d6x9y8"
PyQt5-Checkbox-GUI/
│
├── PyQt5_CheckBoxes.py
├── README.md
├── Output.png
```

## ⚙️ Installation

### 1. Clone the Repository

```bash id="g3y7qf"
git clone https://github.com/your-username/PyQt5-Checkbox-GUI.git
```

### 2. Navigate to the Project Directory

```bash id="q3f8la"
cd PyQt5-Checkbox-GUI
```

### 3. Install PyQt5

Install PyQt5 using pip:

```bash id="5h8r2u"
pip install PyQt5
```

Or:

```bash id="k6v2wb"
python -m pip install PyQt5
```

## ▶️ How to Run

Run the Python program:

```bash id="n4s1kd"
python main.py
```

A GUI window will appear with the checkbox:

```text id="a1c8z4"
☐ Do you like food?
```

Click the checkbox to change its state.

### When Checked

The terminal displays:

```text id="x8p3mf"
You like food
```

### When Unchecked

The terminal displays:

```text id="z7r2kc"
You don't like food
```

## 🧠 How the Code Works

### 1. Import Required Libraries

```python id="p4j7mx"
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt
```

* `sys` → Used for application arguments.
* `QApplication` → Manages the GUI application.
* `QMainWindow` → Creates the main application window.
* `QCheckBox` → Creates the checkbox.
* `Qt` → Provides constants such as `Qt.Checked`.

## ☑️ Creating the Checkbox

The checkbox is created using:

```python id="c6n8vq"
self.checkbox = QCheckBox("Do you like food?", self)
```

This creates a checkbox with the text:

```text id="t5f4xq"
Do you like food?
```

## 📐 Setting the Checkbox Position

```python id="h2r8vz"
self.checkbox.setGeometry(100, 200, 500, 100)
```

The values represent:

```text id="n2d8sl"
100 → X position
200 → Y position
500 → Width
100 → Height
```

## 🔘 Setting the Initial State

```python id="y8q4nv"
self.checkbox.setChecked(False)
```

The checkbox starts in an **unchecked** state.

## 🔗 Connecting the Checkbox Signal

```python id="s7w3kj"
self.checkbox.stateChanged.connect(self.checkbox_changed)
```

This connects the checkbox's `stateChanged` signal to the `checkbox_changed()` function.

Whenever the checkbox state changes, the function is called.

## 🧩 Checking the Checkbox State

The function receives the current checkbox state:

```python id="c1m6py"
def checkbox_changed(self, state):
    if state == Qt.Checked:
        print("You like food")
    else:
        print("You don't like food")
```

If the state is:

```python id="g8v1zd"
Qt.Checked
```

the program prints:

```text id="s8f4cd"
You like food
```

Otherwise, it prints:

```text id="r5m2ka"
You don't like food
```

## 🎨 Styling the Checkbox

The checkbox can be styled using Qt Style Sheets.

The intended styling is:

```python id="j7q4kp"
self.checkbox.setStyleSheet(
    "font-size: 30px;"
    "font-family: Arial;"
)
```

This makes the checkbox text larger and changes its font to Arial.

## ⚠️ Troubleshooting

### 1. `front-size` is incorrect

Your code currently contains:

```python id="e3n7yt"
"front-size;30px;"
```

The correct property is:

```python id="x5k8qa"
"font-size: 30px;"
```

### 2. `front-family` is incorrect

Your code contains:

```python id="w4p2zn"
"front-family:Arial;"
```

The correct property is:

```python id="q9v6ma"
"font-family: Arial;"
```

Therefore, use:

```python id="p8r4cw"
self.checkbox.setStyleSheet(
    "font-size: 30px;"
    "font-family: Arial;"
)
```

### 3. PyQt5 Not Installed

If you receive:

```text id="v7m2kx"
ModuleNotFoundError: No module named 'PyQt5'
```

install PyQt5:

```bash id="f5q9bc"
pip install PyQt5
```

## 🚀 Future Improvements

This project can be improved by adding:

* 📝 A label showing the selected state
* ☑️ Multiple checkboxes
* 🔘 Radio buttons
* 🎨 Custom checkbox styling
* 🔊 Sound effects
* 💾 Saving user preferences
* 🖥️ A more advanced GUI layout
* 📊 Displaying selected preferences

## 🎯 Learning Objectives

This project helps beginners understand:

* Python GUI development
* PyQt5 fundamentals
* `QCheckBox`
* Signals and slots
* Event handling
* `Qt.Checked`
* Qt Style Sheets
* GUI positioning
* Object-oriented programming

## 👨‍💻 Author

**Gaurav G Salian**

B.Tech – Artificial Intelligence & Machine Learning

## 📄 License

This project is created for **educational and learning purposes**.
