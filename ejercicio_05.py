# Promedio de lista
# Dada la lista [12, 7, 22, 5, 14, 9], utiliza un for,
# un acumulador y un contador para calcular y mostrar su promedio.

# Lista de números
numeros = [12, 7, 22, 5, 14, 9]

# Inicialización del acumulador y contador
suma = 0
contador = 0

# Recorrer la lista
for numero in numeros:
    suma += numero
    contador += 1

# Calcular el promedio
promedio = suma / contador

# Mostrar el resultado
print("El promedio es:", promedio)