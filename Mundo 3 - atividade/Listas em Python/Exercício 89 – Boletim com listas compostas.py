Boletim = []

while True:
    nome = input('Seu nome? ').strip().capitalize()
    if not nome or not nome.replace(' ', '').isalpha():
        print('Nome inválido. Digite apenas letras.')
        continue

    while True:
        try:
            nota1 = float(input('Digite a primeira nota: ').replace(',', '.'))
            nota2 = float(input('Digite a segunda nota: ').replace(',', '.'))
            break
        except ValueError:
            print('Digite apenas números válidos.')

    media = (nota1 + nota2) / 2

    if media < 5.0:
        print('\033[1;31mREPROVADO.\033[m')
    elif media >= 7.0:
        print('\033[1;32mAPROVADO.\033[m')
    else:
        print('\033[1;33mRECUPERAÇÃO!\033[m')

    Boletim.append([nome, [nota1, nota2], media])

    continuar = ' '
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    
print('\033[1;32m--- BOLETIM ---\033[m')
for aluno in Boletim:
    print(f'{aluno[0]}: média {aluno[2]:.1f}')

nome_busca = input('Mostrar as notas de qual aluno? ').strip()
for aluno in Boletim:
    if aluno[0].lower() == nome_busca.lower():
        print(f'Notas de {aluno[0]} são: {aluno[1][0]} e {aluno[1][1]}.')
        break
else:
    print(f'Aluno "{nome_busca}" não encontrado.')
    