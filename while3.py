import random

numero = random.randint(1, 100)
contador = 0
while True:
    elemento = int(input('Numero: '))
    contador = contador + 1
    if elemento == numero:
        print('Lo adivine en '+ str(contador)+' intentos')
    else:
        print('Intenta de nuevo')
        if numero > elemento:
            print('Sube')
        else:
            print('Baja')
