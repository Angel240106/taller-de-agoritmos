tarifas = {
    "estados unidos": 900,
    "canada": 800,
    "europa": 950,
    "resto del mundo": 1250
}
destino = input("ingrese el destino de la llamada (estados unidos,canada,europa,resto del mundo):")

if destino not in tarifas:
    print("destino invalido, por favor vuelva a intentarlo.")

duracion = float(input("ingrese la duracion de la llamada en minutos:"))

costo = tarifas[destino] * duracion

if duracion > 15:
 costo *= 0.8

print(f"el costo total de la llamada es {costo} por {duracion} en minutos es: {costo:.2f} pesos")
