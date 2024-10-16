nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
promedio = (nota1 + nota2 + nota3)/3

if promedio >= 4:
    situacion = 'Alumno aprueba'
else:
    situacion = 'Alumno reprueba'
print(situacion)
