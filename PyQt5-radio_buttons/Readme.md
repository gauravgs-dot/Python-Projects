# 🔘 PyQt5 Radio Button GUI

A simple **Graphical User Interface (GUI) application built using Python and PyQt5** that demonstrates how to use **radio buttons** and group them using `QButtonGroup`.

The application allows the user to select a **payment method** and a **purchase method**. The selected option is displayed in the terminal.

## 📌 Project Overview

This beginner-friendly project demonstrates the use of:

* `QRadioButton`
* `QButtonGroup`
* Signals and slots
* Event handling
* Qt Style Sheets
* `sender()` to identify the selected radio button

The application contains two groups of radio buttons.

### 💳 Payment Method

The user can select one option:

* Visa
* Mastercard
* Gift card

### 🛒 Purchase Method

The user can select one option:

* In-store
* Online

The selected option is printed in the terminal.

## ✨ Features

* 🔘 Multiple radio buttons
* 💳 Payment method selection
* 🛒 Purchase method selection
* 🔒 Only one option can be selected from each group
* 🖥️ Simple PyQt5 GUI
* 💬 Displays selected option in the terminal
* 🎨 Custom font and styling
* 🔗 Uses PyQt5 signals and slots

## 🛠️ Technologies Used

* **Python 3**
* **PyQt5**
* `QApplication`
* `QMainWindow`
* `QRadioButton`
* `QButtonGroup`

## 📂 Project Structure

```text
PyQt5-RadioButton-GUI/
│
├── PyQt5_radiobuttons.py
├── README.md
├── Output.png
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PyQt5-RadioButton-GUI.git
```

### 2. Navigate to the Project Directory

```bash
cd PyQt5-RadioButton-GUI
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

A GUI window will appear with the available radio buttons.

### 💳 Payment Options

```text
○ Visa
○ Mastercard
○ Gift card
```

### 🛒 Purchase Options

```text
○ In-store
○ Online
```

When an option is selected, the terminal displays something like:

```text
Visa is selected
```

or:

```text
Online is selected
```

## 🧠 How the Code Works

### 1. Import Required Libraries

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup
```

* `sys` → Used for application arguments.
* `QApplication` → Manages the GUI application.
* `QMainWindow` → Creates the main window.
* `QRadioButton` → Creates selectable radio buttons.
* `QButtonGroup` → Groups related radio buttons.

## 🔘 Creating Radio Buttons

The project creates five radio buttons:

```python
self.radio1 = QRadioButton("Visa", self)
self.radio2 = QRadioButton("Mastercard", self)
self.radio3 = QRadioButton("Gift card", self)
self.radio4 = QRadioButton("In-store", self)
self.radio5 = QRadioButton("Online", self)
```

## 📦 Creating Button Groups

Two separate button groups are created:

```python
self.button_group1 = QButtonGroup(self)
self.button_group2 = QButtonGroup(self)
```

### Payment Group

```python
self.button_group1.addButton(self.radio1)
self.button_group1.addButton(self.radio2)
self.button_group1.addButton(self.radio3)
```

This creates a payment selection group containing:

* Visa
* Mastercard
* Gift card

### Purchase Group

```python
self.button_group2.addButton(self.radio4)
self.button_group2.addButton(self.radio5)
```

This creates a purchase method group containing:

* In-store
* Online

This allows the user to select **one option from each group**.

## 🔗 Connecting Signals

Each radio button is connected to the same function:

```python
self.radio1.toggled.connect(self.radio_button_changed)
self.radio2.toggled.connect(self.radio_button_changed)
self.radio3.toggled.connect(self.radio_button_changed)
self.radio4.toggled.connect(self.radio_button_changed)
self.radio5.toggled.connect(self.radio_button_changed)
```

Whenever the state of a radio button changes, the `radio_button_changed()` function is called.

## 🧩 Detecting the Selected Radio Button

The program uses:

```python
radio_button = self.sender()
```

`sender()` identifies which radio button triggered the signal.

The program then checks whether it is selected:

```python
if radio_button and radio_button.isChecked():
    print(f"{radio_button.text()} is selected")
```

For example, selecting **Mastercard** prints:

```text
Mastercard is selected
```

## 🎨 Styling the Radio Buttons

The application uses Qt Style Sheets:

```python
self.setStyleSheet(
    "QRadioButton {"
    " font-size: 16px;"
    " font-family: Arial;"
    " padding: 10px;"
    "}"
)
```

This provides:

* Font size → `16px`
* Font family → `Arial`
* Padding → `10px`

## 📐 Setting Radio Button Positions

The radio buttons are positioned using `setGeometry()`:

```python
self.radio1.setGeometry(0, 0, 300, 50)
self.radio2.setGeometry(0, 50, 300, 50)
self.radio3.setGeometry(0, 100, 300, 50)
self.radio4.setGeometry(0, 150, 300, 50)
self.radio5.setGeometry(0, 200, 300, 50)
```

The values represent:

```text
X position
Y position
Width
Height
```

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

### Radio Buttons Not Grouping Correctly

Make sure the payment options are added to the same group:

```python
self.button_group1.addButton(self.radio1)
self.button_group1.addButton(self.radio2)
self.button_group1.addButton(self.radio3)
```

And the purchase options are added to the second group:

```python
self.button_group2.addButton(self.radio4)
self.button_group2.addButton(self.radio5)
```

## 🚀 Future Improvements

This project can be extended by adding:

* 💰 Display selected payment method inside the GUI
* 🛒 Add a "Submit" button
* 💳 Create a payment form
* 🧾 Generate a purchase summary
* 🎨 Improve the GUI design
* 🔄 Add a reset button
* 📋 Add more payment methods
* 💵 Add price and checkout functionality
* ✅ Validate the user's selections

## 🎯 Learning Objectives

This project helps beginners understand:

* Python GUI development
* PyQt5 fundamentals
* `QRadioButton`
* `QButtonGroup`
* Signals and slots
* Event handling
* `sender()`
* `isChecked()`
* `setGeometry()`
* Qt Style Sheets
* Object-oriented programming

## 👨‍💻 Author

**Gaurav G Salian**

B.Tech – Artificial Intelligence & Machine Learning

## 📄 License

This project is created for **educational and learning purposes**.
