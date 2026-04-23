from flask import Flask

app = Flask(__name__)

@app.route('/si-se')
def si_se():
    return 'SI Scholarship 2027'

@app.route('/analyze-stock/<ticker>')
def analyzeStock(ticker):
    return {'data': 'Analysis for ' + ticker + ' comming soon'}


if __name__ == '__main__':
    app.run()