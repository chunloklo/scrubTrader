from compData import *
from client import *
from interface import do
import time

def this():
    companies = compData()
    for i in range(0, 10):
        do('BID ' + companies[i].name + ' ' + str(companies[i].minAsk()[0]) + ' ' + str(1))
    dividend = dividendPerShare()
    for i in range(0 , 10):
        dividend[0][i] = dividend[0][i] / (companies[i].minAsk()[0] + 1);
    print(dividend[1])
    #find max dividend
    sortedList = sorted(dividend[0], reverse=True)
    max_value = sortedList[0]
    max_index = list(dividend[0]).index(max_value)

    #sell everything everything
    companies2 = compData()
    for i in range(0, 10):
        if companies[i].maxBid > companies.minAsk():
            do('ASK ' + companies[i].name + ' ' + str(companies[i].maxBid()[0] - .01) + ' ' + str(int(list(dividend[1])[i])))
    print(max_index)


    k = 0;
    while(k < 6):
        # if cash() / companies[max_index].minAsk()[0] < companies[max_index].minAsk()[1]:
            # do('BID ' + companies[max_index].name + ' ' + str(companies[max_index].minAsk()[0] + .1) + ' ' + str(int(cash() / companies[max_index].minAsk()[0])))
        do('BID ' + companies[max_index].name + ' ' + str(companies[max_index].minAsk()[0] + .1) + ' ' + str(companies[max_index].minAsk()[1]))
        k += 1
        max_value = sortedList[k]
        max_index = list(dividend[0]).index(max_value)


        print(cash())
    print(dividend[0])
    print(dividend[1])
    print(cash())
    return max_index, companies

def start():
    try:
        startTime = time.time()
        print(cash())
        companyReturn = this()
        companies = companyReturn[1]
        max_index = companyReturn[0]
        while(True):
            currTime = time.time() - startTime;
            if currTime > 0:
                companyReturn = this()
                companies = companyReturn[1]
                max_index = companyReturn[0]
                startTIme = time.time();
            dividend = dividendPerShare()
            while(k < 6):
                # if cash() / companies[max_index].minAsk()[0] < companies[max_index].minAsk()[1]:
                    # do('BID ' + companies[max_index].name + ' ' + str(companies[max_index].minAsk()[0] + .1) + ' ' + str(int(cash() / companies[max_index].minAsk()[0])))
                do('BID ' + companies[max_index].name + ' ' + str(companies[max_index].minAsk()[0] + .1) + ' ' + str(companies[max_index].minAsk()[1]))
                k += 1
                max_value = sortedList[k]
                max_index = list(dividend[0]).index(max_value)
            print(dividend[0])
            print(dividend[1])
            print(cash())
    finally:
        start()

start()