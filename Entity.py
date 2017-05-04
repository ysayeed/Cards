import Stage

class Entity:
    def __init__(self,x,y,stage): #server should ensure Entity is being created in valid location
        self.posx=x
        self.posy=y
        self.symbol="#" #Error symbol, should never appear
        self.stage=stage
        self.movepoints=0
        stage.occupy(self,x,y)
        

class Player(Entity):
    def __init__(self,x,y,stage,symbol):
        Entity.__init__(self,x,y,stage)
        self.symbol=symbol
        self.deck=[]#todo
        self.grave=[]
        self.mana=()#todo
        

#class Summon(Entity):
    
