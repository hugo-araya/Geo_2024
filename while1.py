cantidad = int(input('Cantidad de notas: '))
lista = []
i = 0
suma = 0
while i < cantidad:
    nota = float(input('Nota ' + str(i+1) + ': '))
    suma = suma + nota
    lista.append(nota)
    i = i + 1
promedio = suma / cantidad
print(promedio)
print(lista)

