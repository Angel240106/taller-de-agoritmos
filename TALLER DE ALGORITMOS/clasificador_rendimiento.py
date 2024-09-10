print("ingrese las cuatro notas del estudante (en escala de 1 a 5):")

nota1 = float(input("nota1:"))
nota2 = float(input("nota2:"))
nota3 = float(input("nota3:"))
nota4 = float(input("nota4:"))

costo_matricula = float(input("ingrese el costo total de la matricula:"))
promedio = (nota1 + nota2 + nota3 + nota4) / 4

if 4 <= promedio <= 5:
    clasificacion = "excelente"
    descuento = 0.20
elif 3 <= promedio <= 4:
    clasificacion = "bien"
    descuento = 0.0
else:
    clasificacion = "deficiente"
    descuento = 0.0

monto_final = costo_matricula * (1 - descuento)

print(f"promedio del estudiante: {promedio:.2f}")
print(f"clasificacion de rendimiento: {clasificacion}")
print(f"monto final a pagar por la matricula:{monto_final:.2f} pesos")

