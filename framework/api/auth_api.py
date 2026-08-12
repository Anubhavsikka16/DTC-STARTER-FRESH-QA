import requests


class AuthAPI:

    def __init__(self, api_base_url):

        self.api_base_url = api_base_url

    def login(self, email, password):

        response = requests.post(
            f"{self.api_base_url}/auth/user/emailpass",
            json={
                "email": email,
                "password": password
            }
        )

        response.raise_for_status()

        return response.json()["token"]