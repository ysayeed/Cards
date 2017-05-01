class Tile:
    def __init__(self,x,y):
        self.posx=x
        self.posy=y
        self.type=None
        self.cost=1
        self.block=False
        self.occupant=None
        self.symbol=None
        
    
class Empty(Tile):
    def __init__(self,x,y):
        Tile.__init__(self,x,y)
        self.type="empty"
        self.symbol="."

class Wall(Tile):
    def __init__(self,x,y):
        Tile.__init__(self,x,y)
        self.type="wall"
        self.symbol="X"

class Stage:
    d={".":Empty, "X":Wall}
    def __init__(self,length,height,source):
        self.grid=[]
        self.gridsetup(length,height,source)
        
    def gridsetup(self,length,height,source):
        f=open(source,"r")
        self.grid=[]
        for i in range(height):
            self.grid.append([])
            for j in range(length):
                c=f.read(1)
                if (c=="\n"):
                    c=f.read(1)
                self.grid[i].append(Stage.d[c](i,j))
        f.close()
        
    def printgrid(self):
        s=""
        for i in self.grid:
            for j in i:
                if j.occupant!=None:
                   s+=j.occupant.symbol
                else:
                    s+=j.symbol
            s+="\n"
        return s
    
    def occupy(self,entity,x,y):
        self.grid[x][y].occupant=entity

    def move(self,x,y,direction):
        if True:#add movement check
            #swap occupants, movement check will prevent swap of hostile entities
            temp=self.grid[x][y].occupant
            self.grid[x][y].occupant=self.grid[x+direction[0]][y+direction[1]].occupant
            self.grid[x+direction[0]][y+direction[1]].occupant=temp
        
