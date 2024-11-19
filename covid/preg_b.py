ent = open('datos_covid.txt')
datos = []
# Saco todos los datos del archivo
for linea in ent:
    linea = linea.rstrip('\n')
    lista = linea.split(';')
    datos.append(lista)
ent.close()

# Comienzo a procesar los datos
suma = 0
for dato in datos:
    suma = suma + float(dato[-2])

print('Casos totales pais:', suma)
