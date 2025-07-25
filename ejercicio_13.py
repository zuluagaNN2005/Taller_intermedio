# Menú repetitivo
# Desarrolla un menú en bucle while con estas opciones:

# Sumar dos números

# Restar dos números

# Multiplicar dos números

# Salir
# Elige la opción, pide los operandos, muestra el resultado y vuelve a mostrar
# el menú hasta que seleccione “Salir”.

# Menú repetitivo
while True:
    print("\n--- MENÚ ---")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "4":
        print("¡Hasta luego!")
        break

    if opcion in ("1", "2", "3"):
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            resultado = num1 + num2
            print("Resultado:", resultado)
        elif opcion == "2":
            resultado = num1 - num2
            print("Resultado:", resultado)
        elif opcion == "3":
            resultado = num1 * num2
            print("Resultado:", resultado)
    else:
        print("Opción no válida. Intenta de nuevo.")
