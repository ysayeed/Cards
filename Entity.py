import Stage
import Card
from random import shuffle

class Entity:
    def __init__(self,x,y,stage): #server should ensure Entity is being created in valid location
        self.posx=x
        self.posy=y
        self.symbol="#" #Error symbol, should never appear
        self.movepoints=0
        self.teleportpoints=0
        self.stage=stage
        stage.occupy(self,x,y)
        

class Player(Entity):
    def __init__(self,x,y,stage,symbol,source):
        Entity.__init__(self,x,y,stage)
        self.handlimit=5 #make ability to change that
        self.symbol=symbol
        self.deck=[]
        self.getdeck(source)
        self.hand=[]
        self.draw()
        self.grave=[]
        self.mana=()#todo
    def getdeck(self,source):
        f=open(source,"r")
        self.deck=[]
        for i in range(10):#change to 100 when more cards
            self.deck.append(Card.d[f.readline().strip()]())
        f.close()
        shuffle(self.deck)
    def draw(self):
        while(len(self.hand)<self.handlimit):
            if (len(self.deck)!=0):
                self.hand.append(self.deck.pop(0))
            else:
                print('no cards in deck') #change later
    def play1(self,c,*args):
        if c not in self.hand:
            pass #throw exception
        c.effect1(self,*args)
        self.grave.append(c)
        self.hand.remove(c)
    def play2(self,c,*args):
        if c not in self.hand:
            pass #throw exception
        #this one is more complicated, needs for mana, if effect exists, etc
        c.effect2(self,*args)
        self.grave.append(c)
        self.hand.remove(c)
    def takedamage(self, amount):
        self.grave.extend(self.deck[:amount])
        self.deck=self.deck[amount:]
    def remainingcards(self):
        return sorted(self.deck)
    def move(self,direction):
        if (sum(direction)<=self.movepoints):
            if (self.stage.move(self.posx,self.posy,direction)):
                self.movepoints-=sum(direction)

class Summon(Entity):
    def __init__(self,x,y,stage,symbol):
        Entity.__init__(self,x,y,stage)
        self.symbol=symbol
        self.ai=None
        self.lifespan=None
        
