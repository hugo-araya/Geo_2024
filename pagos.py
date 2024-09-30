gasto = int(input('Diga su gasto: '))
if gasto <= 100:
    print('pagar_en_efectivo')
elif gasto > 100 and gasto < 300:
    print('pagar_con_debito')
else:
    print('pagar_con_credito')
    