# ⏱️ PyQt5 Stopwatch

A simple and interactive **Stopwatch GUI application built using Python and PyQt5**. The application allows users to start, stop, and reset a stopwatch with an easy-to-use graphical interface.

The stopwatch displays **hours, minutes, seconds, and hundredths of a second** and updates every 10 milliseconds.

## 📌 Project Overview

This project demonstrates how to build a functional stopwatch using PyQt5's `QTimer` and `QTime`.

The application provides three controls:

* ▶️ **Start** — Starts the stopwatch.
* ⏹️ **Stop** — Pauses the stopwatch.
* 🔄 **Reset** — Stops and resets the stopwatch to zero.

### Display Format

The stopwatch displays time in the following format:

```text
HH:MM:SS:MS
```

For example:

```text
00:05:23:47
```

Where:

* `HH` → Hours
* `MM` → Minutes
* `SS` → Seconds
* `MS` → Hundredths of a second

---

## ✨ Features

* ⏱️ Real-time stopwatch
* ▶️ Start functionality
* ⏹️ Stop/Pause functionality
* 🔄 Reset functionality
* 🕐 Hours, minutes, seconds, and milliseconds display
* ⚡ Updates every 10 milliseconds
* 🎨 Custom PyQt5 styling
* 🖥️ Simple graphical interface
* 🐍 Beginner-friendly project

---

## 🛠️ Technologies Used

* **Python 3**
* **PyQt5**
* `QApplication`
* `QWidget`
* `QVBoxLayout`
* `QHBoxLayout`
* `QLabel`
* `QPushButton`
* `QTimer`
* `QTime`
* `Qt`

---

## 📂 Project Structure

```text
PyQt5-Stopwatch/
│
├── PyQt5_Stopwatch.py
├── Output.png
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PyQt5-Stopwatch.git
```

Replace `your-username` with your GitHub username.

### 2. Navigate to the Project Directory

```bash
cd PyQt5-Stopwatch
```

### 3. Install PyQt5

```bash
pip install PyQt5
```

Or:

```bash
python -m pip install PyQt5
```

---

## ▶️ How to Run

Run the Python program:

```bash
python main.py
```

A stopwatch window will open.

The initial display will be:

```text
00:00:00:00
```

Click **Start** to begin counting.

Click **Stop** to pause the stopwatch.

Click **Reset** to return the stopwatch to:

```text
00:00:00:00
```

---

## 🖥️ Application Interface

The application contains:

```text
┌───────────────────────────────────────────┐
│                                           │
│             00:00:00:00                   │
│                                           │
│    ┌───────┐  ┌───────┐  ┌───────┐       │
│    │ Start │  │ Stop  │  │ Reset │       │
│    └───────┘  └───────┘  └───────┘       │
│                                           │
└───────────────────────────────────────────┘
```

---

## 🧠 How the Code Works

### 1. Creating the Stopwatch

The main class inherits from `QWidget`:

```python
class Stopwatch(QWidget):
```

The initial time is set to zero:

```python
self.time = QTime(0, 0, 0, 0)
```

A `QLabel` is used to display the stopwatch time:

```python
self.time_label = QLabel("00:00:00:00", self)
```

---

## ▶️ Start Button

The Start button is connected to the `start()` method:

```python
self.start_button.clicked.connect(self.start)
```

The stopwatch timer starts with:

```python
def start(self):
    self.timer.start(10)
```

The value `10` represents **10 milliseconds**.

Therefore, the `QTimer` triggers the update approximately every 10 milliseconds.

---

## ⏹️ Stop Button

The Stop button is connected to:

```python
self.stop_button.clicked.connect(self.stop)
```

The timer is stopped using:

```python
def stop(self):
    self.timer.stop()
```

This pauses the stopwatch without resetting the elapsed time.

---

## 🔄 Reset Button

The Reset button is connected to:

```python
self.reset_button.clicked.connect(self.reset)
```

The reset method stops the timer and sets the time back to zero:

```python
def reset(self):
    self.timer.stop()
    self.time = QTime(0, 0, 0, 0)
    self.time_label.setText(self.format_time(self.time))
```

---

## ⏱️ Updating the Time

The timer is connected to the `update_display()` method:

```python
self.timer.timeout.connect(self.update_display)
```

Every 10 milliseconds, this method is called:

