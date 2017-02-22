from compData import *
from client import *
from interface import do
import time

def start():
    try:
        while True:
            companies = compData()
            dividend = dividendPerShare()
            for i in range(0 , 10):
                dividend[0][i] = dividend[0][i] / (companies[i].minAsk()[0] + 1)
            cash1 = cash();
            print(cash1);
            for i in range(0, 10):
                if companies[i].minAsk()[0] - companies[i].maxBid()[0] < companies[i].maxBid()[0] * .05:
                # if (companies[1].marBid()[0] + companies[1].marAsk()[0]) / 2 > companies[i].maxBid()[0] :
                    do('BID ' + companies[i].name + ' ' + str(companies[i].minAsk()[0]) + ' ' + str(2))
            for i in range(0, 10):
                # if (companies[1].marBid() + companies[1].marAsk()) / 2 < companies[i].maxBid()[0]:
                if companies[i].minAsk()[0] - companies[i].maxBid()[0] < .5 and (dividend[0][i] < .00000000000001 or companies[i].maxBid()[0] > companies[i].minAsk()[0]) :
                    do('ASK ' + companies[i].name + ' ' + str(companies[i].maxBid()[0]) + ' ' + str(int(dividend[1][i])))
            print(dividend[0])
    except Exception as e:
        print(str(e))
        start()


start()