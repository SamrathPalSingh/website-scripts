from trend import trend
import requests
#print(trend("AAPL"))

####          check for the previous trend           ####
####      Upward trend required for this pattern     ####

string = 'https://finnhub.io/api/v1/stock/candle?symbol='+ "AAPL" +'&resolution=D&count=2&token=bq24qknrh5rc5ioodhhg'
r = requests.get(string)
#print(len(r.json()['c']))

c0 = r.json()['c'][0]
h0 = r.json()['h'][0]
l0 = r.json()['l'][0]
o0 = r.json()['o'][0]

c1 = r.json()['c'][1]
h1 = r.json()['h'][1]
l1 = r.json()['l'][1]
o1 = r.json()['o'][1]
if( (c0 > o0) and (c1 < o1) ):
    if((o0 < c1) and (c0 > o1)):
        print("dark cloud cover")

####  check comments in dark_cloud_cover.py  ####


#file.write("bearish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o) + " l = " + str(l) + "\n\n")
print("end")
