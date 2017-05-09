import unittest
import Stage
import Entity
import Card

class Test(unittest.TestCase):
    def test_Stage(self):
        s=Stage.Stage(3,3,"teststage.txt")
        self.assertEqual(s.printgrid(),"X.X\nX..\n...\n")
        e=Entity.Player(1,1,s,"T","testdeck.txt")
        self.assertEqual(s.grid[1][1].occupant.symbol,"T")
        self.assertEqual(s.printgrid(),"X.X\nXT.\n...\n")
        s.move(1,1,(0,1))
        self.assertEqual(s.printgrid(),"X.X\nX..\n.T.\n")
        self.assertIsNotNone(s.grid[2][1].occupant)
        self.assertIsNone(s.grid[1][1].occupant)
        self.assertEqual(type(s.grid[0][0]).__name__,"Wall")
        self.assertEqual(type(s.grid[0][1]).__name__,"Empty")
    def test_Entity(self):
        s=Stage.Stage(3,3,"teststage.txt")
        e=Entity.Player(1,1,s,"T","testdeck.txt")
        self.assertEqual(e.posx,1)
        self.assertEqual(e.posy,1)
        self.assertEqual(e.movepoints,0)
        self.assertEqual(e.stage,s)
        self.assertIsNotNone(s.grid[1][1].occupant)
        self.assertEqual(e.symbol,"T")
        self.assertEqual(e.handlimit,5)
        #test deck
        #test hand
        #test grave
        #test mana
        #test draw()
        


unittest.main()
