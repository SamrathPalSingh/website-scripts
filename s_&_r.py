import requests
r = requests.get('https://finnhub.io/api/v1/scan/support-resistance?symbol=IBM&resolution=D&token=bq24qknrh5rc5ioodhhg')
print(r.json())

# import requests
# r = requests.get('https://finnhub.io/api/v1/stock/candle?symbol=IBM&resolution=D&count=10&token=')
# print(r.json())
