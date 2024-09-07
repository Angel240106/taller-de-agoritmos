altura = float(input("altura:"))

peso = int(input("peso:"))

imc = peso / altura ** 2

print("imc")

if imc <= 18.5:
    print("bajo peso")
elif imc <= 25:
    print("peso normal")
elif imc <= 30:
    print("sobre peso")
elif imc <= 35:
    print("obesidad moderada")
elif imc <= 40:
    print("obesidad severa")
elif imc <= 50:
    print("obesidad morbida")