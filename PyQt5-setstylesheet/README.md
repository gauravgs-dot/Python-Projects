🎨 PyQt5 Styled Buttons GUI

A simple Graphical User Interface (GUI) application built using Python and PyQt5. This project demonstrates how to create multiple buttons, arrange them horizontally using QHBoxLayout, and customize their appearance using Qt Style Sheets (QSS).

Each button has a unique color and a different hover effect.

📌 Project Overview

This project is designed for beginners learning PyQt5 GUI development.

The application creates three buttons:

🔘 #1
🔘 #2
🔘 #3

The buttons are arranged horizontally and styled with different background colors. When the user moves the mouse over a button, its background color changes.

✨ Features
🖥️ Simple PyQt5 desktop GUI
🔘 Three custom buttons
↔️ Horizontal layout using QHBoxLayout
🎨 Different colors for each button
🖱️ Hover effects
🔤 Custom Arial font
📐 Rounded corners
🧱 Custom borders
📏 Custom padding and margins
🎯 Individual button styling using object names
🛠️ Technologies Used
Python 3
PyQt5
QApplication
QMainWindow
QPushButton
QWidget
QHBoxLayout
Qt Style Sheets (QSS)
📂 Project Structure
PyQt5-Styled-Buttons/
│
├── PyQt5_setstylesheet.py
├── README.md
├── Output.png
⚙️ Installation
1. Clone the Repository
git clone https://github.com/your-username/PyQt5-Styled-Buttons.git

Replace your-username with your GitHub username.

2. Navigate to the Project
cd PyQt5-Styled-Buttons
3. Install PyQt5
pip install PyQt5

Or:

python -m pip install PyQt5
▶️ How to Run

Run the application using:

python main.py

A GUI window will open containing three buttons:

┌──────────┐    ┌──────────┐    ┌──────────┐
│    #1    │    │    #2    │    │    #3    │
└──────────┘    └──────────┘    └──────────┘

Move the mouse over each button to see its hover effect.

🧠 How the Code Works
1. Import Required Libraries
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QHBoxLayout
)
sys → Used for application arguments.
QApplication → Manages the GUI application.
QMainWindow → Creates the main window.
QPushButton → Creates buttons.
QWidget → Provides the central widget.
QHBoxLayout → Arranges widgets horizontally.
2. Create the Buttons

Three buttons are created:

self.button1 = QPushButton("#1")
self.button2 = QPushButton("#2")
self.button3 = QPushButton("#3")

Each button displays a different label.

3. Create the Central Widget
central_widget = QWidget()
self.setCentralWidget(central_widget)

The central widget provides an area where the buttons and layouts can be placed.

4. Create a Horizontal Layout
hbox = QHBoxLayout()

hbox.addWidget(self.button1)
hbox.addWidget(self.button2)
hbox.addWidget(self.button3)

central_widget.setLayout(hbox)

QHBoxLayout automatically arranges the three buttons from left to right.

#1  →  #2  →  #3
🏷️ Using Object Names

Each button is assigned a unique object name:

self.button1.setObjectName("button1")
self.button2.setObjectName("button2")
self.button3.setObjectName("button3")

These names allow individual buttons to be customized using Qt Style Sheets.

For example:

QPushButton#button1 {
    background-color: hsl(120, 100%, 30%);
}

This style applies only to button1.

🎨 Styling with Qt Style Sheets

The project uses setStyleSheet() to customize the buttons:

self.setStyleSheet("""
    QPushButton {
        font-size: 40px;
        font-family: Arial;
        padding: 25px;
        margin: 25px;
        border: 3px solid;
        border-radius: 15px;
    }
""")
Styling Properties
Property	Purpose
font-size	Controls the text size
font-family	Sets the font
padding	Adds space inside the button
margin	Adds space around the button
border	Sets the border
border-radius	Creates rounded corners
background-color	Changes the button color
🌈 Button Colors

Each button has its own background color.

🟢 Button #1
QPushButton#button1 {
    background-color: hsl(120, 100%, 30%);
}
🔴 Button #2
QPushButton#button2 {
    background-color: hsl(0, 100%, 50%);
}
🔵 Button #3
QPushButton#button3 {
    background-color: hsl(204, 100%, 50%);
}
🖱️ Hover Effects

The project uses the :hover selector to change the button color when the mouse moves over it.

Button #1
QPushButton#button1:hover {
    background-color: hsl(156, 100%, 50%);
}
Button #2
QPushButton#button2:hover {
    background-color: hsl(0, 100%, 75%);
}
Button #3
QPushButton#button3:hover {
    background-color: hsl(200, 100%, 75%);
}

This makes the interface more interactive.

🔍 Understanding QSS Selectors
Style all buttons
QPushButton {
    font-size: 40px;
}

This applies to every QPushButton.

Style one specific button
QPushButton#button1 {
    background-color: green;
}

This applies only to the button with the object name button1.

Style a button when hovered
QPushButton#button1:hover {
    background-color: lightgreen;
}

This applies when the mouse pointer is over button1.

⚠️ Troubleshooting
PyQt5 Not Installed

If you get:

ModuleNotFoundError: No module named 'PyQt5'

install PyQt5:

pip install PyQt5
Buttons Are Not Arranged Horizontally

Make sure you are using:

hbox = QHBoxLayout()

and adding all buttons:

hbox.addWidget(self.button1)
hbox.addWidget(self.button2)
hbox.addWidget(self.button3)
Individual Styling Does Not Work

Make sure each button has an object name:

self.button1.setObjectName("button1")

The name in your stylesheet must match the object name exactly:

QPushButton#button1 {
    background-color: green;
}
🚀 Future Improvements

This project can be expanded by adding:

🖱️ Click events for each button
💬 Display messages when buttons are clicked
🔢 Button click counter
🔄 Reset button
🔊 Sound effects
🖼️ Icons on buttons
✨ More advanced animations
🌙 Dark mode
🎨 Multiple themes
📱 Responsive layouts

For example, button #1 could be connected to a function:

self.button1.clicked.connect(self.button1_clicked)

def button1_clicked(self):
    print("Button #1 clicked!")
🎯 Learning Objectives

This project helps beginners understand:

Python GUI development
PyQt5 fundamentals
QPushButton
QWidget
QHBoxLayout
Layout management
Object names
Qt Style Sheets (QSS)
CSS-like selectors
Hover effects
Button customization
Object-oriented programming
👨‍💻 Author

Gaurav G Salian

B.Tech – Artificial Intelligence & Machine Learning

📄 License

This project is created for educational and learning purposes