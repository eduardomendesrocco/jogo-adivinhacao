# 🎯 Jogo de Adivinhação

Um jogo de adivinhação de números feito em Python, com níveis de dificuldade que alteram a amplitude do intervalo de números possíveis.

## 📋 Como funciona

O programa sorteia um número secreto num intervalo (conforme a dificuldade escolhida) e o jogador precisa de adivinhar qual é esse número. A cada tentativa, o jogo informa se o palpite foi maior ou menor que o número secreto, até o jogador acertar.

Ao final, é exibido o número total de tentativas usadas e o número secreto sorteado.

## 🎮 Como jogar

1. Execute o script.
2. Escolha um nível de dificuldade digitando o número correspondente (1 a 5).
3. Digite um número dentro do intervalo indicado.
4. Siga as dicas (▲ maior / ▼ menor) até acertar o número secreto.
5. Veja o seu total de tentativas ao final da partida.

## 🕹️ Níveis de dificuldade

| Nível | Dificuldade | Intervalo |
|:-----:|-------------|:---------:|
| 1 | Iniciante | 1 - 10 |
| 2 | Fácil | 1 - 50 |
| 3 | Médio | 1 - 125 |
| 4 | Difícil | 1 - 300 |
| 5 | Impossível | 1 - 1000 |

## ▶️ Como executar

Requer Python 3 instalado. Nenhuma dependência externa é necessária (usa apenas a biblioteca padrão `random`).

```bash
python jogo_adivinhacao.py
```

## 🛠️ Tecnologias

- Python 3
- Biblioteca `random` (módulo padrão)

## 📌 Exemplo de execução

```
             | Dificuldades |
=============================================
            | Iniciante  -> 1
            | Fácil      -> 2
            | Médio      -> 3
            | Difícil    -> 4
            | Impossível -> 5
=============================================

Digite o nível de dificuldade (aumentará a amplitude entre os possíveis números) -> 1

Bem-vindo ao Jogo da Adivinhação
||  Dificuldade: Iniciante  ||
Digite um número de 1-10 -> 5
▲ Muito baixo! Tente um número maior... ▲

Digite um número de 1-10 -> 8
Parabéns, você acertou o número secreto!
```