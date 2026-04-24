from flask import Flask, abort

app = Flask(__name__)

@app.route('/si-se')
def si_se():
    return 'SI Scholarship 2027'

@app.route('/analyze-stock/<ticker>')
def analyzeStock(ticker):
    if len(ticker) > 5 or not ticker.isidentifier():
        abort(400, 'Invalid ticker symbol')
    return {'data': 'Analysis for ' + ticker + ' comming soon'}

if __name__ == '__main__':
    app.run()