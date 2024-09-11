'''Hacer un algoritmo que calcule el total a pagar por la compra de camisas. 
Si se compran tres camisas o más se aplica un descuento del 20% sobre el total 
de la compra y si son menos de tres camisas un descuento del 10%
'''
monto = int(input("monto "))
compra = int(input("cantidad de prendas "))
 
if compra >3:
   desc = monto * 0.2
else:
   desc = monto * 0.1
total = monto - desc
print("monto a pagar " , total )