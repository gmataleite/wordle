class InputValidator:
    @staticmethod
    def validate_guess(guess, word_length=5):
        """Validate user input for a guess."""
        if not guess.isalpha():
            return False, "A palavra deve conter apenas letras"
        
        if len(guess) != word_length:
            return False, f"A palavra deve ter {word_length} letras"
        
        return True, ""
