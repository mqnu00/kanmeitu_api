import requests
from . import requests_data


def requests_method(url, method, cnt=3, data=None):
    response = None

    while cnt > 0:

        try:

            if method == 'get':
                response = requests.get(
                    url=url,
                    headers=requests_data.headers,
                    data=data
                )
            elif method == 'post':
                response = requests.post(
                    url=url,
                    headers=requests_data.headers,
                    data=data
                )

            return response

        except Exception as e:
            cnt = cnt - 1

    return response

