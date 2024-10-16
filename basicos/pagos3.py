gasto = int(input('Diga su gasto: '))
if gasto <= 100:
    print('pagar_en_efectivo')

if gasto > 100 and gasto < 300:
    print('pagar_con_debito')

if gasto > 300:
    print('pagar_con_credito')