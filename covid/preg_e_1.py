import matplotlib.pyplot as plt

ent = open('datos_covid.txt')
datos = []
# Saco todos los datos del archivo
for linea in ent:
    linea = linea.rstrip('\n')
    lista = linea.split(';')
    datos.append(lista)
ent.close()
regiones = [15, 1, 2, 3, 4, 5, 13, 6, 7, 16, 8, 9, 14, 10, 11, 12]
totales = []
for region in regiones:
    suma = 0
    for dato in datos:
        if region == int(dato[1]):
            suma = suma + float(dato[-2])
    totales.append(suma)

plt.bar(regiones, totales)
plt.show()

