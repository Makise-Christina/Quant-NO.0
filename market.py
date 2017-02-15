from investor import Investor
import random

Ins = []
for i in xrange(5):
    Ins.append(Investor(0,0))

for i in xrange(240):
    for a in Ins:
        a.Exp += a.parm1
