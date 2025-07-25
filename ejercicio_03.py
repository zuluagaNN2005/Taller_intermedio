# Contador de vocales
# Solicita al usuario una palabra y, con un for,
# cuenta cuántas vocales (a, e, i, o, u) contiene. Muestra el total al final.

vocales = "aeiou"

conatdor_vocales = {v: 0 for v in vocales}
palabra = input("ingrese la palabra a consultar: ")

for letra in palabra:
    letra_min = letra.lower()
    if letra in vocales:
        conatdor_vocales[letra_min] += 1

print("\ncontador de vocales: ")
for v,c in conatdor_vocales.items():
    print(f"{v}: {c}")




