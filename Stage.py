down=(1,0)
up=(-1,0)
left=(0,-1)
right=(0,1) #(row, column)
directions=[down,up,left,right]
d={}

class Tile:
    def __init__(self,x,y):
        self.posx=x
        self.posy=y
        self.cost=1
        self.block=False
        self.occupant=None
        self.symbol=None
        self.trap=None
    
class Empty(Tile):
    def __init__(self,x,y):
        Tile.__init__(self,x,y)
        self.symbol="."
d["."]=Empty

class Wall(Tile):
    def __init__(self,x,y):
        Tile.__init__(self,x,y)
        self.symbol="X"
        self.block=True
d["X"]=Wall

class Stage:
    #d={".":Empty, "X":Wall}
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
                self.grid[i].append(d[c](i,j))
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
    def settrap(self,trap,x,y):
        self.grid[x][y].trap=trap
    def remove(self,x,y):
        self.grid[x][y].occupant=None

    def move(self,x,y,direction):
        if True:#add movement check
            #swap occupants, movement check will prevent swap of hostile entities
            temp=self.grid[x][y].occupant
            self.grid[x][y].occupant=self.grid[x+direction[1]][y+direction[0]].occupant
            if(self.grid[x][y].occupant):
                self.grid[x][y].occupant.posx=x
                self.grid[x][y].occupant.posy=y
            self.grid[x+direction[1]][y+direction[0]].occupant=temp
            if(self.grid[x+direction[1]][y+direction[0]].occupant):
                self.grid[x+direction[1]][y+direction[0]].occupant.posx=x+direction[1]
                self.grid[x+direction[1]][y+direction[0]].occupant.posy=y+direction[0]
            return True;
        
