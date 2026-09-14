import random
amplitude_numeros = {
    "1": 10,
    "2": 50,
    "3": 125,
    "4": 300,
    "5": 1000
}

currently_available_difficulties = [1, 2, 3, 4, 5]

difficult_string = {
    "1": "Iniciante",
    "2": "Fácil",
    "3": "Médio",
    "4": "Difícil",
    "5": "Impossível"
}

print("             | Dificuldades |")
print("=" * 45)
print(f"            | Iniciante  -> 1\n"
      f"            | Fácil      -> 2\n"
      f"            | Médio      -> 3\n"
      f"            | Difícil    -> 4\n"
      f"            | Impossível -> 5")
print("=" * 45 + "\n")

tentativas = 0
dificuldade = int(input("Digite o nível de dificuldade (aumentará a amplitude entre os possíveis números) -> "))

while dificuldade not in currently_available_difficulties:
    dificuldade = int(input(f"{dificuldade} não é uma opção válida, tente novamente -> "))

else:
    print(f"\nBem-vindo ao Jogo da Adivinhação\n"
          f"||  Dificuldade: {difficult_string[str(dificuldade)]}  ||")

    numero_secreto = random.randint(1, amplitude_numeros[str(dificuldade)])
    tentativa = -1

    while tentativa != numero_secreto:
        tentativa = int(input(f"Digite um número de 1-{amplitude_numeros[str(dificuldade)]} -> "))
        tentativas += 1

        if tentativa > numero_secreto:
            print(f"▼ Muito alto! Tente um número menor... ▼\n")
        elif tentativa < numero_secreto:
            print(f"▲ Muito baixo! Tente um número maior... ▲\n")

    print("\n" + "=~" * 21)
    print(f"| Parabéns, você acertou o número secreto!\n"
          f"| Tentativas necessárias -> {tentativas}\n"
          f"| Número secreto -> {numero_secreto}")
    print("=~" * 21)