# Test 1
# 10 investor, 5 buyer 5 seller
# 100 stocks on sale
# no price boundry
# cannot see the expected price of others
import methods_UI.method_1 as md1
import numpy as np
from investor import Investor
import random

# the dExp for the investor U at this moment
# U = Investor attributes
# P = realtime stock price
# dp = change rate of P
def expChangeFunc(U, P, dp):
    return (U.parm1 + (P - U.parm2) * 0.05 + dp) * U.Status

# player1 = Investor(1,2)
# player1.displayParm()

def __displayAll():
    for b in Byer:
        b.displayParm()
    for s in Sler:
        s.displayParm()

def tryBuy(Sler, b):
    Sler.sort()
    i = 0
    while i < len(Sler) and Sler[i].Exp <= b.Exp:
        if Sler[i].Status == -1:
            b.Status = 0
            Sler[i].Status = 0
            return True, b.Exp, Sler[i].Exp
        i += 1
    return False, 0, 0

def trySel(Byer, s):
    Byer.sort()
    i = len(Sler) - 1
    while i > -1 and Byer[i].Exp >= s.Exp:
        if Byer[i].Status == 1:
            s.Status = 0
            Byer[i].Status = 0
            return True, s.Exp, Byer[i].Exp
        i -= 1
    return False, 0, 0


# simulate
finalPrice = []
pstPrice = 50
pstValue = 0
pstAmnt = 0
Byer = []
Sler = []
for i in xrange(150):
    Byer.append(Investor(0, 1, random.randint(0,9), 0))
for i in xrange(150):
    Sler.append(Investor(100, -1, random.randint(0, 9), 0))

__displayAll()

for i in xrange(240):
    pstValue = 0
    pstAmnt = 0

    for b in Byer:
        b.histExp.append(b.Exp)
        b.Exp += expChangeFunc(b, pstPrice, 0)
        if b.Status == 1:
            tResult, bexp, sexp = tryBuy(Sler, b)
            if tResult:
                print ("Time: " + str(i))
                print ("Buy: " + str(bexp) + "  Sell: " + str(sexp))
                print ("")
                # del b
                # del Sler[0]
                pstValue += sexp
                pstAmnt += 1

    for s in Sler:
        s.histExp.append(s.Exp)
        s.Exp += expChangeFunc(s, pstPrice, 0)
        if s.Status == 1:
            tResult, sexp, bexp = trySel(Byer, s)
            if tResult:
                print ("Time: " + str(i))
                print ("Buy: " + str(bexp) + "  Sell: " + str(sexp))
                print ("")
                pstValue += bexp
                pstAmnt += 1

    finalPrice.append(pstPrice)
    if pstAmnt != 0:
        pstPrice = pstValue / pstAmnt

md1.resetPlot()
# for b in Byer:
    # md1.drawLine(b.histExp)
# for s in Sler:
    # md1.drawLine(s.histExp)
md1.drawLine(finalPrice)
md1.drawAll()
