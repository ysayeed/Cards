import Stage
import Card

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
        self.deck=[]#todo
        self.hand=[]
        self.grave=[]
        self.mana=()#todo
    def draw(self):
        while(self.hand.size()<self.handlimit):
            if (self.deck.size!=0):
                self.hand.append(self.deck.pop(0))
            else:
                print('no cards in deck') #change later
        

#class Summon(Entity):
    
