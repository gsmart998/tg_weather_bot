import os

from dotenv import load_dotenv


class Config:
    load_dotenv()
    BOT_KEY = os.environ["BOT_KEY_TEST"]
    API_KEY = os.environ["API_KEY"]
