examen_mat = float(input('Examen Matematica: '))
nota1_mat = float(input('Nota 1 mat: '))
nota2_mat = float(input('Nota 2 mat: '))
nota3_mat = float(input('Nota 3 mat: '))
promedio_mat = (nota1_mat + nota2_mat + nota3_mat)/3
nota_mat = promedio_mat * 0.1 + examen_mat * 0.9

examen_fis = float(input('Examen Fisica: '))
nota1_fis = float(input('Nota 1 fis: '))
nota2_fis = float(input('Nota 2 fis: '))
promedio_fis = (nota1_fis + nota2_fis)/2
nota_fis = promedio_fis * 0.2 + examen_mat * 0.8

examen_pro = float(input('Examen Programacion: '))
nota1_pro = float(input('Nota 1 pro: '))
nota2_pro = float(input('Nota 2 pro: '))
nota3_pro = float(input('Nota 3 pro: '))
promedio_pro = (nota1_pro + nota2_pro + nota3_pro)/3
nota_pro = promedio_pro * 0.15 + examen_pro * 0.85

final = (nota_mat + nota_fis + nota_pro)/3
print('Promedio final: ', final)

