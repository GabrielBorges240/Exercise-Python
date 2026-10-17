person = {'Nome': 'Wanda', 'Sexo': 'F', 'Idade': '32'}
person['Idade'] = '34'
for k, v in person.items():
    print(f'{k} - {v}')

Brasil = []
Estado1 = {'Uf': 'Rondônia', 'Sigla': 'RO'}
Estado2 = {'Uf': 'São Paulo', 'Sigla': 'SP'}
Brasil.append(Estado1)
Brasil.append(Estado2)
print(Brasil[1]['Sigla'])

Brasil = []
for i in range(3):
    estado = {}
    estado['Uf'] = str(input('Unidade Federativa: '))
    estado['UF'] = str(input('Sigla do Estado: '))
    Brasil.append(estado.copy())
for c in Brasil:
    for k, v in c.items():
        print(f'O campo {k} tem valor {v}.')