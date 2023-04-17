import requests

url = "https://ebay-search-result.p.rapidapi.com/search/ipad"

querystring = {"sort_order":"BestMatch","limit":"10","offset":"0","country":"US"}

headers = {
    "X-RapidAPI-Key": "number this is a secret",
    "X-RapidAPI-Host": "ebay-search-result.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
