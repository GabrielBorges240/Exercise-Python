from random import randint
from operator import itemgetter

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6),
}

print('Valores adicionados:')
for jogador, valor in jogo.items():
    print(f'{jogador} tirou {valor} no dado.')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('\nRanking:')
for posicao, (jogador, valor) in enumerate(ranking, start=1):
    print(f'{posicao}º lugar: {jogador} com {valor}')