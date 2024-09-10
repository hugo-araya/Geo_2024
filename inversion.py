inversion1 = float(input("Ingrese la inversión de la primera persona: "))
inversion2 = float(input("Ingrese la inversión de la segunda persona: "))
inversion3 = float(input("Ingrese la inversión de la tercera persona: "))
 
total_inversion = inversion1 + inversion2 + inversion3
 
porcentaje1 = (inversion1 / total_inversion) * 100
porcentaje2 = (inversion2 / total_inversion) * 100
porcentaje3 = (inversion3 / total_inversion) * 100
 
print("Porcentaje de la primera persona: ", porcentaje1)
print("Porcentaje de la segunda persona: ", porcentaje2)
print("Porcentaje de la tercera persona: ", porcentaje3)