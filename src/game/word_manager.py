import random

class WordManager:
    def __init__(self, word_file_path):
        self.word_file_path = word_file_path
        self.words = self._load_words()

    def _load_words(self):
        """Load words from the word list file."""
        try:
            with open(self.word_file_path, 'r') as file:
                return [word.strip().upper() for word in file if len(word.strip()) == 5]
        except FileNotFoundError:
            return []

    def get_random_word(self):
        """Get a random word from the word list."""
        if not self.words:
            raise ValueError("No words available")
        return random.choice(self.words)

    def is_valid_word(self, word):
        """Check if a word is in the word list."""
        return word.upper() in self.words
