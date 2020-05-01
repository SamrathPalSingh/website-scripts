##final code for marobuzo recognition

import threading
import pandas as pd
from queue import Queue
import time
file = open("stock_pred.txt", "w")
data = pd.read_csv("C:\\Users\\BEST BUY\\Desktop\\NASDAQ_20200331.csv")
symbols = data.iloc[:,0:1].values
th = Queue(maxsize = 4000)

def net_work(i):
    print(i[0])
    string = 'https://finnhub.io/api/v1/stock/candle?symbol='+ i[0] +'&resolution=D&count=1&token=bq24qknrh5rc5ioodhhg'
    r = requests.get(string)
    print(r.content)
    if (str(r.headers.get('content-type'))) != "application/json; charset=utf-8":
        print("-----------------")
        th.put(threading.Thread(target=net_work, args = [i]))
        return
    if (r.json()['c'][0] > r.json()['o'][0]):
        print("up")
        c = r.json()['c'][0]
        h = r.json()['h'][0]
        l = r.json()['l'][0]
        o = r.json()['o'][0]
        if o != c:
            if ((((c-h)/c)*100) <= 0.5 and (((o-l)/o)*100) <= 0.5 and ((h-c)/(c-o)*100) <= 5 and ((o-l)/(c-o)*100) <= 5):
                print("bullish Marabozu at " + str(i[0]))
                file.write("bullish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o)+ " l = " + str(l) + "\n\n")
    else:
        print('down')
        c = r.json()['c'][0]
        h = r.json()['h'][0]
        l = r.json()['l'][0]
        o = r.json()['o'][0]
#         print(((c-l)/c)*100, (((h-o)/o)*100))
        if o != c:
            if ((((h-o)/o)*100) <= 0.5 and (((c-l)/c)*100)<= 0.5 and ((h-o)/(o-c)*100) <= 5 and ((c-l)/(o-c)*100) <= 5):
                print("bearish Marabozu at " + str(i[0]))
                file.write("bearish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o) + " l = " + str(l) + "\n\n")

for i in symbols:
    th.put(threading.Thread(target=net_work, args = [i]))

while (th.qsize()) > 0:
    print("-------------------iteration------------------------")
    time.sleep(20)
    temp = []
    for j in range(0, 500):
        if th.empty() == False:
            temp1 = th.get()
            temp.append(temp1)
            temp1.start()
    for i in temp:
        i.join()


file.close()
print("END")
