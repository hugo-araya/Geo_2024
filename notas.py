
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota_examen = float(input('Nota examen: '))
nota_trab = float(input('Nota trabajo: '))
promedio = (nota1 + nota2 + nota3)/3
nota_final = promedio * 0.55 + nota_examen * 0.3 + nota_trab * 0.15
print('Nota final es: ', nota_final)
