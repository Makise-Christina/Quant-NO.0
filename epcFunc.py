# expected price change function
def expChangeFunc(U, P, dp, t):
    reVal = (U.parm1 * t  +  dp) * U.Status
    return int(reVal)
