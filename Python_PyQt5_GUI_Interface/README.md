# 🖥️ PyQt5 First GUI Application

A simple **Graphical User Interface (GUI) application built using Python and PyQt5**.

This beginner-friendly project demonstrates how to create a basic desktop window, set its title and size, and add a custom application icon using Python's `os` module.

## 📌 Project Overview

This project creates a simple desktop GUI window using the **PyQt5 framework**.

The application demonstrates:

* Creating a PyQt5 application
* Creating a main window using `QMainWindow`
* Setting a window title
* Setting the window size and position
* Adding a custom window icon
* Using `os.path` to create a reliable icon path
* Running the application using a `main()` function

## ✨ Features

* 🖥️ Simple desktop GUI
* 🪟 Custom window title
* 📐 Custom window size and position
* 🖼️ Custom application icon
* 🐍 Built entirely with Python
* 📁 Uses a relative path for the icon

## 🛠️ Technologies Used

* **Python 3**
* **PyQt5**
* **OS module**

## 📂 Project Structure

```text
PyQt5-First-GUI/
│
├── PyQt5_window.py
├── icon.png
|── README.md
├── Output.png
```

> Make sure `icon.png` is located in the same folder as `main.py`.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PyQt5-First-GUI.git
```

### 2. Navigate to the Project Directory

```bash
cd PyQt5-First-GUI
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

Run the Python file:

```bash
python main.py
```

A GUI window should appear with the title:

```text
My Cool first GUI
```

The window will have a size of:

```text
500 × 500
```

and a custom icon loaded from `icon.png`.

## 🧠 How the Code Works

### Importing Required Modules

```python
import sys
import os
```

`sys` is used to interact with the Python interpreter and handle application arguments.

`os` is used to construct the path to the icon file.

PyQt5 components are imported using:

```python
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
```

### Creating the Main Window

The `MainWindow` class inherits from `QMainWindow`:

```python
class MainWindow(QMainWindow):
```

This provides the basic functionality required for the application's main window.

### Setting the Window Title

```python
self.setWindowTitle("My Cool first GUI")
```

This sets the title displayed in the window's title bar.

### Setting Window Size and Position

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

### Setting the Window Icon

```python
icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
self.setWindowIcon(QIcon(icon_path))
```

Using `os.path.join()` and `__file__` ensures that Python looks for `icon.png` relative to the Python script's location.

This is more reliable than simply using:

```python
QIcon("icon.png")
```

## 🔍 Important

Make sure your project contains:

```text
main.py
icon.png
```

in the same directory.

For example:

```text
D:\Python_Projects\PyQt5-First-GUI\
│
├── main.py
└── icon.png
```

If `icon.png` is missing, the application may run without displaying the custom icon.

## 🚀 Future Improvements

This project can be expanded by adding:

* 🔘 Buttons
* 📝 Text boxes
* 📋 Labels
* 📑 Menus
* 🖼️ Images
* 🎨 Custom styling with Qt Style Sheets
* 📦 Multiple windows
* 🧮 Calculator functionality
* 📝 To-do list functionality
* 🔐 Login system

## 🎯 Learning Objectives

Through this project, you can learn the basics of:

* Python GUI development
* Object-oriented programming
* PyQt5
* Desktop application development
* File and directory handling
* Python application structure

## 👨‍💻 Author

**Gaurav G Salian**

B.Tech – Artificial Intelligence & Machine Learning

## 📄 License

This project is created for **educational and learning purposes**.
