from trend import trend
import requests
#print(trend("AAPL"))

####          check for the previous trend           ####
####    Downward trend required for this pattern     ####

string = 'https://finnhub.io/api/v1/stock/candle?symbol='+ "AAPL" +'&resolution=D&count=3&token=bq24qknrh5rc5ioodhhg'
r = requests.get(string)
# print(len(r.json()['c']))

c0 = r.json()['c'][0]
h0 = r.json()['h'][0]
l0 = r.json()['l'][0]
o0 = r.json()['o'][0]

c1 = r.json()['c'][1]
h1 = r.json()['h'][1]
l1 = r.json()['l'][1]
o1 = r.json()['o'][1]

c2 = r.json()['c'][2]
h2 = r.json()['h'][2]
l2 = r.json()['l'][2]
o2 = r.json()['o'][2]

if( (c0 < o0) and (c0 > o1) and (c1 < o2) and (c2 > o2) and (c2 > o0) ):
    ###if( !doji( on day 1 ) ):
    ### if( doji( on day 2 ) ):
    print("Morning star")

#file.write("bearish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o) + " l = " + str(l) + "\n\n")
print("end")
