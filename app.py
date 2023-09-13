from flask import Flask, request

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

if __name__ == '__main__':
    app.run()