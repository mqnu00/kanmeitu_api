from utils import requests_utils

import base_data

data = base_data.search_data
data['keyboard'] = '南宫'

response = requests_utils.requests_util.requests_method(
    url=base_data.search_url,
    method='post',
    cnt=3,
    data=data
)

with open('test.html', 'wb') as f:
    f.write(response.content)