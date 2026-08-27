# 🖥️ PyQt5 Button and Label GUI

A simple **Graphical User Interface (GUI) application built using Python and PyQt5**.

This beginner-friendly project demonstrates how to create a window containing a **button and a label**, and how to change the label text when the button is clicked.

## 📌 Project Overview

The application creates a basic PyQt5 window with:

* 🔘 A **"Click me!"** button
* 🏷️ A **"Hello"** label
* 🖱️ A button click event
* 🔄 Dynamic label text modification

When the user clicks the button, the label changes from:

```text
Hello
```

to:

```text
Goodbye
```

## ✨ Features

* 🖥️ Simple desktop GUI
* 🔘 Interactive button
* 🏷️ Text label
* 🖱️ Button click event handling
* 🔄 Dynamically changes label text
* 🎨 Basic GUI styling using Qt Style Sheets
* 🐍 Built with Python

## 🛠️ Technologies Used

* **Python 3**
* **PyQt5**
* `QApplication`
* `QMainWindow`
* `QPushButton`
* `QLabel`

## 📂 Project Structure

```text
PyQt5-Button-Label/
│
├── PyQt5-pushbutton-display.py
├── README.md
├── Output.png
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PyQt5-Button-Label.git
```

### 2. Navigate to the Project Directory

```bash
cd PyQt5-Button-Label
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

A GUI window will appear containing the button and label.

### Before Clicking

```text
Hello
```

### After Clicking "Click me!"

```text
Goodbye
```

## 🧠 How the Code Works

### 1. Import Required Libraries

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
```

* `sys` → Used for application arguments.
* `QApplication` → Manages the GUI application.
* `QMainWindow` → Creates the main window.
* `QPushButton` → Creates the clickable button.
* `QLabel` → Displays text.

### 2. Create the Main Window

```python
class MainWindow(QMainWindow):
```

The `MainWindow` class inherits from `QMainWindow`.

The window size is set using:

```python
self.setGeometry(700, 300, 500, 500)
```

The values represent:

```text
700 → X position
300 → Y position
500 → Width
500 → Height
```

### 3. Create the Button

```python
self.button = QPushButton("Click me!", self)
```

This creates a button with the text:

```text
Click me!
```

### 4. Create the Label

```python
self.label = QLabel("Hello", self)
```

This creates a label displaying:

```text
Hello
```

### 5. Connect the Button to a Function

```python
self.button.clicked.connect(self.on_click)
```

This connects the button's `clicked` signal to the `on_click()` function.

Whenever the button is clicked, `on_click()` is executed.

### 6. Change the Label Text

```python
def on_click(self):
    self.label.setText("Goodbye")
```

The `setText()` method changes the label from:

```text
Hello
```

to:

```text
Goodbye
```

## 🎨 GUI Styling

The project uses Qt Style Sheets to customize the appearance of the widgets.

For example:

```python
self.button.setStyleSheet("font-size: 30px;")
```

This increases the button's font size.

Similarly:

```python
self.label.setStyleSheet("font-size: 50px;")
```

increases the label's font size.

## ⚠️ Troubleshooting

### Font Size Not Changing

Make sure you use:

```python
font-size
```

and **not**:

```python
front_size
```

The correct code is:

```python
self.button.setStyleSheet("font-size: 30px;")
self.label.setStyleSheet("font-size: 50px;")
```

Your original code contains:

```python
"front_size:30px;"
```

which is a typo.

### PyQt5 Not Installed

If you get:

```text
ModuleNotFoundError: No module named 'PyQt5'
```

install PyQt5:

```bash
pip install PyQt5
```

## 🚀 Future Improvements

This simple project can be expanded by adding:

* 🔄 A reset button
* 🔢 Click counter
* 🎨 Different button colors
* 🌙 Dark mode
* 🖼️ Images
* 🔊 Sound effects
* ✏️ Text input fields
* 🔘 Multiple buttons
* 🧮 Calculator functionality
* 🎯 Random messages on every click

## 🎯 Learning Objectives

This project helps beginners understand:

* Python GUI development
* PyQt5 fundamentals
* Classes and objects
* `QMainWindow`
* `QPushButton`
* `QLabel`
* Signals and slots
* Event handling
* Qt Style Sheets
* Dynamic GUI updates

## 👨‍💻 Author

**Gaurav G Salian**

B.Tech – Artificial Intelligence & Machine Learning

## 📄 License

This project is created for **educational and learning purposes**.
