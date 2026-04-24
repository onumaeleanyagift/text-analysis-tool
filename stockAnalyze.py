import json
import yfinance as yf
import requests
import analyze
from datetime import datetime
from bs4 import BeautifulSoup



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
        if newsDict['content']['clickThroughUrl']:
            link = newsDict['content']['clickThroughUrl']['url']
        else:
            link = newsDict['content']['canonicalUrl']['url']

        newsDictToAdd = {
            'title': newsDict['content']['title'],
            'link': link
        }
        allNewsArticles.append(newsDictToAdd)
    # print(allNewsArticles)
    return allNewsArticles

def extractNewsArticleTextFromHtml(soup):
    allText = ""
    result = soup.find_all("div", {"class":"body-wrap"})
    for res in result:
        allText += res.text
    return allText

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36'
}

def extractCompamyNewsArticles(newsArticles):
    allArticlesText = ""
    for newsArticle in newsArticles:
        url = newsArticle['link']
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        # print(soup.title)
        # print(soup.url)

        if not soup.find_all(string="Story Continues"):
            allArticlesText += extractNewsArticleTextFromHtml(soup)
    return allArticlesText



def getCompanyStockInfo(tickerSymbol):
    # Get data from Yahoo Finance API
    company = yf.Ticker(tickerSymbol)

    # Get basic info on company
    basicInfo = extractbasicInfo(company.info)
  
    # Check if company exists, if not, trigger error
    if not basicInfo["longName"]:
        raise NameError("Could not find stock info, ticker may be delisted or does not exist")

    priceHistory = getPriceHistory(company)
    futureEarningsDates = getEarningsDates(company)
    newsArticles = getCompanyNews(company)
    newsArticlesAllText = extractCompamyNewsArticles(newsArticles)
    newsTextAnalysis = analyze.analyzeText(newsArticlesAllText)

    finalStockAnalysis = {
        "basicInfo": basicInfo,
        "priceHistory": priceHistory,
        "futureEarningsDates": futureEarningsDates,
        "newsArticles": newsArticles,
        "newsTextAnalysis": newsTextAnalysis
    }
    return finalStockAnalysis

# companyStockAnalysis = getCompanyStockInfo("MSFT")
# print(json.dumps(companyStockAnalysis, indent=4))