import requests


def test_case1():
    BASE_URL = "http://52.207.242.187/"
    login_data = {
                "email": "email@example.com",
                "password": "qwerty1"
                 }

    # Login and getting of valid token
    login = requests.post(BASE_URL + "auth/login", json=login_data)
    token = login.json()['session']['access_token']
    # Logout
    requests.delete(BASE_URL + "auth/logout", headers={'Authorization': token})
    # Attempt to get profile data to make sure that token is invalid
    token_check = requests.get(BASE_URL + "users/me", headers={'Authorization': token})
    assert token_check.status_code == 401