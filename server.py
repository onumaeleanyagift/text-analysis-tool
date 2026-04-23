from flask import Flask

app = Flask(__name__)

@app.route('/si-se')
def si_se():
    return 'SI Scholarship 2027'

@app.route('/analyze-stock')
def analyzeStock():
    return {'data': 'Coming soon'}


if __name__ == '__main__':
    app.run()