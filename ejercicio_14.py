# Uso de break y continue
# Escribe un programa con while True que recorra números de 1 en adelante y:

# Use continue para saltar e imprimir solo los números que no sean múltiplos de 3.

# Detenga el bucle (break) cuando alcance el número 20.

# Suma hasta cero

# Uso de break y continue
numero = 1

while True:
    if numero % 3 == 0:
        numero += 1
        continue

    print(numero)

    if numero == 20:
        break

    numero += 1