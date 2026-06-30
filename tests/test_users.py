from api.users_api import get_user


# 존재하는 유저 조회
'''상태코드 + 파싱데이터 검증 케이스'''
def test_get_single_user():
    response = get_user(2)

    assert response.status_code == 200

    data = response.json()["data"]
    assert data["id"] == 2
    assert "email" in data


# 없는 유저 조회
def test_get_nonexistent_user():
    response = get_user(23)

    assert response.status_code == 404
