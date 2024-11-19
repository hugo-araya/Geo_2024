ent = open('datos_covid.txt')
datos = []
# Saco todos los datos del archivo
for linea in ent:
    linea = linea.rstrip('\n')
    lista = linea.split(';')
    datos.append(lista)
ent.close()

habitantes = 0

# Comienzo el proceso de busqueda
for dato in datos:
    habitantes = habitantes + float(dato[4])

print('La cantidad de habitantes registrados es:', habitantes)