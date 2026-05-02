# import json
from flask import Flask, abort, request
from flask_cors import CORS
from stockAnalyze import getCompanyStockInfo
from analyze import analyzeText

# f = open('test/result.json')
# stockDataTest = json.load(f)

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Running", 200

@app.route("/health")
def health():
    return "OK", 200

@app.route('/analyze-stock/<ticker>', methods=["GET"])
def analyzeStock(ticker):
    # return stockDataTest
    if len(ticker) > 5 or not ticker.isidentifier():
        abort(400, 'Invalid ticker symbol.')
    try:
        analysis = getCompanyStockInfo(ticker)
    except NameError as e:
        abort(404, e)
    except Exception as e:
        print(f"Error running the stock analysis: {e}")
        abort(500, 'Something went wrong running the stock analysis.')
    return analysis

@app.route('/analyze-text', methods=["POST"])
def analyzeTextHandler():
    data = request.get_json()
    if "text" not in data or not data["text"]:
        abort(400, "No text provided to analyze")

    analysis = analyzeText(data["text"])
    return analysis

if __name__ == '__main__':
    app.run(host="0.0.0.0")