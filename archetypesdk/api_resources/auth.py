from __future__ import absolute_import, division, print_function
from flask import Flask, request
from datetime import datetime
import functools
import json

from archetypesdk.api_request_thread import requests_loop
from archetypesdk.auth_requestor import AuthRequestor
from archetypesdk.utils import Utils
from archetypesdk import record_auth_requests
from werkzeug.wrappers import Request, Response
import asyncio

auth_requestor = AuthRequestor()

def Auth(func):
    # request = kwargs.get("request", None)
    start_time = datetime.utcnow().timestamp()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args = Utils.get_request_args(request=request)
        headers = Utils.get_request_headers(request=request)
        body = Utils.get_request_body(request=request)

        header_apikey = request.headers.get("apikey", None)
        body_apikey = body.get("apikey", None)
        url_apikey = args.get("apikey", None)

        path = request.path
        method = request.method
        size = 0
        auth_response = asyncio.run_coroutine_threadsafe(auth_requestor.create_request(
            url_apikey=url_apikey,
            header_apikey=header_apikey,
            body_apikey=body_apikey,
            path=path,
            method=method,
        ), requests_loop).result()
        if auth_response.status < 400:
            return func(*args, **kwargs)

        error_reason = asyncio.run_coroutine_threadsafe(auth_response.json(), requests_loop).result()
        if "detail" in error_reason:
            error_reason = error_reason["detail"]
            if "message" in error_reason:
                error_reason = error_reason["message"]
        elif "message" in error_reason:
            error_reason = error_reason["message"]

        res = Response(
            json.dumps(error_reason),
            mimetype="application/json",
            status=auth_response.status,
        )
        return res

    return wrapper
