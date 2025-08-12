import unittest
from src.game.word_manager import WordManager

class TestWordManager(unittest.TestCase):
    def setUp(self):
        self.word_manager = WordManager('data/wordlist.txt')

    def test_word_validation(self):
        self.assertTrue(self.word_manager.is_valid_word("teste"))
        self.assertFalse(self.word_manager.is_valid_word("invalid"))

    def test_random_word(self):
        word = self.word_manager.get_random_word()
        self.assertEqual(len(word), 5)
        self.assertTrue(self.word_manager.is_valid_word(word))

if __name__ == '__main__':
    unittest.main()
