import unittest
from bowling import Game, Player, Frame

# class TestGame(unittest.TestCase):
#     def test_setUp(self):
#         anna = Player('Anna')
#         self.game = Game([anna])
#         self.assertEqual(self.game.play(), ['Anna: 0'])

#     def test_calculate(self):
#         anna = Player('Anna')
#         game = Game([anna])
#         game.bowl(1,anna,10,0)
#         game.bowl(2,anna,7,3)
#         game.bowl(3,anna,9,0)
#         game.bowl(4,anna,10,0)
#         game.bowl(5,anna,0,8)
#         game.bowl(6,anna,8,2)
#         game.bowl(7,anna,0,6)
#         game.bowl(8,anna,10,0)
#         game.bowl(9,anna,10,0)
#         game.bowl(10,anna,10,8,1)
#         self.assertEqual(game.play(), ['Anna: 167'])

        
        


# if __name__ == '__main__':
#     unittest.main()


anna = Player('Anna')
game = Game([anna])
game.bowl(1,anna,10,0)
game.bowl(2,anna,7,3)
game.bowl(3,anna,9,0)
game.bowl(4,anna,10,0)
game.bowl(5,anna,0,8)
game.bowl(6,anna,8,2)
game.bowl(7,anna,0,6)
game.bowl(8,anna,10,0)
game.bowl(9,anna,10,0)
game.bowl(10,anna,10,8,1)
print(game.play())