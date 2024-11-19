ent = open('datos_covid.txt')
datos = []
# Saco todos los datos del archivo
for linea in ent:
    linea = linea.rstrip('\n')
    lista = linea.split(';')
    datos.append(lista)
ent.close()
# Comienzo a procesar los datos
for dato in datos:
    if dato[2] == 'Talca':
        print('Casos totales Talca:', dato[-2])

