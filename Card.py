d={}

class Card:
    def __init__(self):
        self.name=None
        self.element=None
        self.cost=None
    def effect1(self,user,*args):
        pass
    def effect2(self,user,*args):
        pass

class Basicmove(Card):
    def __init__(self):
        Card.__init__(self)
        self.name="basicmove"
    def effect1(self, user,*args):
        user.movepoints+=2
d["basicmove"]=Basicmove

class Basicattack(Card):
    def __init(self):
        Card.__init__(self)
        self.name="basicmove"
    def effect1(self,user,*args):
        print("change this")

d["basicattack"]=Basicattack
