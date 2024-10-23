ent = open('sismos.txt')
cont = 0
for linea in ent:
    linea = linea.rstrip('\n')
    lista = linea.split(',')
    temblor = lista[4]
    if float(temblor) >= 8.0:
        cont = cont + 1
print(cont)