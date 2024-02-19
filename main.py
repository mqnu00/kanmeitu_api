from flask import Flask

import utils.requests_utils.requests_util

app = Flask(__name__)


@app.route('/index')
def index():
    return 'hello world!'


if __name__ == '__main__':
    app.run(host='192.168.10.233', port=8000)