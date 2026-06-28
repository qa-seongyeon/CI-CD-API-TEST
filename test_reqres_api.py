import requests

BASE_URL = "https://reqres.in/api"
API_KEY = "free_user_3FkPBToFISFH0vWAmSInt43hsfn"

#유저 아이디가 2 조회하는 api, 200나오고, 파싱데이터에서 아이디값이 2인지, 이메일이 있는지

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/2", headers={"x-api-key": API_KEY})

    assert response.status_code == 200

    data = response.json()["data"]
    assert data["id"] == 2

#없는 유저 조회
def test_get_nonexistent_user():
    response = requests.get(f"{BASE_URL}/users/23", headers={"x-api-key": API_KEY})

    assert response.status_code == 404

