import time

from flask import Flask, request, after_this_request

import pic_package_search
from utils.mysql_utils import pic_package_info, pic_url
from threading import Thread

app = Flask(__name__)


@app.route('/api/kanmeitu/search', methods=['GET'])
def index():
    """
    url http://localhost:8000/api/kanmeitu/search?keyboard={}&search_id={}&page={}
    """
    keyboard = request.args.get('keyboard')
    search_id = request.args.get('search_id')
    page = request.args.get('page')
    print(keyboard, search_id)
    if keyboard == "":
        keyboard = None
    if search_id == "":
        search_id = None
    return pic_package_search.pic_package_search(keyboard=keyboard, search_id=search_id, page=page)


@app.route('/api/kanmeitu/view', methods=['GET'])
def view():
    """
    url http://localhost:8000/api/kanmeitu/view?url=
    :return:
    """
    package_url = request.args.get('url')
    package_id = package_url[package_url.find('mm/') + 3:-len('.html')]
    res = pic_package_info.select(package_id)
    if len(res) == 0:
        yield {
            'status': False,
            'msg': '未找到此数据，尝试寻找'
        }
        pic_package_info.insert(package_id, 0)
        response = pic_package_search.pic_package_total_url(package_url)
        pic_package_info.update(package_id, len(response))
        for url, count_id in zip(response, range(1, len(response) + 1)):
            pic_url.insert(package_id, count_id, url)
    else:
        package_info = res[0]
        count = package_info[1]
        if count == 0:
            return {
                'status': False,
                'msg': '找到此数据，正在收集信息'
            }
        else:
            res = pic_url.select(package_id)


@app.route('/test', methods=['GET'])
def test():
    """
    url: localhost:8000/test?test=
    :return:
    """
    info = 111

    yield str(info)

    info = 11

    for i in range(1, info):
        print(i)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
