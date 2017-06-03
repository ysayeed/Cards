import unittest
import Stage
import Entity
import Card

class Test(unittest.TestCase):
    def test_Stage(self):
        s=Stage.Stage(3,3,"teststage.txt")
        self.assertEqual(s.printgrid(),"X.X\nX..\n...\n")
        e=Entity.Player(1,1,s,"T",0,"testdeck.txt")
        self.assertEqual(s.grid[1][1].occupant.symbol,"T")
        self.assertEqual(s.printgrid(),"X.X\nXT.\n...\n")
        s.move(1,1,(0,1))
        self.assertEqual(s.printgrid(),"X.X\nX..\n.T.\n")
        self.assertIsNotNone(s.grid[2][1].occupant)
        self.assertIsNone(s.grid[1][1].occupant)
        self.assertEqual(type(s.grid[0][0]).__name__,"Wall")
        self.assertEqual(type(s.grid[0][1]).__name__,"Empty")
    def test_Player(self):
        s=Stage.Stage(3,3,"teststage.txt")
        e=Entity.Player(1,1,s,"T",0,"testdeck.txt")
        self.assertEqual(e.posx,1)
        self.assertEqual(e.posy,1)
        self.assertEqual(e.movepoints,0)
        self.assertEqual(e.stage,s)
        self.assertIsNotNone(s.grid[1][1].occupant)
        self.assertEqual(e.symbol,"T")
        self.assertEqual(e.handlimit,5)
        self.assertEqual(len(e.hand),5)
        self.assertEqual(len(e.deck),5) #change this when deck size changes
        e.play1(e.hand[0])#change this when deck contains more types of Card
        self.assertEqual(e.movepoints,2)#change this with above
        self.assertEqual(len(e.hand),4)
        self.assertEqual(len(e.grave),1)
        e.draw()
        self.assertEqual(len(e.hand),5)
        self.assertEqual(len(e.deck),4)#change when deck size changes
        #test mana
    def test_Summon(self):
        s=Stage.Stage(3,3,"teststage.txt")
        e=Entity.Player(0,1,s,"T",0,"testdeck.txt")
        r=Entity.Rat(1,1,s,"R",1)
        r.attack()
        self.assertEqual(len(e.deck),4)
        self.assertEqual(len(e.grave),1)
        


unittest.main()
