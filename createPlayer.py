# create players
from investor import Investor
import random

def createByer(nBuy):
    Byer = []
    for i in xrange(int(nBuy * 0.9)):
        Byer.append(Investor(random.randint(2700,3000), 1, random.uniform(0,3), 0))
    for i in xrange(int(nBuy * 0.1)):
        Byer.append(Investor(random.randint(3000,3300), 1, random.uniform(0,1), 0))
    return Byer

def createSler(nSel):
    Sler = []
    for i in xrange(nSel):
        Sler.append(Investor(random.randint(2700,3300), -1, random.uniform(0,1), 0))
    return Sler

def createByerWithParm(nBuy, exp, parm1):
    Byer = []
    for i in xrange(nBuy):
        Byer.append(Investor(exp, 1, parm1, 0))
    return Byer
