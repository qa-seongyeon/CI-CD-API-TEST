import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://reqres.in/api")
API_KEY = os.getenv("API_KEY", "free_user_3FkPBToFISFH0vWAmSInt43hsfn")
