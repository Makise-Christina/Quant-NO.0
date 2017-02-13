# 2 random investors

import numpy as np
from methods_UI.method_1 import draw_line

# basic expected price
Exp1 = 10.0
Exp2 = 8.0

P1 = np.array([])
P2 = np.array([])

# Exp function
def f(U, P, bP):
    dp = U+P+bP
    return dp

for i in xrange(0, 240):
    Exp1 += f(0+i, 1, 2)
    Exp2 += f(2+2*i, 3, 4)

    P1 = np.append(P1, Exp1)
    P2 = np.append(P2, Exp2)

X = np.linspace(0, 240, 240, endpoint = True)
# P = np.random.random_sample(240) * 10 + 5
# print (type(X))
# draw_line(P, X)

print (P1)
print (P2)
draw_line(P1, X)
