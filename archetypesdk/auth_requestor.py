import asyncio
from archetypesdk.api_resources.error import AuthRequestError
from archetypesdk.enums import Method
from archetypesdk import auth_version
import requests
import json
import logging
from werkzeug.wrappers import Request, Response
from archetypesdk.api_request_thread import requests_loop


class AuthRequestor:
    def __init__(self):
        from archetypesdk import SECRET_KEY, APP_ID, API_URL

        self.app_id = APP_ID
        self.secret_key = SECRET_KEY
        self.api_url = API_URL

    def create_request(
        self,
        method: str,
        path: str,
        url_apikey: str = "",
        body_apikey: str = "",
        header_apikey: str = "",
        headers: dict = {},
        data: dict = {},
        intent: str = None,
    ):
        headers = {
            "X-Archetype-SecretKey": self.secret_key,
            "X-Archetype-AppID": self.app_id,
        }

        data = {
            "path": path,
            "method": method,
            "url_apikey": url_apikey,
            "body_apikey": body_apikey,
            "header_apikey": header_apikey,
        }

        url = f"{self.api_url}/sdk/v{auth_version}/authorize"
        logging.debug(f"POST {url}")
        response = requests.post(url=url, headers=headers, json=data)
        return response

        if response.status_code < 400:
            return response
        """
        res = Response(
            json.dumps(
                {
                    "error": "API Key not supplied. Add an 'apikey' field to the headers with your provided API key"
                }
            ),
            mimetype="text/plain",
            status=403,
        )

        
        else:
            raise AuthRequestError(
                response.status_code, response.json(), intent=intent
            )
        """
