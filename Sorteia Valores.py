from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
valor_maior = 0
valor_menor = 0

for index, valor in enumerate(tupla):
    if index == 0:
        valor_maior = tupla[index]
        valor_menor = tupla[index]

    if tupla[index] > valor_maior:
        valor_maior = tupla[index]

    if tupla[index] < valor_menor:
        valor_menor = tupla[index]

print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {valor_maior}\nO menor valor sorteado foi {valor_menor}')
