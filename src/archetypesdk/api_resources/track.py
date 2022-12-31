from datetime import datetime
from client_ip import ClientIp


def _send_log_details(app_id, status_code, request, start_time, request_body):
    client_ip = ClientIp()
    request_method = request.method
    dct = {}
    dct["status_code"] = status_code
    dct["method"] = request_method
    dct["size"] = 0  # len(response.data)
    dct["path"] = request.path
    dct["args"] = request.args.to_dict() if request.args else {}
    dct["duration"] = datetime.utcnow().timestamp() - start_time
    dct["product_id"] = "tier"
    dct["app_id"] = app_id
    dct["timestamp"] = start_time
    dct["ip"] = client_ip.get_client_address(request.environ)
    dct["body"] = request_body
    dct["user_id"] = request.args.get("apikey") if "apikey" not in request.args else ""
    dct["headers"] = (
        {k: v for k, v in request.headers.items()} if request.headers else {}
    )
    # _send_details(dct)
