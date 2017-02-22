from compData import *
from client import *
from interface import do
import time

def start():
    try:
        startTime = time.time()
        while True:
            cash1 = cash();
            print(cash1);
            currTime = time.time() - startTime;
            currTime = currTime % 240
            dividend = dividendPerShare()
            if currTime < 120:
                print(1)
                companies = compData()
                for i in range(5, 10):
                    do('ASK ' + companies[i].name + ' ' + str(companies[i].maxBid()[0]) + ' ' + str(dividend[1][i]))
                for i in range(0, 5):
                        do('BID ' + companies[i].name + ' ' + str(companies[i].minAsk()[0]) + ' ' + str(2))
                for i in range(0, 5):
                    if (companies[1].marBid() + companies[1].marAsk()) / 2 < companies[i].maxBid()[0]:
                        do('ASK ' + companies[i].name + ' ' + str(companies[i].maxBid()[0]) + ' ' + str(companies[i].maxBid()[3]))
            if currTime > 120:
                print(2)
                companies = compData()
                for i in range(0, 5):
                    do('ASK ' + companies[i].name + ' ' + str(companies[i].maxBid()[0]) + ' ' + str(dividend[1][i]))
                for i in range(5, 10):
                        do('BID ' + companies[i].name + ' ' + str(companies[i].minAsk()[0]) + ' ' + str(2))
                for i in range(5, 10):
                    if (companies[1].marBid() + companies[1].marAsk()) / 2 < companies[i].maxBid()[0]:
                        do('ASK ' + companies[i].name + ' ' + str(companies[i].maxBid()[0]) + ' ' + str(companies[i].maxBid()[1]))
            print(dividendPerShare()[1])
    except Exception as e:
        print(str(e))
        start()

start()