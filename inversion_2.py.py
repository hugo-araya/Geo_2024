cap_inv = int(input('Capital a invertir: '))
interes = float(input('Interes: '))

ganancia = cap_inv * interes /100

if ganancia > 7000:
    cap_inv = cap_inv + ganancia
print('Saldo: ', cap_inv)
