from random import choice 
aluno1 = str(input('primerio aluno:')) 
aluno2  = str(input('segundo aluno:'))
aluno3 = str(input('terceiro aluno:'))
aluno4 = str(input('quarto aluno:'))

lista = [aluno1 ,  aluno2 ,  aluno3 ,  aluno4]
escolhido = choice(lista)

print(f'o aluno escolhido foi:{escolhido}') 

#str - trasforma valores em texto