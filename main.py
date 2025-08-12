from src.game.game_logic import WordleGame
from src.game.word_manager import WordManager
from src.utils.input_validator import InputValidator
from src.utils.display import Display

def main():
    # Inicializar componentes do jogo
    word_manager = WordManager('data/wordlist.txt')
    game = WordleGame()
    display = Display()
    
    # Iniciar novo jogo
    target_word = word_manager.get_random_word()
    game.start_game(target_word)
    
    # Mostrar mensagem de boas-vindas
    display.show_welcome()
    
    # Loop principal do jogo
    while not game.game_over:
        # Obter entrada do usuário
        guess = input(f"Tentativa {game.current_attempt + 1}/6: ").strip()
        
        # Validar entrada
        is_valid, error_message = InputValidator.validate_guess(guess)
        if not is_valid:
            print(error_message)
            continue
            
        # Verificar se é uma palavra válida
        if not word_manager.is_valid_word(guess):
            print("Palavra não está na lista de palavras válidas!")
            continue
        
        # Processar tentativa e mostrar feedback
        feedback = game.make_guess(guess)
        print(display.show_feedback(feedback))
    
    # Mostrar mensagem de fim de jogo
    display.show_game_over(game.won, game.target_word)

if __name__ == "__main__":
    main()
