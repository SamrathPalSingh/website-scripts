import requests
def trend(sym):
    string = 'https://finnhub.io/api/v1/stock/candle?symbol='+ sym +'&resolution=D&count=50&token=bq24qknrh5rc5ioodhhg'
    r = requests.get(string)
    #print(r.json())
    #print(len(r.json()['c']))
    lst = r.json()['c']
    maxx = []
    maxy = []
    for i in range(1, len(lst)-1 ):
        if( lst[i] >= lst[i-1] and lst[i] >= lst[i+1] and lst[i] != lst[i+1] ):
            maxx.append(i)
            maxy.append(lst[i])

    minx = []
    miny = []
    for i in range(1, len(lst)-1 ):
        if( lst[i] <= lst[i-1] and lst[i] <= lst[i+1] and lst[i] != lst[i+1]):
            minx.append(i)
            miny.append(lst[i])

    #print(maxy)
    #print(lst)
    import matplotlib.pyplot as plt
    plt.plot(lst)
    plt.scatter(minx, miny)
    plt.scatter(maxx, maxy)
    #print(miny)
    #print(maxy)
    min_sum_of_min = 0
    max_sum_of_max = 0
    while(len(maxy) != 0 and len(miny) != 0):
        if(maxx[len(maxx)-1] > minx[len(minx)-1]):
            value = maxy.pop()
            index = maxx.pop()
            sm = 0
            asm = 0
            count = 0
            for i in range(index+1, len(lst)):
                sm = sm + (lst[i] - lst[i-1])
                asm = asm + lst[i]
                count = count + 1
    #        print("In max : " + str(sm) )
            if (min_sum_of_min < abs(sm)):
                min_sum_of_min = abs(sm)
            if((abs(sm) > 0.1*(asm/count)) and (max_sum_of_max < (0.2*abs(sm)))):
    #            print("0.1*(asm/count)" + str(0.1*(asm/count)))
    #            print("asm" + str(asm))
    #            print("count" + str(count))
    #            print("abs(sm)" + str(abs(sm)))
    #            print("Downward trend")
                return(-1) # replace with return

        else:
            value = miny.pop()
            index = minx.pop()
            sm = 0
            asm = 0
            count = 0
            for i in range(index+1, len(lst)):
                sm = sm + (lst[i] - lst[i-1])
                asm = lst[i] + asm
                count = count + 1
            print("In min : " + str(sm))
            if (max_sum_of_max < abs(sm)):
                max_sum_of_max = abs(sm)
            if( (abs(sm) > 0.1*(asm/count)) and (min_sum_of_min < (0.2*abs(sm))) ):
    #            print("0.1*(asm/count)" + str(0.1*(asm/count)))
    #            print("abs(sm)" + str(abs(sm)))
    #            print("asm" + str(asm))
    ###            print("min_sum_of_min" + str(min_sum_of_min))
        #        print("(0.2*abs(sm))" + str((0.2*abs(sm))))
                 return(1) # replace with return
    return(0)
##############   TODO : IF THE TREND STAGNATES FOR A VERY LONG TIME IN THE LAST 3-4 DAYS DOES IT STILL QUALFY FOR UPWARD OR
##############    DOWNWARD TREND ????
##############   YES : WE ARE ONLY TRYING TO GET THE PREVIOUS TREND IF NO TREND IN THE LAST FEW DAYS THEN THE PREVIOUS TREND
##############    IS STILL
##############   WHAT EVER IT WAS DECIDED AFTER APPLYING THE ABOVE ALGORITHM
##############   NO : THE TREND BREAKS IF THE CLOSING PRICE STAGNATES IN THE LAST FEW DAYS
##############

# import requests
# r = requests.get('https://www.finnhub.io/api/v1/scan/pattern?symbol=AAPL&resolution=1&token=bq24qknrh5rc5ioodhhg')
# #print(r.json())
# print(len(r.json()['points']) )
# for i in (r.json()['points']):
#     print(i)
