import yfinance as yf

def extractbasicInfo(data):
    keysToExtract = ["longName", "website", "sector", "fullTimeEmployee", "marketCap", "totalRevenue", "trailingEps"]

    basicInfo = {}
    for key in keysToExtract:
        if key in data:
            basicInfo[key] = data[key] 
        else:
            basicInfo[key] = ""
    return basicInfo

def getCompanyStockInfo(tickerSymbol):
    company = yf.Ticker(tickerSymbol)
    basicInfo = extractbasicInfo(company.info)
    print(basicInfo)

getCompanyStockInfo("MSFT")