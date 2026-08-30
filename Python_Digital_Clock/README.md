# 🕐 PyQt5 Digital Clock

A simple **Digital Clock GUI application built using Python and PyQt5**. The application displays the current system time in a digital format and automatically updates every second.

This project demonstrates the use of **QTimer, QTime, QLabel, QVBoxLayout, QFont, and Qt alignment** in PyQt5.

## 📌 Project Overview

The Digital Clock displays the current time in the following format:

```text
HH:MM:SS AM/PM
```

For example:

```text
03:21:45 PM
```

The clock automatically updates every **1 second**, ensuring that the displayed time stays synchronized with the system clock.

## ✨ Features

* 🕐 Real-time digital clock
* ⏱️ Updates every second
* 🖥️ Simple desktop GUI
* 🟢 Green digital-style text
* ⚫ Black background
* 🔤 Large Arial font
* 🎯 Center-aligned time
* 📐 Clean and minimal interface
* 🐍 Beginner-friendly Python project

## 🛠️ Technologies Used

* **Python 3**
* **PyQt5**
* `QApplication`
* `QWidget`
* `QVBoxLayout`
* `QLabel`
* `QTimer`
* `QTime`
* `QFont`
* `Qt`

## 📂 Project Structure

```text
PyQt5-Digital-Clock/
│
├── PyQt5_Digital_Clock.py
├── Output.png
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PyQt5-Digital-Clock.git
```

Replace `your-username` with your GitHub username.

### 2. Navigate to the Project Directory

```bash
cd PyQt5-Digital-Clock
```

### 3. Install PyQt5

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

A window will open displaying the current time.

Example:

```text
┌──────────────────────────────────┐
│                                  │
│          03:21:45 PM             │
│                                  │
└──────────────────────────────────┘
```

The displayed time will automatically update every second.

## 🧠 How the Code Works

### 1. Import Required Libraries

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont
```

* `sys` → Used to handle application arguments.
* `QApplication` → Manages the GUI application.
* `QWidget` → Provides the base window.
* `QVBoxLayout` → Arranges widgets vertically.
* `QLabel` → Displays the current time.
* `QTimer` → Executes a function at regular intervals.
* `QTime` → Retrieves the current system time.
* `Qt` → Provides alignment options.
* `QFont` → Customizes the text font.

## 🪟 Creating the Digital Clock

The main class inherits from `QWidget`:

```python
class DigitalClock(QWidget):
```

Two important objects are created:

```python
self.time_label = QLabel(self)
self.timer = QTimer(self)
```

`time_label` displays the current time, while `timer` is responsible for updating it.

## 📐 Setting the Window

```python
self.setWindowTitle("Digital Clock")
self.setGeometry(600, 400, 400, 150)
```

The window title is set to:

```text
Digital Clock
```

The geometry values represent:

```text
600 → X position
400 → Y position
400 → Width
150 → Height
```

## 📦 Using QVBoxLayout

```python
vbox = QVBoxLayout()
vbox.addWidget(self.time_label)
self.setLayout(vbox)
```

`QVBoxLayout` places the time label inside the window using a vertical layout.

## 🎯 Centering the Time

```python
self.time_label.setAlignment(Qt.AlignCenter)
```

This centers the clock text inside the label.

## 🔤 Setting the Font

```python
self.time_label.setFont(QFont("Arial", 48))
```

This sets:

* Font → **Arial**
* Font size → **48**

The large font makes the digital clock easier to read.

## 🎨 Styling the Clock

The time label is styled using Qt Style Sheets:

```python
self.time_label.setStyleSheet(
    "font-size:48px;"
    "font-family: Arial;"
    "color: hsl(111,100%,50%);"
)
```

The text is displayed in a bright green color.

The window background is set to black:

```python
self.setStyleSheet("background-color: black;")
```

This creates a simple digital-clock appearance.

## ⏱️ Updating the Clock

The timer is connected to the `update_time()` function:

```python
self.timer.timeout.connect(self.update_time)
```

The timer starts with:

```python
self.timer.start(1000)
```

`1000` milliseconds equals **1 second**.

Therefore, `update_time()` is called every second.

## 🕐 Getting the Current Time

The current system time is obtained using:

```python
current_time = QTime.currentTime().toString("hh:mm:ss AP")
```

The format:

```text
hh:mm:ss AP
```

means:

| Format | Meaning |
| ------ | ------- |
| `hh`   | Hour    |
| `mm`   | Minute  |
| `ss`   | Second  |
| `AP`   | AM/PM   |

For example:

```text
03:21:45 PM
```

## 🔄 Updating the Label

The current time is displayed using:

```python
self.time_label.setText(current_time)
```

This updates the label with the latest time.

The program also calls:

```python
self.update_time()
```

when the application starts so the time appears immediately instead of waiting for the first timer interval.

## 🔁 Program Flow

```text
Start Application
       │
       ▼
Create Digital Clock Window
       │
       ▼
Create QLabel
       │
       ▼
Create QTimer
       │
       ▼
Get Current System Time
       │
       ▼
Display Time
       │
       ▼
Wait 1 Second
       │
       ▼
Update Time
       │
       └──────────────► Repeat
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

### Clock Is Not Updating

Make sure the timer is connected correctly:

```python
self.timer.timeout.connect(self.update_time)
```

and started:

```python
self.timer.start(1000)
```

### Time Format

If you want a 24-hour clock instead, you can use:

```python
QTime.currentTime().toString("HH:mm:ss")
```

Example:

```text
15:21:45
```

For a 12-hour clock with AM/PM, use:

```python
QTime.currentTime().toString("hh:mm:ss AP")
```

## 🚀 Future Improvements

This project can be extended by adding:

* 📅 Current date
* 🌍 Multiple time zones
* 🌙 Dark/light mode
* 🎨 Custom clock colors
* 🔤 Digital clock-style fonts
* ⏰ Alarm functionality
* ⏱️ Stopwatch
* ⏲️ Countdown timer
* 🌎 World clock
* 🖥️ Full-screen clock mode
* ⚙️ User-selectable time formats

## 🎯 Learning Objectives

This project helps beginners understand:

* Python GUI development
* PyQt5 fundamentals
* `QTimer`
* `QTime`
* `QLabel`
* `QVBoxLayout`
* Signals and slots
* Timer-based events
* Qt Style Sheets
* Font customization
* GUI alignment
* Real-time GUI updates

## 👨‍💻 Author

**Gaurav G Salian**

B.Tech – Artificial Intelligence & Machine Learning

## 📄 License

This project is created for **educational and learning purposes**.
