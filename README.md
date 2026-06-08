# 📊 MyReporter

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![PySide6](https://img.shields.io/badge/UI-PySide6-green.svg)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)

A lightweight desktop application for managing and sending automated messages via the Bale Bot API.

Built with PySide6, MyReporter provides a simple and clean UI for creating, editing, storing, and sending predefined activity reports.


## ✨ Features

- Add / Edit / Delete activity messages
- Send selected messages directly to Bale channel/bot
- Local persistence using JSON storage
- Simple and clean PySide6 desktop UI
- Integrated Bale Bot API client
- Ready for packaging as Windows executable (PyInstaller)
- Dark mode support (optional / extensible)


## 🧱 Project Structure

```
MyReporter/
├── assets/              # UI images and icons
│   ├── MyReporterBot raw.png
│   ├── MyReporterBot.ico
│   └── MyReporterBot.png
├── docs/                # Web docs and landing page
│   ├── index.html
│   ├── script.js
│   └── style.css
├── .env                 # Environment variables (BOT_TOKEN, CHANNEL_ID)
├── .gitignore
├── bale_api.py          # Bale Bot API client wrapper
├── config.py            # Bot token and channel configuration
├── env_template.txt
├── LICENSE
├── main.py              # Optional test script for API
├── README.md
├── requirements.txt
├── test_api.py
└── ui.py                # Main GUI application (entry point)
```


## 🚀 Getting Started

### 1. Clone repository

```bash
git clone https://github.com/MahdiMohammadiha/MyReporter.git
cd MyReporter
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install PySide6 requests python-dotenv pyinstaller
```

### 3. Configure environment variables

Create a `.env` file:

```
BOT_TOKEN=your_bale_bot_token
CHANNEL_ID=your_channel_id
```

### 4. Run application

```bash
python main.py
```

## 📦 Build Executable

```bash
pyinstaller --onefile --windowed --name MyReporter --icon=assets/MyReporterBot.ico --add-data ".env;." main.py
```

Output:

```
dist/MyReporter.exe
```

## ⚠️ Notes

- Keep BOT token private
- Ensure .env exists when running EXE
- Use main.py as entry point


## 📄 License

This project is licensed under the [GNU General Public License v3.0 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html).


## 💡 Contribution
Contributions are welcome!  
If you have any **ideas**, **suggestions**, or **bug reports**, please open an issue or submit a PR.

🔗 GitHub Page: https://MahdiMohammadiha.github.io/MyReporter/ <br>
🔗 GitHub Repository: https://github.com/MahdiMohammadiha/MyReporter/


---

Created by *Mahdi Mohammadiha* — © 2026 *MyReporter* Project
