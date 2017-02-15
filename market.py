from investor import Investor
import methods_UI.method_1 as md1
from epcFunc import expChangeFunc
import random

# initiate value
finalPrice = []
pstPrice = 50
pstValue = 0
pstAmnt = 0
Byer = []
Sler = []

# create buyer & seller
nBuy = 500
nSel = 1500

for i in xrange(nBuy):
    Byer.append(Investor(random.randint(2700,2800), 1, random.randint(0,3), 0))
for i in xrange(nSel):
    Sler.append(Investor(random.randint(2700,3300), -1, random.randint(0,1), 0))

# get pstPrice
Byer.sort()
Sler.sort()
pstPrice = (Byer[-1].Exp + Sler[0].Exp) / 2
openP = pstPrice

# simulate
for i in xrange(240):
    pstValue = 0
    pstAmnt = 0

    for b in Byer:
        b.histExp.append(b.Exp)
        b.Exp += expChangeFunc(b, pstPrice, 0)
        if b.Status == 1:
            tResult, bexp, sexp = b.tryBuy(Sler)
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
            tResult, sexp, bexp = s.trySel(Byer)
            if tResult:
                print ("Time: " + str(i))
                print ("Buy: " + str(bexp) + "  Sell: " + str(sexp))
                print ("")
                pstValue += bexp
                pstAmnt += 1

    finalPrice.append(pstPrice)
    if pstAmnt != 0:
        pstPrice = pstValue / pstAmnt

# print plot
md1.resetPlot(openP)
for b in Byer:
    md1.drawLine(b.histExp)
for s in Sler:
    md1.drawLine(s.histExp)
md1.drawLine(finalPrice)
md1.drawAll()
