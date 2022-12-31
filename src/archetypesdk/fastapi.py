from fastapi import Request, HTTPException
from dataclasses import dataclass
import asyncio
from archetypesdk.auth_requestor import AuthRequestor
from archetypesdk.api_request_thread import requests_loop
import json

auth_requestor = AuthRequestor()

async def authorized(request: Request) -> bool:
    args = request.query_params
    body = await request.body()
    print(body)

    if body is not None and len(body) > 0:
        body = json.loads(body)
    else:
        body = {}

    header_apikey = request.headers.get("apikey", None)
    body_apikey = body.get("apikey", None)
    url_apikey = args.get("apikey", None)

    path = request.url.path
    method = request.method
    size = 0
    auth_response = auth_requestor.create_request(
        url_apikey=url_apikey,
        header_apikey=header_apikey,
        body_apikey=body_apikey,
        path=path,
        method=method,
    )
    if auth_response.status_code < 400:
        return True

    error_reason = auth_response.json()
    if "detail" in error_reason:
        error_reason = error_reason["detail"]
        if "message" in error_reason:
            error_reason = error_reason["message"]
    elif "message" in error_reason:
        error_reason = error_reason["message"]

    raise HTTPException(status_code=401, detail=error_reason)