# define class investor

class Investor:
    invCount = 0
    def __init__(self, Exp, Status, parm1, parm2):
        self.parm1 = parm1
        self.parm2 = parm2

        # expected price
        # status 1=buyer, -1=seller, 0=invaled
        self.Exp = Exp
        self.Status = Status
        self.id = Investor.invCount
        Investor.invCount += 1

        self.histExp = []

    # for sort
    def __lt__(self, other):
        return self.Exp < other.Exp

    # buy & sell
    def tryBuy(self, Sler):
        Sler.sort()
        i = 0
        while i < len(Sler) and Sler[i].Exp <= self.Exp:
            if Sler[i].Status == -1:
                self.Status = 0
                Sler[i].Status = 0
                return True, self.Exp, Sler[i].Exp
            i += 1
        return False, 0, 0

    def trySel(self, Byer):
        Byer.sort()
        i = len(Byer) - 1
        while i > -1 and Byer[i].Exp >= self.Exp:
            if Byer[i].Status == 1:
                self.Status = 0
                Byer[i].Status = 0
                return True, self.Exp, Byer[i].Exp
            i -= 1
        return False, 0, 0

    def displayParm(self):
        # print (str(self.parm1) + " " + str(self.parm2))
        print (self.id)
        print (self.Exp * self.Status)
