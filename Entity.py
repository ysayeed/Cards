import Stage
import Card
from random import shuffle

class Entity:
    def __init__(self,x,y,stage,team): #server should ensure Entity is being created in valid location
        self.posx=x
        self.posy=y
        self.symbol="#" #Error symbol, should never appear
        self.movepoints=0
        self.teleportpoints=0
        self.damagereduction=0
        self.stage=stage
        self.team=team
        stage.occupy(self,x,y)
    def endturn(self):
        pass
        

class Player(Entity):
    def __init__(self,x,y,stage,symbol,team,source):
        Entity.__init__(self,x,y,stage,team)
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
        amount=max(amount-self.damagereduction,0)
        self.grave.extend(self.deck[:amount])
        self.deck=self.deck[amount:]
    def remainingcards(self):
        return sorted(self.deck)
    def move(self,direction):
        if (sum(direction)<=self.movepoints):
            if (self.stage.move(self.posx,self.posy,direction)):
                self.movepoints-=sum(direction)
    def endturn(self):#incomplete
        self.draw()

class Trap:
    def __init__(self,x,y,stage,symbol,team):
        self.posx=x
        self.posy=y
        self.stage=stage
        self.symbol=symbol
        self.team=team
        stage.settrap(self,x,y)
    

class Summon(Entity):
    def __init__(self,x,y,stage,symbol,team):
        Entity.__init__(self,x,y,stage,team)
        self.symbol=symbol
        self.ai=None
        self.lifespan=None
        self.hp=None
        self.attacktype=None
        self.damage=1
    def endturn(self):
        if self.lifespan!=None:
            self.lifespan-=1
        if self.lifespan==0:
            self.stage.remove(self.x,self.y)
    def move(self):
        if self.ai=="Random":
            shuffle(Stage.directions)
            while(not(self.stage.move(self.posx,self.posy,Stage.directions[0]))):
                shuffle(Stage.directions)
    def attack(self):
        if self.attacktype=="Close":
            for x in Stage.directions:
                #check boundaries, prevent wraparound
                temp=self.stage.grid[self.posx+x[0]][self.posy+x[1]]
                if temp.occupant!=None and temp.occupant.team!=self.team:
                    temp.occupant.takedamage(self.damage)
                    break
        elif self.attacktype=="Ranged":
            for x in Stage.directions:
                temp=self.stage.grid[self.posx+x[0]][self.posy+x[1]]
                done=False
                i=0
                while True:
                    if temp.occupant!=None and temp.occupant.team!=self.team:
                        temp.occupant.takedamage(self.damage)
                        done=True
                        break
                    elif temp.block:
                        break
                    i+=1
                    #deal with wraparound
                    temp=self.stage.grid[self.posx+i*x[0]][self.posy+i*x[1]]
                if done==True:
                    break
    def takedamage(self, amount):
        amount=max(amount-self.damagereduction,0)
        self.hp-=amount
        if self.hp<=0:
            self.stage.remove(self.posx,self.posy)

class Rat(Summon):
    def __init__(self,x,y,stage,symbol,team):
        Summon.__init__(self,x,y,stage,symbol,team)
        self.ai="Random"
        self.lifespan=4
        self.hp=1
        self.attacktype="Close"

class Turret(Summon):
    def __init__(self,x,y,stage,symbol,team):
        Summon.__init__(self,x,y,stage,symbol,team)
        self.ai="None"
        self.lifespan=5
        self.hp=10

