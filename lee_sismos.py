import matplotlib.pyplot as plt
ent = open('sismos.txt')
dato = 1570
x = []
y = []
while dato < 2024:
    cont = 0
    ent = open('sismos.txt')
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split(',')
        fecha = lista[0]
        lista = fecha.split('-')
        agno = lista[2]
        if agno == str(dato):
            cont = cont + 1
    if cont !=0:
        x.append(dato)
        y.append(cont)
    dato = dato + 1
    ent.close()
plt.bar(x, y)
plt.show()
