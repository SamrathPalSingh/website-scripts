## Threads
import threading
import pandas as pd
from queue import Queue
import time
import requests
file = open("stock_pred.txt", "w")
data = pd.read_csv("C:\\Users\\BEST BUY\\Desktop\\NASDAQ_20200331.csv")
symbols = data.iloc[:100,0:1].values
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
    if (r.json()['c'][0] >= r.json()['o'][0]):
        print("up")
        c = r.json()['c'][0]
        h = r.json()['h'][0]
        l = r.json()['l'][0]
        o = r.json()['o'][0]
        flag1 = 0
        if( (h-c) > (o-l) ):
            if( (h-c) <= (o-l)*1.2 ):
                flag1 = 1
        elif ( (h-c) < (o-l) ):
            if( (h-c)*1.2 >= (o-l) ):
                flag1 = 1
        elif ( (h-c) == (o-l) ):
                flag1 = 1
        flag2 = 0
        if( (c-o) <= (0.03*((c+o)/2)) ):
                flag2 = 1
        if( flag1 == 1 and flag2 == 1):
            print("Spinning top")
            file.write("spinning top at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o)+ " l = " + str(l) + "\n\n")
    else:
        print('down')
        c = r.json()['c'][0]
        h = r.json()['h'][0]
        l = r.json()['l'][0]
        o = r.json()['o'][0]
        flag1 = 0
        if( (h-o) > (c-l) ):
            if( (h-o) <= (c-l)*1.2 ):
                flag1 = 1
        elif ( (h-o) < (c-l) ):
            if( (h-o)*1.2 >= (c-l) ):
                flag1 = 1
        elif ( (h-o) == (c-l) ):
                flag1 = 1
        flag2 = 0
        if( (o-c) <= (0.03*((c+o)/2)) ):
            flag2 = 1
        if( flag1 == 1 and flag2 == 1):
            file.write("spinning top at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o)+ " l = " + str(l) + "\n\n")
            print("Spinning top")

for i in symbols:
    th.put(threading.Thread(target=net_work, args = [i]))

while (th.qsize()) > 0:
    print("-------------------iteration------------------------")
    time.sleep(5)
    temp = []
    for j in range(0, 100):
        if th.empty() == False:
            temp1 = th.get()
            temp.append(temp1)
            temp1.start()
    for i in temp:
        i.join()


file.close()
print("END")
