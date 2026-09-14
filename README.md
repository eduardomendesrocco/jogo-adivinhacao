# Código...

import random

currently_available_difficulties = [1, 2, 3, 4, 5]
diffculty_string = {
    "1": "Iniciante",
    "2": "Fácil",
    "3": "Médio",
    "4": "Difícil",
    "5": "Impossível"
}
def game(guess):
    print("             | Dificuldades |")
    print("=" * 45)
    print(f"             Iniciante  -> 1\n"
          f"             Fácil      -> 2\n"
          f"             Médio      -> 3\n"
          f"             Difícil    -> 4\n"
          f"             Impossível -> 5")
    print("=" * 45 + "\n")

    dificuldade = int(input("Digite o nível de dificuldade (aumentará a amplitude entre os possíveis números) -> "))

    if dificuldade not in currently_available_difficulties:
        dificuldade = int(input(f"{dificuldade} não é uma opção válida, tente novamente -> "))

    else:
        string = str(dificuldade)
        print(f"Bem-vindo ao Jogo da Adivinhação\n"
              f"||  Dificuldade: {diffculty_string[string]}  ||")



chute = int(input())
if __name__ == "__main__":
    game(chute)
