import requests

url = "https://api.quotable.io/quotes/random"

print("ggetting a random quote...\n")

response = requests.get(url)

randomQuoteList = response.json()
print(randomQuoteList[0]["content"])
print("- " + randomQuoteList[0]["author"])