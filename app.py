from flask import Flask, request
from require_auth import require_auth

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/param-test')
def param_test(param):
    return param

@app.route('/post', methods=['POST'])
def post_test():
    return request.get_json()

@app.route('/query-test')
def query_test():
    return request.args


@app.route('/auth-test')
@require_auth
def auth_test():
    return 'You are logged in!'


if __name__ == '__main__':
    app.run()