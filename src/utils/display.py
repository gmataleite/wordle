class Display:
    @staticmethod
    def show_feedback(feedback):
        """Display the feedback for a guess."""
        display_symbols = {
            'correct': '🟩',  # Verde para letra correta na posição correta
            'present': '🟨',  # Amarelo para letra correta na posição errada
            'absent': '⬜'    # Branco para letra que não está na palavra
        }
        
        return ' '.join(display_symbols[status] for status, _ in feedback)

    @staticmethod
    def show_welcome():
        """Display welcome message."""
        print("\nBem-vindo ao Wordle!")
        print("Tente adivinhar a palavra de 5 letras.")
        print("🟩 = letra correta na posição correta")
        print("🟨 = letra correta na posição errada")
        print("⬜ = letra não está na palavra")
        print("\nVocê tem 6 tentativas. Boa sorte!\n")

    @staticmethod
    def show_game_over(won, target_word):
        """Display game over message."""
        if won:
            print(f"\nParabéns! Você acertou a palavra: {target_word}")
        else:
            print(f"\nGame Over! A palavra era: {target_word}")
