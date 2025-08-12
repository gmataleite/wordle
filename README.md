# Wordle em Python 🎮

Um clone do famoso jogo Wordle implementado em Python, onde você tem 6 tentativas para adivinhar uma palavra de 5 letras.

## 🎯 Como Jogar

1. O jogo escolhe aleatoriamente uma palavra de 5 letras
2. Você tem 6 tentativas para adivinhar a palavra
3. Após cada tentativa, você receberá feedback:
   - 🟩 = letra correta na posição correta (verde)
   - 🟨 = letra correta na posição errada (amarelo)
   - ⬜ = letra não está na palavra (branco)

## 🚀 Como Executar

1. Certifique-se de ter Python 3.6 ou superior instalado
2. Clone este repositório:
   ```bash
   git clone https://github.com/gmataleite/wordle.git
   cd wordle
   ```
3. Execute o jogo:
   ```bash
   python main.py
   ```

## 📁 Estrutura do Projeto

```
wordle/
│
├── src/
│   ├── game/
│   │   ├── game_logic.py     # Lógica principal do jogo
│   │   └── word_manager.py   # Gerenciamento de palavras
│   │
│   └── utils/
│       ├── input_validator.py # Validação de entrada
│       └── display.py        # Interface com usuário
│
├── data/
│   └── wordlist.txt          # Lista de palavras válidas
│
├── tests/
│   ├── test_game_logic.py
│   └── test_word_manager.py
│
└── main.py                   # Ponto de entrada do jogo
```

## 🧪 Testes

Para executar os testes unitários:
```bash
python -m unittest discover tests
```

## 🎮 Exemplo de Jogada

```
Bem-vindo ao Wordle!
Tente adivinhar a palavra de 5 letras.

Tentativa 1/6: festa
⬜ 🟨 ⬜ ⬜ 🟩

Tentativa 2/6: preta
⬜ 🟨 🟨 ⬜ 🟩

Tentativa 3/6: testa
🟩 🟨 🟩 🟩 🟩

Tentativa 4/6: teste
🟩 🟩 🟩 🟩 🟩

Parabéns! Você acertou a palavra: teste
```

## 🛠️ Tecnologias Utilizadas

- Python 3.6+
- Unittest para testes

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✨ Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.