```python
def update_display(self):
    self.time = self.time.addMSecs(10)
    self.time_label.setText(self.format_time(self.time))
```

The program adds 10 milliseconds to the current time and updates the label.

---

## 🕐 Formatting the Time

The `format_time()` function converts the `QTime` object into a readable format:

```python
def format_time(self, time):
    hours = time.hour()
    minutes = time.minute()
    seconds = time.second()
    milliseconds = int(time.msec() / 10)

    return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"
```

For example:

```text
QTime → 00 hours, 02 minutes, 15 seconds, 47 milliseconds
```

is displayed as:

```text
00:02:15:04
```

The final section represents **hundredths of a second**, not the full three-digit millisecond value.

---

## 🎨 GUI Styling

The project uses Qt Style Sheets to customize the interface:

```python
self.setStyleSheet("""
    QPushButton, QLabel {
        padding: 20px;
        font-weight: bold;
        font-family: Calibri;
    }

    QPushButton {
        font-size: 50px;
    }

    QLabel {
        font-size: 120px;
        background-color: hsl(200,100%,85%);
        border-radius: 20px;
    }
""")
```

### Styling Includes

* Large stopwatch display
* Calibri font
* Bold text
* Button padding
* Light-colored display background
* Rounded display corners

> **Note:** In your original code, `front-size:50px;` is written with `front-size`. The correct Qt Style Sheet property is **`font-size: 50px;`**.

---

## 📦 Layout Management

The project uses two layouts.

### Vertical Layout

```python
vbox = QVBoxLayout()
```

This organizes the main components vertically.

### Horizontal Layout

```python
hbox = QHBoxLayout()

hbox.addWidget(self.start_button)
hbox.addWidget(self.stop_button)
hbox.addWidget(self.reset_button)
```

This places the three buttons next to each other.

The resulting layout is:

```text
        Stopwatch
            │
            ▼
      Time Display
            │
            ▼
   Start | Stop | Reset
```

---

## 🔄 Program Flow

```text
             Start Application
                    │
                    ▼
            Create Stopwatch
                    │
                    ▼
             Display 00:00:00:00
                    │
                    ▼
              Click "Start"
                    │
                    ▼
             Start QTimer
                    │
                    ▼
            Add 10 milliseconds
                    │
                    ▼
             Update Display
                    │
                    └──────────────┐
                                   │
                                   ▼
                         Repeat every 10 ms
```

### Stop

```text
Click Stop
    │
    ▼
Stop QTimer
    │
    ▼
Pause Stopwatch
```

### Reset

```text
Click Reset
    │
    ▼
Stop QTimer
    │
    ▼
Set Time to 00:00:00:00
```

---

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

### Button Font Size Is Not Working

Make sure the property is:

```css
font-size: 50px;
```

and **not**:

```css
front-size: 50px;
```

### Stopwatch Does Not Start

Make sure the signal is connected:

```python
self.start_button.clicked.connect(self.start)
```

and the timer is started:

```python
self.timer.start(10)
```

### Stopwatch Does Not Update

Make sure the timer is connected to the update function:

```python
self.timer.timeout.connect(self.update_display)
```

---

## 🚀 Future Improvements

This project can be improved by adding:

* 🏁 Lap functionality
* 📋 Lap time history
* ⏱️ More accurate elapsed-time calculation
* 💾 Save lap times to a file
* 🔊 Start/stop sound effects
* 🌙 Dark mode
* 🎨 Multiple themes
* ⌨️ Keyboard shortcuts
* 📊 Lap time comparison
* 🖥️ Full-screen mode

### Possible Future Buttons

```text
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│ Start  │ │  Stop  │ │  Reset │ │   Lap  │
└────────┘ └────────┘ └────────┘ └────────┘
```

---

## 🎯 Learning Objectives

This project helps beginners understand:

* Python GUI development
* PyQt5 fundamentals
* `QTimer`
* `QTime`
* `QLabel`
* `QPushButton`
* `QVBoxLayout`
* `QHBoxLayout`
* Signals and slots
* Timer-based events
* GUI styling with QSS
* Time formatting
* Event-driven programming
* Object-oriented programming

---

## 👨‍💻 Author

**Gaurav G Salian**

B.Tech – Artificial Intelligence & Machine Learning

---

## 📄 License

This project is created for **educational and learning purposes**.
