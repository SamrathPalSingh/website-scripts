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
    if((o0 >= c1) and (o1 > o0) and (c0 >= o1)):
        if(((((o1-o0)/(c0-o0))*100)>50) and ((((o1-o0)/(c0-o0))*100)<100):
            print("dark cloud cover")
    # elif( (o0 <= c1) and (c0 >= o1)):
    #     if(((((o1-c1)/(c0-o0))*100) > 50) and (((((o1-c1)/(c0-o0))*100) <100))):
    #         print("dark cloud cover")


        #### This case is handled in the Bearish Harami ####
        ####       Make sure this works properly        ####


    elif((o0 <= c1) and (c1 < c0) and (o1 >= c0)):
        if(((((c0-c1)/(c0-o0))*100)>50) and (((((c0-c1)/(c0-o0))*100)< 100)):
            print("dark cloud cover")
#file.write("bearish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o) + " l = " + str(l) + "\n\n")
print("end")
