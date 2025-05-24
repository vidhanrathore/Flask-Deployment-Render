from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/vidhan')
def hello_world2():
    return 'Hello Vidhan'

if __name__ == '__main__':
    app.run()
