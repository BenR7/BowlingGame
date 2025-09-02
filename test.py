
import unittest
from bowling_game import BowlingGame

testGame = BowlingGame()

"""
Unit tests for the BowlingGame module
"""

# Testing for the roll() function 

class Testing(unittest.TestCase):
    
    def setUp(self):
        self.game = BowlingGame()

    def test_single_roll(self):
        self.game.roll(5)
        self.assertEqual(self.game.rolls, [5])
        self.assertEqual(self.game.current_roll, 1)

    def test_multiple_rolls(self):
        self.game.roll(1)
        self.game.roll(8)
        self.game.roll(6)
        self.game.roll(10)
        self.assertEqual(self.game.rolls, [1, 8, 6, 10])
        self.assertEqual(self.game.current_roll, 4)


# Tests for score() function
    

    def test_normal_game(self):
        self.game.roll(7)
        self.game.roll(2)

        self.game.roll(2)
        self.game.roll(3)

        self.game.roll(1)
        self.game.roll(1)

        self.game.roll(5)
        self.game.roll(4)

        self.game.roll(6)
        self.game.roll(1)

        self.game.roll(2)
        self.game.roll(4)

        self.game.roll(8)
        self.game.roll(1)

        self.game.roll(6)
        self.game.roll(2)

        self.game.roll(7)
        self.game.roll(1)

        self.game.roll(2)
        self.game.roll(2)

        self.assertEqual(len(self.game.rolls), 20)
        self.assertEqual(self.game.score(), 67)

    def test_all_gutterballs(self):
        
        for _ in range(20):
            self.game.roll(0)

            
        self.assertEqual(len(self.game.rolls), 20)
        self.assertEqual(self.game.score(), 0)


    def test_perfect_game(self):

        for _ in range(12):
            self.game.roll(10)

        
        self.assertEqual(len(self.game.rolls), 12)
        self.assertEqual(self.game.score(), 300)



    def test_all_spares(self):

        for _ in range(21):
            self.game.roll(5)


        self.assertEqual(len(self.game.rolls), 21)
        self.assertEqual(self.game.score(), 150)


if __name__ == '__main__':
    unittest.main()