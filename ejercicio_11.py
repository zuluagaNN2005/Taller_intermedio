# Suma hasta cero
# Crea un programa que lea números del usuario repetidamente con while hasta que ingrese un 0. Al finalizar,
# muestra la suma de todos los valores ingresados (excluyendo el cero).

# Suma hasta cero
suma = 0
numero = int(input("Ingresa un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingresa otro número (0 para terminar): "))

print("La suma total es:", suma)