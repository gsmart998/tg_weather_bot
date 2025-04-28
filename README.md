# 🌦️ Telegram Weather Bot

A simple educational Telegram bot written in Python that shows the current weather for a given city using the OpenWeather API.

## 📁 Project Structure

```
.
├── .env               # Environment variables (API keys)
├── .gitignore
├── .python-version    # Python version for pyenv (optional)
├── README.md
├── config.py          # Configuration file
├── main.py            # Bot logic
├── pyproject.toml     # Project dependencies (managed via uv)
└── uv.lock            # Locked dependencies
```

## 🛠️ Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) — modern Python package manager

## 🚀 Quick Start

1. Clone the repository:

```bash
git clone https://github.com/gsmart998/tg_weather_bot.git
cd tg_weather_bot
```

2. Create virtual environment and install dependencies:

```bash
uv venv
uv pip install -r <(uv pip compile pyproject.toml)
```

3. Add your tokens to the `.env` file:

```
BOT_KEY=your_telegram_bot_token
API_KEY=your_openweather_api_key
```

4. Run the bot:

```bash
uv run python main.py
```

## 📌 Commands

- `/start` or `/help` — greeting and usage instructions
- Send a city name — the bot will reply with the current weather

## 🧾 Example

**You:** `London`  
**Bot:** `The weather in London is: +14 🌧️ \nFeels like +12`

---

🔧 Built for learning purposes
