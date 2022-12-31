import json


class Utils:
    def is_url_parsable(query: str) -> bool:
        pass

    def get_request_body(request):
        if request.method != "GET":
            try:
                request_data = request.get_data()
                fix_bytes_value = request_data.decode("unicode_escape")
                json_data = json.loads(fix_bytes_value)
                return json_data
            except Exception as e:
                return {}
        else:
            return {}

    def get_request_headers(request):
        headers = {k: v for k, v in request.headers.items()} if request.headers else {}
        return headers

    def get_request_args(request):
        args = request.args.to_dict() if request.args else {}
        return args
