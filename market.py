from investor import Investor
import methods_UI.method_1 as md1
from epcFunc import expChangeFunc
import createPlayer
import random

# price limit
def limitPrice(P, cl):
    if P > cl * 1.1:
        return cl * 1.1
    if P < cl * 0.9:
        return cl * 0.9
    return P

# initiate value
finalPrice = []
finalAmunt = []
pstPrice = 50
pstValue = 0
pstAmnt = 0
Byer = []
Sler = []

# create buyer & seller
nBuy = 2000
nSel = 2000

Byer = createPlayer.createByer(nBuy)
Sler = createPlayer.createSler(nSel)

# get pstPrice
Byer.sort()
Sler.sort()
pstPrice = (Byer[-1].Exp + Sler[0].Exp) / 2
openP = pstPrice

# simulate
for i in xrange(240):
    finalAmunt.append(pstAmnt * 10)
    pstValue = 0
    pstAmnt = 0
    print (i)

    # randomly add buyer and seller
    Byer += createPlayer.createByer(random.randint(0,20))
    Sler += createPlayer.createSler(random.randint(0,20))

    if i == 60:
        Byer += createPlayer.createByerWithParm(1500, pstPrice, 300)

    for b in Byer:
        b.histExp.append(b.Exp)
        b.Exp += expChangeFunc(b, pstPrice, 0, i)
        b.Exp = limitPrice(b.Exp, openP)
        if b.Status == 1:
            tResult, bexp, sexp = b.tryBuy(Sler)
            if tResult:
                # print ("Time: " + str(i))
                # print ("Buy: " + str(bexp) + "  Sell: " + str(sexp))
                # print ("")
                # del b
                # del Sler[0]
                # Sler.append(Investor(sexp * (1 + random.uniform(0,0.1)), -1, random.uniform(0,1), 0))
                pstValue += sexp
                pstAmnt += 1

    for s in Sler:
        s.histExp.append(s.Exp)
        s.Exp += expChangeFunc(s, pstPrice, 0, i)
        s.Exp = limitPrice(s.Exp, openP)
        if s.Status == 1:
            tResult, sexp, bexp = s.trySel(Byer)
            if tResult:
                # print ("Time: " + str(i))
                # print ("Buy: " + str(bexp) + "  Sell: " + str(sexp))
                # print ("")
                pstValue += bexp
                pstAmnt += 1

    finalPrice.append(pstPrice)
    if pstAmnt != 0:
        pstPrice = pstValue / pstAmnt

# print plot
md1.resetPlot(openP)
# for b in Byer:
    # md1.drawLine(b.histExp)
# for s in Sler:
    # md1.drawLine(s.histExp)
md1.drawLine(finalPrice)
md1.drawBar(finalAmunt)
md1.drawAll()
