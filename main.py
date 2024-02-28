from flask import Flask, request

import pic_package_search
import process_data
import utils.requests_utils.requests_util

app = Flask(__name__)


@app.route('/api/kanmeitu/search', methods=['GET'])
def index():
    """
    url http://localhost:8000/search?keyboard={}&search_id={}&page={}
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
    url = request.args.get('url')
    
    return pic_package_search.pic_package_total_url(url)


@app.route('/api/kanmeitu/view_process', methods=['GET'])
def view_process():
    """
    url http://localhost:8000/api/kanmeitu/view_process
    :return:
    """
    print(pic_package_search.process_now, pic_package_search.process_max)
    return {
        'max': pic_package_search.process_max,
        'process': pic_package_search.process_now
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
