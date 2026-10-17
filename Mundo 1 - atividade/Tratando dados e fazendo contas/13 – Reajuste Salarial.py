salario = float(input('Qual o salário do funcionario?'))
aumento = salario * 0.15
salario_final = salario + aumento

print(f'O salario final do funcionário com aumento de 15% é: R${salario_final:.2f}')

 
#{}: marcador de posição utilizado para inserir valores em uma string formatada.
#format(): método de formatação de string que permite substituir os marcadores de posição por valores específicos. Exemplo: 'O salário final do funcionário com aumento de 15% é: R${:.2f}'.format(salario_final) onde {:.2f} formata o valor de salario_final para ter duas casas decimais.        