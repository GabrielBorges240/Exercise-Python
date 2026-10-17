from random import choice 
jogada =  ["Pedra", "Papel", "Tesoura"]

print('''Sua jogada é: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

if __name__ == '__main__':
    jogador = int(input('Qual é a sua jogada? '))
    computador = choice(jogada)
    print(f'Computador jogou: {computador}')
    print(f'Jogador jogou: {jogada[jogador]}')

    if jogador == 0 and computador == "Tesoura":
        print("Jogador Venceu!")
    elif jogador == 1 and computador == "Pedra":
        print("Jogador Venceu!")
    elif jogador == 2 and computador == "Papel":
        print("Jogador Venceu!")
    elif jogador == 0 and computador == "Papel":
        print("Computador Venceu!")
    elif jogador == 1 and computador == "Tesoura":
        print("Computador Venceu!")
    elif jogador == 2 and computador == "Pedra":
        print("Computador Venceu!")
    else:
        print("Empate!") 
 
    
     



