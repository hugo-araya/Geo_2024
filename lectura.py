ent = open('sismos.txt')
cont = 0
linea = ent.readline()
while linea != '':
    linea = linea.rstrip('\n')
    lista = linea.split(',')
    if float(lista[4]) > 7.5:
        cont = cont + 1
    linea = ent.readline()
print('Cantidad: ', cont)


