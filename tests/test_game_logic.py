import unittest
from src.game.game_logic import WordleGame

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game = WordleGame()
        self.game.start_game("teste")

    def test_correct_guess(self):
        feedback = self.game.make_guess("teste")
        self.assertTrue(self.game.won)
        self.assertTrue(all(status == "correct" for status, _ in feedback))

    def test_wrong_guess(self):
        feedback = self.game.make_guess("valor")
        self.assertFalse(self.game.won)
        self.assertFalse(self.game.game_over)

if __name__ == '__main__':
    unittest.main()
