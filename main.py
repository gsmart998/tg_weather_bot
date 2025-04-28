import logging
from config import Config

from telebot import TeleBot
from telebot.types import Message
import requests
import json


emoji = {
    "Thunderstorm": "⛈️",
    "Drizzle": "💨",
    "Rain": "🌧️",
    "Snow": "❄️",
    "Mist": "💨",
    "Smoke": "💨",
    "Haze": "🌁",
    "Dust": "😷",
    "Fog": "🌁",
    "Sand": "🏖️",
    "Ash": "🌋",
    "Squall": "🌪️",
    "Tornado": "🌪️",
    "Clear": "☀️",
    "Clouds": "☁️",
}

logging.basicConfig(level=logging.INFO)
bot = TeleBot(Config.BOT_KEY)


@bot.message_handler(commands=["start", "help"])
def start(message: Message):
    """Hello user"""
    logging.info(f"Received '{message.text}' command.")
    bot.send_message(
        message.from_user.id,
        f"Hello, {message.from_user.first_name} 👋\nWrite city name to get weather.",
    )


@bot.message_handler(content_types=["text"])
def get_weather(message: Message):
    logging.info(
        f"Received text: '{message.text}' from user: '{message.from_user.first_name}'"
    )
    text = message.text.strip().lower()
    if text[0] == "/":
        bot.reply_to(message, "Wrong command!\nAvailable commands: /start, /help")
        return
    res = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={text}&appid={Config.API_KEY}&units=metric"
    )

    data = json.loads(res.text)

    if data["cod"] != 200:
        if data["cod"] == "404":
            bot.reply_to(
                message, f"{data['message'].capitalize()}😩\nTry another city name"
            )
            return
        bot.reply_to(message, "Something went wrong, try again later 🤔")
        return

    city = data["name"]
    temp = round(data["main"]["temp"])
    weather = data["weather"][0]["main"]
    if temp > 0:
        temp = f"+{temp}"
    temp_feel = round(data["main"]["feels_like"])
    if temp_feel > 0:
        temp_feel = f"+{temp_feel}"
    bot.reply_to(
        message,
        f"The weather in {city} is: {temp} {emoji[weather]} \nFeels like {temp_feel}",
    )


if __name__ == "__main__":
    # Polling checks for new messages
    print("Bot now running...")
    bot.infinity_polling()
