import matplotlib.pyplot as plt

ent = open('datos_covid.txt')
region = ['15', '01', '02', '03', '04', '05', '13', '06', '07', '16', '08', '09', '14', '10', '12' ]
datos = []
for linea in ent:
    lista = linea.rstrip('\n').split(';')
    datos.append(lista)
x = []
y = []
z = []
for elem in region:
    suma = 0
    poblacion = 0
    for lista in datos:
        if lista[1] == elem:
            suma = suma + float(lista[-2])
            poblacion = poblacion + float(lista[4])
    x.append(elem)
    y.append(suma)
    z.append(poblacion / suma)
plt.bar(x,z)
plt.show()
