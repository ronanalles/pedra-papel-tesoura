import random

def jogo_pedra_papel_tesoura():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    jogador_escolha = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()
    computador_escolha = random.choice(opcoes)

    print(f"Computador escolheu: {computador_escolha}")

    if jogador_escolha == computador_escolha:
        print("Empate!")
    elif (jogador_escolha == "Pedra" and computador_escolha == "Tesoura") or \
         (jogador_escolha == "Papel" and computador_escolha == "Pedra") or \
         (jogador_escolha == "Tesoura" and computador_escolha == "Papel"):
        print(f"Você ganhou! {jogador_escolha} vence {computador_escolha}.")
    else:
        print(f"Você perdeu! {computador_escolha} vence {jogador_escolha}.")

jogo_pedra_papel_tesoura()
