# 🖼️ PyQt5 Image Viewer

A simple **Image Viewer GUI application built using Python and PyQt5**. This project demonstrates how to create a desktop window and display an image inside it using the `QLabel` and `QPixmap` classes.

The project also demonstrates how to use Python's `os` module to create a reliable path to the image file.

## 📌 Project Overview

This beginner-friendly project creates a PyQt5 window and displays an image in the center of the window.

The application demonstrates:

* Creating a GUI using PyQt5
* Creating a window using `QMainWindow`
* Displaying images using `QLabel`
* Loading images using `QPixmap`
* Scaling images to fit a label
* Centering an image inside a window
* Creating file paths using `os.path`
* Checking whether an image was loaded successfully

## ✨ Features

* 🖥️ Simple desktop GUI
* 🖼️ Displays an image inside the application
* 📐 Automatically scales the image to the label size
* 🎯 Centers the image in the window
* ✅ Checks whether the image was loaded successfully
* 📁 Uses a relative path for the image

## 🛠️ Technologies Used

* **Python 3**
* **PyQt5**
* `sys`
* `os`

## 📂 Project Structure

```text
PyQt5-Image-Viewer/
│
├── PyQt5_images.py
├── icon.png
├── README.md
├── Output.png
```

> **Important:** Make sure `icon.png` is in the same folder as `PyQt5_images.py`.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PyQt5-Image-Viewer.git
```

### 2. Navigate to the Project Directory

```bash
cd PyQt5-Image-Viewer
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

A window will open with the `icon.png` image displayed in the center.

## 🧠 How It Works

### 1. Import Required Libraries

```python
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
```

* `sys` → Used to handle application arguments.
* `os` → Used to create the image file path.
* `QApplication` → Manages the GUI application.
* `QMainWindow` → Creates the main application window.
* `QLabel` → Used to display the image.
* `QPixmap` → Used to load and display images.

### 2. Create the Main Window

```python
class MainWindow(QMainWindow):
```

The `MainWindow` class inherits from `QMainWindow`, providing the basic structure for the application window.

### 3. Set Window Size

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

### 4. Create a QLabel

```python
label1 = QLabel(self)
label1.setGeometry(0, 0, 250, 250)
```

The `QLabel` is used as a container for displaying the image.

### 5. Create the Image Path

```python
image_path = os.path.join(
    os.path.dirname(__file__),
    "icon.png"
)
```

This creates the path to `icon.png` relative to the location of the Python file.

This is useful because the program does not depend on a hard-coded path such as:

```text
D:\Python_Projects\PyQt5-Image-Viewer\icon.png
```

### 6. Load the Image

```python
pixmap = QPixmap(image_path)
```

`QPixmap` loads the image from the specified path.

### 7. Check Whether the Image Loaded

```python
print("Image loaded:", not pixmap.isNull())
print("Image path:", image_path)
```

If the image loads successfully, the console will display:

```text
Image loaded: True
```

If the image cannot be found or loaded:

```text
Image loaded: False
```

### 8. Display the Image

```python
label1.setPixmap(pixmap)
```

This places the loaded image inside the `QLabel`.

### 9. Scale the Image

```python
label1.setScaledContents(True)
```

This allows the image to scale according to the size of the label.

### 10. Center the Image

The following code calculates the position required to place the image in the center of the window:

```python
label1.setGeometry(
    (self.width() - label1.width()) // 2,
    (self.height() - label1.height()) // 2,
    label1.width(),
    label1.height()
)
```

This ensures that the image is positioned approximately in the center of the application window.

## 🖼️ Image Requirements

The project expects an image named:

```text
icon.png
```

The project should look like:

```text
PyQt5-Image-Viewer/
│
├── main.py
└── icon.png
```

You can use another image by changing:

```python
"icon.png"
```

to the name of your image:

```python
"my_image.jpg"
```

## 🐛 Troubleshooting

### Image Not Displaying

If the console shows:

```text
Image loaded: False
```

check that:

1. The image exists.
2. The filename is exactly `icon.png`.
3. The image is in the same folder as `main.py`.
4. The image extension is correct.

For example:

```text
icon.png
```

is different from:

```text
Icon.png
icon.jpg
icon.jpeg
icon.png.png
```

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

This project can be extended by adding:

* ⬅️ Previous/Next image buttons
* 🔍 Zoom in and Zoom out
* 🔄 Rotate image
* 📂 Open image using a file dialog
* 💾 Save images
* 🖼️ Image slideshow
* 🎨 GUI styling
* 🖱️ Drag-and-drop image support
* 📁 Support for multiple image formats

## 🎯 Learning Objectives

This project helps beginners understand:

* Python GUI development
* PyQt5 basics
* Object-oriented programming
* `QMainWindow`
* `QLabel`
* `QPixmap`
* Image handling
* File paths using Python
* Basic GUI positioning

## 👨‍💻 Author

**Gaurav G Salian**

B.Tech – Artificial Intelligence & Machine Learning

## 📄 License

This project is created for **educational and learning purposes**.
