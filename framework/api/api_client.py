import requests


class APIClient:

    def __init__(self, api_base_url, token=None):

        self.api_base_url = api_base_url

        self.session = requests.Session()

        if token:
            self.session.headers.update({
                "Authorization": f"Bearer {token}"
            })

    def get(self, endpoint):

        return self.session.get(
            f"{self.api_base_url}{endpoint}"
        )

    def post(self, endpoint, data=None):

        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=data
        )