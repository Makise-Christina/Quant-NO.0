# expected price change function
def expChangeFunc(U, P, dp):
    return (U.parm1 + (P - U.parm2) * 0.05 + dp) * U.Status
