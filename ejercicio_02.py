# Suma acumulada (primeros 100 números)
# Implementa un programa que use un bucle for y un
# acumulador para calcular la suma de los 100 primeros
# números naturales (del 1 al 100) y muestre el resultado.

# Inicializar el acumulador
suma = 0

# Bucle for para recorrer los números del 1 al 100
for i in range(1, 101):
    suma += i  # Acumular la suma

# Mostrar el resultado
print("La suma de los primeros 100 números naturales es:", suma)
