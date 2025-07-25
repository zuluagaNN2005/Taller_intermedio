# Pares e impares
# Dada la lista [3, 8, 15, 22, 7, 10, 13], recórrela con un for y utiliza
# dos contadores para determinar cuántos son
# pares y cuántos impares. Muestra ambos totales.

# Pares e impares
numeros = [3, 8, 15, 22, 7, 10, 13]

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)