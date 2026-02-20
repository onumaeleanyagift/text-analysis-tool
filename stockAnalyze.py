import yfinance as yf
from datetime import datetime


def extractbasicInfo(data):
    keysToExtract = ["longName", "website", "sector", "fullTimeEmployee", "marketCap", "totalRevenue", "trailingEps"]

    basicInfo = {}
    for key in keysToExtract:
        if key in data:
            basicInfo[key] = data[key] 
        else:
            basicInfo[key] = ""
    return basicInfo

def getPriceHistory(company):
    historyDF = company.history(period="12mo")
    prices = historyDF["Open"].tolist()
    dates = historyDF.index.strftime("%Y-%m-%d").tolist()
    return {
        "price": prices,
        "date": dates
    }

def getEarningsDates(company):
    earningsDatesDf = company.earnings_dates
    allDates = earningsDatesDf.index.strftime("%Y-%m-%d").tolist()
    date_objects = [datetime.strptime(date, "%Y-%m-%d") for date in allDates]
    current_date = datetime.now()
    future_dates = [date.strftime("%Y-%m-%d") for date in date_objects if date > current_date]
    return future_dates

def getCompanyNews (company):
    newsList = company.news
    allNewsArticles = []
    for newsDict in newsList:
        newsDictToAdd = {
            'title': newsDict['content']['title']
            # 'url': newsDict['content']['clickThroughUrl']['url']
        }
        allNewsArticles.append(newsDictToAdd)
    print(allNewsArticles)
    return allNewsArticles

def getCompanyStockInfo(tickerSymbol):
    # Get data from Yahoo Finance API
    company = yf.Ticker(tickerSymbol)

    # Get basic inf on company
    basicInfo = extractbasicInfo(company.info)
    priceHistory = getPriceHistory(company)
    futureEarningsDates = getEarningsDates(company)
    newsArticles = getCompanyNews(company)

getCompanyStockInfo("MSFT")