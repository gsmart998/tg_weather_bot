import os

from dotenv import load_dotenv


class Config:
    load_dotenv()
    BOT_KEY = os.getenv("BOT_KEY")
    API_KEY = os.getenv("API_KEY")
