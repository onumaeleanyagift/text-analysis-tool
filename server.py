from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Si Scholarship 2027'

if __name__ == '__main__':
    app.run()