from trend import trend
import requests
#print(trend("AAPL"))


####          check for the previous trend         ####
####    Upward trend required for this pattern     ####

##*****#####****   hanging man not as accurate in predicting as the hammer ****####****####

string = 'https://finnhub.io/api/v1/stock/candle?symbol='+ "AAPL" +'&resolution=D&count=1&token=bq24qknrh5rc5ioodhhg'
r = requests.get(string)
#print(r.content)
# if (str(r.headers.get('content-type'))) != "application/json; charset=utf-8":
#     print("-----------------")
#     th.put(threading.Thread(target=net_work, args = [i]))
#     return
if (r.json()['c'][0] > r.json()['o'][0]):
    print("up")
    c = r.json()['c'][0]
    h = r.json()['h'][0]
    l = r.json()['l'][0]
    o = r.json()['o'][0]
    if (((c-o) <= (2*(o-l))) and ((c-o) <= (0.075*((c+o)/2)))):
        print("Hammer found ")
            #file.write("bullish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o)+ " l = " + str(l) + "\n\n")
else:
    print('down')
    c = r.json()['c'][0]
    h = r.json()['h'][0]
    l = r.json()['l'][0]
    o = r.json()['o'][0]
#         print(((c-l)/c)*100, (((h-o)/o)*100))
    if (((o-c) <= (2*(c-l))) and ((o-c) <= (0.075*((c+o)/2)))):
        print("Hammer found ")
            #file.write("bearish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o) + " l = " + str(l) + "\n\n")
print("end")
