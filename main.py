from flask import Flask, request

import pic_package_search
import utils.requests_utils.requests_util

app = Flask(__name__)


@app.route('/api/kanmeitu/search', methods=['GET'])
def index():
    """
    url http://localhost:8000/search?keyboard={}&search_id={}
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
