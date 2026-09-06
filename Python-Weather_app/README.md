# 🌤️ PyQt5 Weather App

A simple and interactive **Weather Application built using Python, PyQt5, and the OpenWeatherMap API**.

The application allows users to enter a city name and retrieve the current weather information, including **temperature, weather condition, and a corresponding weather emoji**.

---

## 📌 Project Overview

This project demonstrates how to build a GUI-based weather application using **PyQt5** and how to retrieve real-time weather data from an external REST API.

The user enters a city name and clicks the **Get Weather** button.

The application then displays:

* 🌡️ Current temperature
* 🌤️ Weather condition
* 😀 Weather emoji
* ⚠️ Error messages when something goes wrong

### Example

If the user enters:

```text
Udupi
```

The application may display:

```text
                 82°F
                  ☁️
             Broken clouds
```

The exact weather information depends on the current conditions returned by the API.

---

## ✨ Features

* 🌍 Search weather by city name
* 🌡️ Displays current temperature
* 🇺🇸 Displays temperature in Fahrenheit
* 🌤️ Displays weather description
* 😀 Weather-specific emojis
* 🔌 Uses OpenWeatherMap API
* ⚠️ Handles HTTP errors
* 🌐 Handles internet connection errors
* ⏱️ Handles request timeouts
* 🔄 Handles API request failures
* 🎨 Custom PyQt5 styling
* 🖥️ Simple and beginner-friendly GUI

---

## 🛠️ Technologies Used

* **Python 3**
* **PyQt5**
* **Requests**
* **OpenWeatherMap API**

### Python Libraries

```text
PyQt5
requests
```

---

## 📂 Project Structure

```text
PyQt5-Weather-App/
│
├── Weather_app.py
├── Output.png
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PyQt5-Weather-App.git
```

Replace `your-username` with your GitHub username.

### 2. Navigate to the Project Directory

```bash
cd PyQt5-Weather-App
```

### 3. Install Required Libraries

Install PyQt5:

```bash
pip install PyQt5
```

Install Requests:

```bash
pip install requests
```

Or install both at once:

```bash
pip install PyQt5 requests
```

---

# 🔑 OpenWeatherMap API Key

This application requires an **OpenWeatherMap API key** to retrieve weather data.

You can create an account and obtain an API key from OpenWeatherMap.

**Important:** Never upload your API key directly to GitHub.

### ❌ Do NOT do this

```python
api_key = "YOUR_API_KEY"
```

Instead, use an environment variable.

### ✅ Recommended approach

Install `python-dotenv`:

```bash
pip install python-dotenv
```

Create a `.env` file:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

Then load the key in Python:

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
```

Add `.env` to your `.gitignore` file:

```text
.env
```

This prevents your API key from being uploaded to GitHub.

> **Security note:** If the API key shown in your original code is real and still active, revoke or rotate it before publishing the repository.

---

## ▶️ How to Run

After installing the dependencies and configuring your API key:

```bash
python main.py
```

The Weather App window will open.

Enter a city name:

```text
Enter city name:
[ Udupi                         ]

[       Get Weather             ]
```

The application will retrieve the weather information and display it.

---

## 🖥️ Application Interface

The application contains:

```text
┌──────────────────────────────────────┐
│                                      │
│          Enter city name:            │
│                                      │
│       [ Enter city name ]             │
│                                      │
│          [ Get Weather ]             │
│                                      │
│              82°F                    │
│                                      │
│               ☁️                     │
│                                      │
│          Broken clouds               │
│                                      │
└──────────────────────────────────────┘
```

---

# 🧠 How the Code Works

## 1. Import Required Libraries

```python
import sys
import requests

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)

