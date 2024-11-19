ent = open('datos_covid.txt')
datos = []
# Saco todos los datos del archivo
for linea in ent:
    linea = linea.rstrip('\n')
    lista = linea.split(';')
    datos.append(lista)
ent.close()

mayor = -1
comuna = ''

# Comienzo el proceso de busqueda
for dato in datos:
    if float(dato[-1]) > mayor:
        mayor = float(dato[-1])
        comuna = dato[2]
print('La comuna de', comuna,'tiene la mayor tasa, con un valor de', mayor)