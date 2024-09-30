import random

lista = []
i = 0
while i < 20:
    lista.append(random.randint(1, 100))
    i = i + 1

elemento = int(input('a buscar: '))
largo = len(lista)
i = 0
while i < largo:
    if elemento == lista[i]:
        print('lo encointre')
    i = i + 1
print(lista)

