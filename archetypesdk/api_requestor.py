import requests
from venv import create
from archetypesdk.api_resources.error import APIRequestError
from archetypesdk.enums import Method


class APIRequestor:
    def __init__(self):
        from archetypesdk import SECRET_KEY, APP_ID, API_URL

        self.app_id = APP_ID
        self.secret_key = SECRET_KEY
        self.api_url = API_URL
        

    def create_request(
        self,
        request_method: Method,
        path: str,
        headers: dict = {},
        data: dict = {},
        object: str = None,
        intent: str = None,
    ):
        headers["Authorization"] = f"Bearer {self.secret_key}"
        headers["X-Archetype-AppID"] = self.app_id
        headers["X-Archetype-SecretKey"] = self.secret_key
    
        url = f"{self.api_url}{path}"
        if request_method == Method.GET:
            response = requests.get(url=url, headers=headers)
        elif request_method == Method.POST:
            response = requests.post(url=url, headers=headers, json=data)
        elif request_method == Method.PUT:
            response = requests.put(url=url, headers=headers, json=data)
        elif request_method == Method.DELETE:
            response = requests.delete(url=url, headers=headers, json=data)

        if response.status_code < 400:
            return response.json()
        else:
            raise APIRequestError(
                request_method, response.status_code, response.json(), intent=intent
            )
