from archetypesdk.enums import Method


class APIRequestError(Exception):
    """Base class for other exceptions"""

    def __init__(self, method: Method, status_code: int, json: dict, intent: str):

        error_reason = json
        if "detail" in json:
            error_reason = json["detail"]
            if "message" in error_reason:
                error_reason = error_reason["message"]
        elif "message" in json:
            error_reason = json["message"]

        message = "Error in "
        if intent:
            message = f"{message}{intent} -- {error_reason}"
        else:
            message = f"Archetype Error: {json}"
        super().__init__(message)


class AuthRequestError(Exception):
    """The reasoning for blocking a request"""

    def __init__(self, status_code: int, json: dict, intent: str):

        error_reason = json
        if "detail" in json:
            error_reason = json["detail"]
            if "message" in error_reason:
                error_reason = error_reason["message"]
        elif "message" in json:
            error_reason = json["message"]

        message = "Error in "
        if intent:
            message = f"{message}{intent} -- {error_reason}"
        else:
            message = f"Archetype Error: {json}"
        super().__init__(message)
