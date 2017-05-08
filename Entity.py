import Stage
import Card
from random import shuffle

class Entity:
    def __init__(self,x,y,stage): #server should ensure Entity is being created in valid location
        self.posx=x
        self.posy=y
        self.symbol="#" #Error symbol, should never appear
        self.movepoints=0
        self.stage=stage
        stage.occupy(self,x,y)
        

class Player(Entity):
    def __init__(self,x,y,stage,symbol):
        Entity.__init__(self,x,y,stage)
        self.handlimit=5 #make ability to change that
        self.symbol=symbol
        self.deck=[]#change to getdeck(name)
        self.hand=[]
        self.grave=[]
        self.mana=()#todo
    def getdeck(self,source):
        f=open(source,"r")
        self.deck=[]
        for i in range(100):
            self.deck.append(Card.d[f.readline().strip()]())#test this
        shuffle(self.deck)
    def draw(self):
        while(self.hand.size()<self.handlimit):
            if (self.deck.size!=0):
                self.hand.append(self.deck.pop(0))
            else:
                print('no cards in deck') #change later
    def play1(self,c):
        c.effect1(self)
        self.grave.append(c)
        self.hand.remove(c)
    def play2(self,c):
        #this one is more complicated, needs for mana, if effect exists, etc
        c.effect2(self)
        self.grave.append(c)
        self.hand.remove(c)
    def takedamage(self, amount):
        self.grave.extend(self.deck[:amount])
        self.deck=self.deck[amount:]
        

#class Summon(Entity):
