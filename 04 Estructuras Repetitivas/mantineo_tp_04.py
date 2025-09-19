import random
# punto 1
for i in range (101):
    print(i)
    
# punto 2
numero_usuario = int(input("Ingrese un número: "))
print(len(str(numero_usuario)))

# punto 3
primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))
resultado = 0
for i in range(primer_numero, segundo_numero + 1):
    if(i != primer_numero and i != segundo_numero):
        resultado += i
print(resultado)

# punto 4
salida = False
resultado = 0
while not salida:
    numero_usuario = int(input("Ingrese un número (0 para salir): "))
    if numero_usuario == 0:
        salida = True
    else:
        resultado += numero_usuario
print(f"El resultado es: {resultado}")

# punto 5
numeros_random = random.randint(0, 9)
intentos = 1
numero_usuario = int(input("Adivine el número entre 0 y 9: "))
while numero_usuario != numeros_random:
    intentos += 1
    numero_usuario = int(input("Incorrecto. Intente nuevamente: "))
print(f"Adivinaste el número {numeros_random} en {intentos} intentos.")

# punto 6
for i in range (100, 0, -1):
    if i % 2 == 0:
        print(i)
        
# punto 7
numero_usuario = int(input("Ingrese un número: "))
resultado = 0
for i in range (1, numero_usuario):
    resultado += i
print(resultado)

# punto 8
for i in range (100):
    numero = int(input(f"Ingrese el número {i+1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# punto 9
numeros = []
for i in range(100):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

media = sum(numeros) / 100

print(f"La media de los {cantidad} números ingresados es: {media}")

# punto 10
numero = input("Ingrese un número entero: ")

numero_invertido = list(numero)
numero_invertido.reverse()

print(f"El número invertido es: {''.join(numero_invertido)}")
