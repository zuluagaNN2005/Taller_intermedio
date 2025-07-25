# Múltiplos de 3
# Escribe un programa que imprima todos los múltiplos de 3 entre 1 y 100.

# si el numero es multliplo de 3 debes imprimir "fizz" en vez del numero

numeros = int(input("Hasta que numero queres contar parce?: "))

for i in range(1, numeros + 1):
    if i % 3 == 0:
        print("fizz")
    else:
        print(i)



