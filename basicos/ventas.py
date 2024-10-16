# Autor: Hugo Araya Carrasco


sueldo_base = int(input('Sueldo base: '))
venta1 = int(input('Venta 1: '))
venta2 = int(input('Venta 2: '))
venta3 = int(input('Venta 3: '))
# Aqui estoy sumando las ventas
ventas = venta1 + venta2 + venta3
comision = ventas * 0.10
sueldo_recibir = sueldo_base + comision
print('Comision: ', comision)
print('Sueldo a recibir: ', sueldo_recibir)
