class WordleGame:
    def __init__(self):
        self.max_attempts = 6
        self.word_length = 5
        self.current_attempt = 0
        self.target_word = None
        self.game_over = False
        self.won = False

    def start_game(self, word):
        """Initialize a new game with a target word."""
        self.target_word = word.upper()
        self.current_attempt = 0
        self.game_over = False
        self.won = False

    def make_guess(self, guess):
        """Process a guess and return feedback."""
        if self.game_over:
            return None

        if self.current_attempt >= self.max_attempts:
            self.game_over = True
            return None

        guess = guess.upper()
        feedback = self._check_guess(guess)
        self.current_attempt += 1

        if guess == self.target_word:
            self.won = True
            self.game_over = True

        if self.current_attempt >= self.max_attempts:
            self.game_over = True

        return feedback

    def _check_guess(self, guess):
        """Check the guess against the target word and return feedback."""
        feedback = []
        for i, letter in enumerate(guess):
            if letter == self.target_word[i]:
                feedback.append(('correct', letter))
            elif letter in self.target_word:
                feedback.append(('present', letter))
            else:
                feedback.append(('absent', letter))
        return feedback

    def get_game_state(self):
        """Return the current state of the game."""
        return {
            'attempts_left': self.max_attempts - self.current_attempt,
            'game_over': self.game_over,
            'won': self.won
        }
