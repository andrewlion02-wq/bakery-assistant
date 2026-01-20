# ejercicio 1 ( normalización de entradas del usuario )

nombre = input("cual es tu nombre?: ").strip().lower()
edad = int(input("cual es tu edad?: ").strip())
ciudad = input("cual es tu ciudad?: ").strip().lower()

print(f"Hola, soy {nombre.title()}, tengo {edad} años y vivo en {ciudad.title()}")

# ejercicio 2 ( operaciones aritméticas básicas )

valor_1 = int(input("ingresa el valor 1:"))
valor_2 = int(input("ingresa el valor 2:"))

resultado1 = valor_1 + valor_2
resultado2 = valor_1 - valor_2
resultado3 = valor_1 * valor_2
resultado4 = valor_1 / valor_2

# ejercicio 3 ( validación de mayoría de edad )

edad = int(input("ingresa tu edad: "))

if edad >= 18:
    print("acceso permitido")
else:
    print("acceso denegado")

# ejercicio 4 ( clasificación de un número según su signo )

numero = int(input("ingresa un numero positivo o negativo:"))  

if numero > 0:
    print(" es positivo")
elif numero < 0:
    print("es negativo")
else:
    print("es cero")

