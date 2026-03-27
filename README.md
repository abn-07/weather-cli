# 🌦️ Weather CLI

A lightweight, terminal-based weather application built with Python. This tool allows you to quickly fetch real-time weather data for any city globally using the OpenWeatherMap API, complete with condition-based emojis directly in your terminal.

## ✨ Features
* **Real-time Data:** Fetches current temperature, humidity, and weather conditions.
* **Visual Emojis:** Automatically pairs weather conditions with intuitive emojis (☀️, 🌧️, ❄️).
* **Flexible Inputs:** Supports multi-word city names.
* **Secure API Key Management:** Uses environment variables to keep credentials safe.

## 🛠️ Prerequisites
* Python 3.6 or higher installed on your system.
* An API key from [OpenWeatherMap](https://openweathermap.org/api).

## 🚀 Installation & Setup

Choose your operating system below for specific setup instructions.

### 🐧 Linux (Debian/Ubuntu & derivatives)
```bash
# 1. Clone the repository
git clone [https://github.com/your-username/weather-cli.git](https://github.com/your-username/weather-cli.git)
cd weather-cli

# 2. Create and activate a virtual environment
sudo apt update && sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### 🍏 macOS
```bash
# 1. Clone the repository
git clone [https://github.com/your-username/weather-cli.git](https://github.com/your-username/weather-cli.git)
cd weather-cli

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### 🪟 Windows
```powershell
# 1. Clone the repository
git clone [https://github.com/your-username/weather-cli.git](https://github.com/your-username/weather-cli.git)
cd weather-cli

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

## 🔐 Environment Configuration

Create a file named `.env` in the root directory of the project and add your OpenWeatherMap API key:
```env
OPENWEATHER_API_KEY=your_api_key_here
```
*(Note: `.env` is included in the `.gitignore` to prevent accidental credential leaks.)*

## 💻 Usage

Run the script followed by the name of the city you want to check. Ensure your virtual environment is activated before running.

**Command:**
```bash
python weather_cli.py "City Name"
```

**Example:**
```bash
python weather_cli.py Kozhikode
```

**Output:**
```text
--- Weather Report ---
Location:   Kozhikode
Condition:  ☀️  Clear Sky
Temp:       29°C
Feels Like: 31°C
Humidity:   70%
----------------------
```

## 📂 Project Structure
* `weather_cli.py`: The main execution script.
* `requirements.txt`: List of required Python packages.
* `.env`: (User created) Local storage for the API key.
* `.gitignore`: Keeps the repository clean by ignoring `venv/` and `.env`.