from PyQt5.QtCore import Qt
```

### Main Components

| Component      | Purpose                                |
| -------------- | -------------------------------------- |
| `QApplication` | Runs the GUI application               |
| `QWidget`      | Creates the main window                |
| `QLabel`       | Displays text and weather information  |
| `QLineEdit`    | Accepts the city name                  |
| `QPushButton`  | Starts the weather search              |
| `QVBoxLayout`  | Arranges widgets vertically            |
| `Qt`           | Provides alignment functionality       |
| `requests`     | Sends HTTP requests to the weather API |

---

## 🏙️ Getting the City Name

The city is entered using:

```python
self.city_input = QLineEdit(self)
```

The application retrieves the entered city using:

```python
city = self.city_input.text()
```

For example:

```text
Udupi
```

---

## 🌐 Creating the API Request

The application sends a request to the OpenWeatherMap API.

The request contains:

* City name
* API key
* Metric temperature units

The API returns weather information in JSON format.

Example structure:

```json
{
    "main": {
        "temp": 28.5
    },
    "weather": [
        {
            "id": 800,
            "description": "clear sky"
        }
    ]
}
```

---

# 🌡️ Temperature Conversion

The API temperature is retrieved in Celsius.

The application converts Celsius to Fahrenheit using:

```python
temperature_f = (temperature_c * 9/5) + 32
```

For example:

```text
28°C → 82°F
```

The result is displayed as:

```python
self.temperature_label.setText(f"{temperature_f:.0f}°F")
```

---

# 🌤️ Weather Description

The weather description is retrieved using:

```python
weather_description = data["weather"][0]["description"].capitalize()
```

For example:

```text
clear sky
```

becomes:

```text
Clear sky
```

---

# 😀 Weather Emojis

The application uses OpenWeatherMap's weather ID to select an appropriate emoji.

### Thunderstorm

```text
200 - 232 → ⛈️
```

### Drizzle

```text
300 - 321 → 🌦️
```

### Rain

```text
500 - 531 → 🌧️
```

### Snow

```text
600 - 622 → ❄️
```

### Atmosphere / Wind

```text
701 - 741 → 💨
```

### Volcano

```text
762 → 🌋
```

### Tornado

```text
781 → 🌪️
```

### Clear Sky

```text
800 → ☀️
```

### Clouds

```text
801 - 804 → ☁️
```

This functionality is implemented in:

```python
@staticmethod
def get_weather_emoji(weather_id):
```

---

# ⚠️ Error Handling

The application includes error handling for different API and network problems.

## 400 — Bad Request

```text
Bad request:
Please check your input
```

## 401 — Unauthorized

```text
Unauthorized:
Invalid API key
```

## 403 — Forbidden

```text
Forbidden:
Access is denied
```

## 404 — City Not Found

```text
Not Found:
City not found
```

## 500 — Internal Server Error

```text
Internal Server Error:
Please try again later
```

## 502 — Bad Gateway

```text
Bad Gateway:
Invalid response from the server
```

## 503 — Service Unavailable

```text
Service Unavailable:
Server is down
```

## 504 — Gateway Timeout

```text
Gateway Timeout:
No response from the server
```

---

# 🌐 Connection Error Handling

If there is no internet connection, the application displays:

```text
Connection error:
Please check your internet connection
```

This is handled using:

```python
except requests.exceptions.ConnectionError:
```

---

# ⏱️ Timeout Handling

If the API request takes too long, the application displays:

```text
Timeout Error:
The request timed out
```

This is handled using:

```python
except requests.exceptions.Timeout:
```

---

# 🎨 GUI Styling

The application uses Qt Style Sheets to customize the interface.

For example:

```python
self.setStyleSheet("""
    QLabel, QPushButton {
        font-family: calibri;
    }

    QLabel#city_label {
        font-size: 40px;
        font-style: italic;
    }

    QLineEdit#city_input {
        font-size: 40px;
    }

    QPushButton#get_weather_button {
        font-size: 30px;
        font-weight: bold;
    }

    QLabel#temperature_label {
        font-size: 75px;
    }

    QLabel#emoji_label {
        font-size: 100px;
        font-family: Segoe UI Emoji;
    }

    QLabel#description_label {
        font-size: 50px;
    }
""")
```

This provides a clean and visually appealing interface.

---

# 🔗 Signals and Slots

The **Get Weather** button is connected to the `get_weather()` method:

```python
self.get_weather_button.clicked.connect(self.get_weather)
```

When the user clicks the button:

```text
Click Get Weather
        │
        ▼
