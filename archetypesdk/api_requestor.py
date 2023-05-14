import requests
from venv import create
from archetypesdk.api_resources.error import APIRequestError
from archetypesdk.enums import Method


class APIRequestor:
    def __init__(self):
        from archetypesdk import secret_key
        from archetypesdk import app_id
        from archetypesdk import api_url
        self.secret_key = secret_key
        self.app_id = app_id
        self.api_url = api_url
        

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
