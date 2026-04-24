from flask import Flask, abort
from stockAnalyze import getCompanyStockInfo

app = Flask(__name__)

@app.route('/si-se')
def si_se():
    return 'SI Scholarship 2027'

@app.route('/analyze-stock/<ticker>')
def analyzeStock(ticker):
    if len(ticker) > 5 or not ticker.isidentifier():
        abort(400, 'Invalid ticker symbol.')
    try:
        analysis = getCompanyStockInfo(ticker)
    except NameError as e:
        abort(404, e)
    except:
        abort(500, 'Something went wrong running the stock analysis.')
    return analysis

if __name__ == '__main__':
    app.run()