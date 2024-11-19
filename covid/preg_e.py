import matplotlib.pyplot as plt

ent = open('datos_covid.txt')
datos = []
# Saco todos los datos del archivo
for linea in ent:
    linea = linea.rstrip('\n')
    lista = linea.split(';')
    datos.append(lista)
ent.close()
regiones = []
totales = []
region = 1
while region <= 16:
    suma = 0
    for dato in datos:
        if region == int(dato[1]):
            suma = suma + float(dato[-2])
    totales.append(suma)
    regiones.append(region)
    region = region + 1

plt.bar(regiones, totales)
plt.show()

