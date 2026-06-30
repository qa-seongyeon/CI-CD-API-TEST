import requests

from config.settings import API_KEY, BASE_URL


def get_user(user_id):
    return requests.get(f"{BASE_URL}/users/{user_id}", headers={"x-api-key": API_KEY})
