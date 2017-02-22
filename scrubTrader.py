from compData import *
from client import *
from interface import do
import time
from random import randint


def start():
    try:
        startTime = time.time()
        while True:
            companies = compData()
            cash1 = cash();
            print(cash1)
            for j in range(0, 9):
                i = randint(0,11)
                do('BID ' + companies[i].name + ' ' + str(companies[i].minAsk()[0]) + ' ' + str(15))
                do('BID ' + companies[i].name + ' ' + str(companies[i].minAsk()[0]) + ' ' + str(10))
                do('BID ' + companies[i].name + ' ' + str(companies[i].minAsk()[0]) + ' ' + str(1))
                i = randint(0,11)
                do('ASK ' + companies[i].name + ' ' + str(companies[i].maxBid()[0]) + ' ' + str(15))
                do('ASK ' + companies[i].name + ' ' + str(companies[i].maxBid()[0]) + ' ' + str(10))
                do('ASK ' + companies[i].name + ' ' + str(companies[i].maxBid()[0]) + ' ' + str(3))
            # dividend = dividendPerShare();
            # print(dividend)

    except Exception as e:
        print(str(e))
        start()

start()