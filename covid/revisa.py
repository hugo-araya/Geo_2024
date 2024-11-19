ent = open('datos_covid.txt')
i = 0
datos = []
flag = 242
for linea in ent:
    lista = linea.rstrip('\n').split(';')
    if len(lista) != flag:
        datos.append([i, len(lista)])
    i = i + 1
ent.close()
print(datos)

