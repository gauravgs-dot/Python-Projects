# 🎨 PyQt5 Styled Label GUI

A simple **Graphical User Interface (GUI) application built using Python and PyQt5** that demonstrates how to create and style a text label using custom fonts, colors, alignment, and Qt Style Sheets.

This project is designed for beginners who are learning the fundamentals of **Python GUI development with PyQt5**.

## 📌 Project Overview

The application creates a `500 × 500` desktop window containing a centered **"Hello"** label.

The label is customized with:

* 🔤 Arial font
* 📏 40px font size
* 🎨 Custom text color
* 🟢 Custom background color
* **Bold** text
* *Italic* text
* <u>Underlined</u> text
* 📍 Center alignment

## ✨ Features

* 🖥️ Simple PyQt5 desktop application
* 🔤 Custom font using `QFont`
* 🎨 Text and background colors
* **Bold font styling**
* *Italic font styling*
* <u>Underline text</u>
* 🎯 Centered label
* 📐 Fixed window size
* 🐍 Beginner-friendly Python code

## 🛠️ Technologies Used

* **Python 3**
* **PyQt5**
* `QApplication`
* `QMainWindow`
* `QLabel`
* `QFont`
* `Qt`

## 📂 Project Structure

```text id="q8v7xn"
PyQt5-Styled-Label/
│
├── PyQt5_Qlabels.py
├── README.md
├── Output.png
```

## ⚙️ Installation

### 1. Clone the Repository

```bash id="4rjzv2"
git clone https://github.com/your-username/PyQt5-Styled-Label.git
```

### 2. Navigate to the Project Directory

```bash id="2iy8ga"
cd PyQt5-Styled-Label
```

### 3. Install PyQt5

Install PyQt5 using pip:

```bash id="gjx6ce"
pip install PyQt5
```

Or:

```bash id="f2wwyo"
python -m pip install PyQt5
```

## ▶️ How to Run

Run the Python program:

```bash id="v9v9xz"
python main.py
```

A GUI window will open displaying the styled **Hello** text in the center.

## 🧠 How the Code Works

### 1. Import Required Libraries

```python id="l7c5qv"
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
```

* `sys` → Used to handle application arguments.
* `QApplication` → Manages the GUI application.
* `QMainWindow` → Creates the main application window.
* `QLabel` → Displays text.
* `QFont` → Used to customize the font.
* `Qt` → Provides alignment options.

## 🔤 Setting the Font

The font is created using:

```python id="3v7jnt"
label.setFont(QFont("Arial", 40))
```

This sets:

* Font family → **Arial**
* Font size → **40**

## 📐 Setting the Label Geometry

```python id="u2b5c4"
label.setGeometry(0, 0, 500, 100)
```

The values represent:

```text id="u1h2p0"
0   → X position
0   → Y position
500 → Width
100 → Height
```

## 🎨 Styling the Label

The project uses Qt Style Sheets to customize the label:

```python id="n4w1c5"
label.setStyleSheet(
    "color:#ff5733;"
    "background-color:#d1f2eb;"
    "font-weight:bold;"
    "font-style:italic;"
    "text-decoration:underline;"
)
```

### Styling Explained

| Property           | Purpose                      |
| ------------------ | ---------------------------- |
| `color`            | Changes the text color       |
| `background-color` | Changes the label background |
| `font-weight`      | Makes the text bold          |
| `font-style`       | Makes the text italic        |
| `text-decoration`  | Underlines the text          |

## 🎯 Centering the Text

The label text is centered using:

```python id="2u8w3j"
label.setAlignment(Qt.AlignCenter)
```

`Qt.AlignCenter` centers the text both horizontally and vertically within the label.

## 🖥️ Expected Output

The application displays:

```text id="2gk67j"
┌─────────────────────────────────────────┐
│                                         │
│               Hello                     │
│                                         │
└─────────────────────────────────────────┘
```

The actual GUI contains a colored background with large, bold, italic, and underlined text.

## ⚠️ Troubleshooting

### PyQt5 Not Installed

If you receive:

```text id="k6mxkj"
ModuleNotFoundError: No module named 'PyQt5'
```

install PyQt5:

```bash id="e3qjv2"
pip install PyQt5
```

### Font Not Available

If Arial is not available on your system, you can replace it with another installed font:

```python id="5kz8iz"
label.setFont(QFont("Times New Roman", 40))
```

or:

```python id="q5j3m6"
label.setFont(QFont("Courier New", 40))
```

## 🚀 Future Improvements

This project can be extended by adding:

* 🔘 Buttons
* 📝 Text input fields
* 🖼️ Images
* 🎨 Multiple labels with different styles
* 🌙 Dark mode
* 📑 Menus
* 🔄 Dynamic text changes
* 🎨 User-selectable colors and fonts
* 📐 Responsive layouts

## 🎯 Learning Objectives

This project helps beginners understand:

* Python GUI development
* PyQt5 basics
* `QMainWindow`
* `QLabel`
* `QFont`
* Qt alignment
* Qt Style Sheets (QSS)
* GUI positioning
* Font customization
* Text styling

## 👨‍💻 Author

**Gaurav G Salian**

B.Tech – Artificial Intelligence & Machine Learning

## 📄 License

This project is created for **educational and learning purposes**.
