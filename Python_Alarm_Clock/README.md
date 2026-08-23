# ⏰ Python Alarm Clock

A simple **Alarm Clock application built with Python** that allows the user to set an alarm for a specific time in `HH:MM:SS` format. When the system time matches the specified alarm time, the application plays an alarm sound using the **Pygame** library.

## 📌 Project Overview

This project is a beginner-friendly Python application that demonstrates how to work with:

* Python date and time
* User input
* Loops and conditional statements
* The `datetime` module
* The `time` module
* Audio playback using `pygame`

The program continuously checks the current system time until it matches the alarm time entered by the user.

## ✨ Features

* ⏰ Set an alarm using `HH:MM:SS` format
* 🕐 Displays the current time while waiting
* 🔊 Plays an MP3 alarm sound when the specified time is reached
* 🛑 Automatically stops after the alarm finishes playing
* 🐍 Simple and beginner-friendly Python implementation

## 🛠️ Technologies Used

* **Python 3**
* **Pygame**
* `datetime`
* `time`

## 📂 Project Structure

```text
Python-Alarm-Clock/
│
├── alarm_clock.py
├── alarm_sound.mp3
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Python-Alarm-Clock.git
```

### 2. Navigate to the Project Directory

```bash
cd Python-Alarm-Clock
```

### 3. Install Pygame

Install the required Python package using:

```bash
pip install pygame
```

## ▶️ How to Run

Run the Python program:

```bash
python alarm_clock.py
```

The program will ask you to enter the alarm time:

```text
Enter the alarm time (HH:MM:SS):
```

For example:

```text
Enter the alarm time (HH:MM:SS): 17:30:00
```

The program will continuously display the current time:

```text
Alarm set for 17:30:00
17:29:55
17:29:56
17:29:57
...
```

When the specified time is reached:

```text
Wake Up! ⏰
```

The `alarm_sound.mp3` file will then be played.

## 🔊 Adding Your Own Alarm Sound

Place an MP3 file named:

```text
alarm_sound.mp3
```

in the same directory as `alarm_clock.py`.

You can also use a different filename by changing this line in the Python code:

```python
sound_file = "alarm_sound.mp3"
```

For example:

```python
sound_file = "my_alarm.mp3"
```

## 🧠 How It Works

The program follows these basic steps:

1. The user enters an alarm time.
2. The program gets the current system time using `datetime`.
3. The current time is converted into `HH:MM:SS` format.
4. The program compares the current time with the alarm time.
5. If both times match, the alarm sound is loaded using Pygame.
6. The alarm sound is played.
7. The program waits until the sound finishes.
8. The program then exits.

## 📚 Python Concepts Used

### `datetime`

Used to obtain the current system time:

```python
datetime.datetime.now().strftime("%H:%M:%S")
```

### `time`

Used to pause the program for one second:

```python
time.sleep(1)
```

### `pygame`

Used to initialize the audio system, load the alarm sound, and play it:

```python
pygame.mixer.init()
pygame.mixer.music.load(sound_file)
pygame.mixer.music.play()
```

## ⚠️ Important Notes

* Enter the alarm time exactly in `HH:MM:SS` format.
* Use **24-hour time format**.
* Make sure `alarm_sound.mp3` exists in the project directory.
* Pygame must be installed before running the application.
* The program needs to remain running until the alarm time is reached.

## 🚀 Future Improvements

Some possible improvements for this project are:

* Add a graphical user interface using **Tkinter**
* Allow users to select an alarm sound
* Add multiple alarms
* Add a snooze option
* Add a stop/dismiss button
* Display a digital clock
* Allow users to cancel the alarm
* Add date-based alarms
* Create a desktop application

## 👨‍💻 Author

**Gaurav G Salian**

B.Tech – Artificial Intelligence & Machine Learning

## 📄 License

This project is created for **educational and learning purposes**.
