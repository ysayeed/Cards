import Entity

class Card:
    def __init__(self):
        self.name=None
        self.element=None
    def effect1(self):
        pass
    def effect2(self):
        pass

class Basicmove(Card):
    def __init__(self):
        Card.__init__(self)
        self.name="basicmove"
    def effect1(self, user):
        user.movepoints+=2