Get City Name
        │
        ▼
Send API Request
        │
        ▼
Receive Weather Data
        │
        ▼
Display Weather
```

---

# 🔄 Application Flow

```text
              Start Application
                     │
                     ▼
              Open Weather GUI
                     │
                     ▼
              Enter City Name
                     │
                     ▼
            Click Get Weather
                     │
                     ▼
              Send API Request
                     │
              ┌──────┴──────┐
              │             │
              ▼             ▼
          Successful      Error
              │             │
              ▼             ▼
       Get Weather Data   Show Error
              │
              ▼
       Convert Temperature
              │
              ▼
        Get Weather Emoji
              │
              ▼
        Display Weather
```

---

# ⚠️ Troubleshooting

## `ModuleNotFoundError: No module named 'PyQt5'`

Install PyQt5:

```bash
pip install PyQt5
```

## `ModuleNotFoundError: No module named 'requests'`

Install Requests:

```bash
pip install requests
```

## Invalid API Key

Make sure your API key is valid and configured correctly.

If you receive:

```text
Unauthorized:
Invalid API key
```

check your API key configuration.

## City Not Found

Make sure the city name is spelled correctly.

For example:

```text
Udupi
Mumbai
Bengaluru
Delhi
London
New York
```

---

# 🚀 Future Improvements

This project can be expanded with:

* 📅 Display current date
* 🌡️ Celsius/Fahrenheit toggle
* 📍 Automatic location detection
* 🌍 Multiple cities
* 📊 5-day weather forecast
* 🌅 Sunrise and sunset times
* 💧 Humidity information
* 💨 Wind speed
* ☁️ Cloud percentage
* 👁️ Visibility information
* 🌙 Dark mode
* 🎨 Dynamic background based on weather
* 🖼️ Weather icons
* 🔄 Refresh weather button
* 📱 Responsive GUI design

---

# 🎯 Learning Objectives

This project helps beginners understand:

* Python GUI development
* PyQt5
* `QWidget`
* `QLabel`
* `QLineEdit`
* `QPushButton`
* `QVBoxLayout`
* Signals and slots
* REST APIs
* HTTP requests
* JSON data
* API error handling
* Exception handling
* Temperature conversion
* Qt Style Sheets
* Environment variables
* Object-oriented programming

---

# 📦 Requirements

Create a `requirements.txt` file containing:

```text
PyQt5
requests
python-dotenv
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 🔐 `.gitignore`

Your `.gitignore` should include:

```text
.env
__pycache__/
*.pyc
```

This prevents your API credentials and Python cache files from being uploaded to GitHub.

---

# 🚀 Future Project Goal

The current project focuses on retrieving **current weather conditions**.

A future version could become a complete weather dashboard containing:

```text
┌─────────────────────────────────────────────┐
│              🌤️ Weather Dashboard           │
│                                             │
│  📍 Udupi                                   │
│                                             │
│             82°F                            │
│              ☁️                             │
│         Partly Cloudy                       │
│                                             │
│  💧 Humidity: 78%                           │
│  💨 Wind: 12 km/h                           │
│  👁️ Visibility: 10 km                      │
│                                             │
│       [ 5 Day Forecast ]                    │
└─────────────────────────────────────────────┘
```

---

## 👨‍💻 Author

**Gaurav G Salian**

B.Tech – Artificial Intelligence & Machine Learning

---

## 📄 License

This project is created for **educational and learning purposes**.
