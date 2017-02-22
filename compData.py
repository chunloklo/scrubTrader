import socket
import sys
from client import *
from enum import Enum
import numpy

compNames = enumerate(['AMZN', 'DIS','FB','GOOGL','IBM', 'IVW','KING', 'KO', 'NFLX', 'TSLA'])
compNames = list(compNames)
class Company:
    def __init__(self, name, net_worth, dividend, volatil):
        self.name = name
        self.net_worth = net_worth
        self.dividend = dividend
        self.volatil = volatil
        self.bid = []
        self.ask = []
    def addBid(self, amount, count):
        self.bid.append((amount, count))
    def addAsk(self, amount, count):
        self.ask.append((amount, count))
    def maxBid(self):
        return max(self.bid)
    def minAsk(self):
        return min(self.ask)

    def marBid(self):
        return max(self.bid, key=lambda x: x[1])
    def marAsk(self):
        return max(self.ask, key=lambda x: x[1])

    def __str__(self):
        string = '\nName:' + self.name + '\n' \
        'Net_worth:' + str(self.net_worth) + '\n' \
        'Dividend:' + str(self.dividend) + '\n' \
        'Volatility:' + str(self.volatil) + '\n' \
        'Bid:' + str(self.bid) + '\n' \
        'Ask:' + str(self.ask) + '\n' \
        '////////////////////////////'
        return string
    def __repr__(self):
        return self.__str__()

def compData():
    #get security data
    sys.stdout = open("securities_out.txt", "w")
    run('curryInAHurry', 'pastaman', 'SECURITIES')
    sys.stdout = sys.__stdout__

    #parce security data
    compNames = [];
    name_data= open("securities_out.txt", "r")
    data = name_data.read().split()
    for k in data:
        if k == 'SECURITIES_OUT':
            continue
        if any(char.isdigit() for char in k) == False:
            compNames.append(k)
    compNames = enumerate(compNames)
    compNames = list(compNames)

    securities_data = numpy.genfromtxt('securities_out.txt')
    securities_data = securities_data[numpy.logical_not(numpy.isnan(securities_data))]
    securities_out = numpy.zeros((12, 3))
    x = 0
    for i in range (0,10):
        for j in range (0, 3):
            securities_out[i][j] = securities_data[x]
            x += 1

    #get security order
    sys.stdout = open("securities_order.txt", "w")
    for i, name in compNames:
        run('curryInAHurry', 'pastaman', 'ORDERS ' + name)
    sys.stdout.close();
    sys.stdout = sys.__stdout__

    order_data = open("securities_order.txt", "r")
    data = order_data.read().split()
    order_data.close()

    companies = []
    for i, name in compNames:
        companies.append(Company(name, securities_out[i][0], securities_out[i][1], securities_out[i][2]))

    order_data = []
    i = 0;
    while(i < len(data)):
        if data[i] == 'BID':
            for j, name in compNames:
                if name == data[i + 1]:
                    companies[j].addBid(float(data[i + 2]), int(data[i + 3]))
                    i += 3
        elif data[i] == 'ASK':
            for j, name in compNames:
                if name == data[i + 1]:
                    companies[j].addAsk(float(data[i + 2]), int(data[i + 3]))
                    i += 3
        else:
            i += 1

    return companies

def cash():
    sys.stdout = open("myCash.txt", "w")
    run('curryInAHurry', 'pastaman', 'MY_CASH')
    sys.stdout.close();
    sys.stdout = sys.__stdout__
    name_data= open("myCash.txt", "r")
    data = name_data.read().split()
    return float(data[1])

def dividendPerShare():
    sys.stdout = open("dividend.txt", "w")
    run('curryInAHurry', 'pastaman', 'MY_SECURITIES')
    sys.stdout.close();
    sys.stdout = sys.__stdout__
    data = numpy.genfromtxt('dividend.txt')
    data = data[numpy.logical_not(numpy.isnan(data))]
    dividendPerShare = numpy.zeros(12)
    share = numpy.zeros(12)
    j = 0;
    for i in range(0, 12):
        if float(data[j]) != 0:
            dividendPerShare[i] = float(data[j + 1]) / float(data[j])
            share[i] = int(data[j])
        j += 2
    return [dividendPerShare, share]



# run('curryInAHurry', 'pastaman', 'MY_CASH')
# run('curryInAHurry', 'pastaman', 'SECURITIES')
# run('curryInAHurry', 'pastaman', 'BID DIS 19.9 10')
# run('curryInAHurry', 'pastaman', 'MY_CASH')
# run('curryInAHurry', 'pastaman', 'MY_SECURITIES')
# run('curryInAHurry', 'pastaman', 'MY_ORDERS')
# run('curryInAHurry', 'pastaman', 'SECURITIES')
