# define class investor

class Investor:
    invCount = 0
    def __init__(self, Exp, Status, parm1, parm2):
        self.parm1 = parm1
        self.parm2 = parm2

        self.Exp = Exp
        self.Status = Status
        self.id = Investor.invCount
        Investor.invCount += 1

        self.histExp = []

    def __lt__(self, other):
        return self.Exp < other.Exp

    def displayParm(self):
        # print (str(self.parm1) + " " + str(self.parm2))
        print (self.id)
        print (self.Exp * self.Status)
