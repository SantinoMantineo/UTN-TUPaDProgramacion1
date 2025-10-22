# punto 1
def calcular_factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

limite_factorial = int(input("Ingrese un número para calcular los factoriales hasta ese número: "))

for valor in range(1, limite_factorial + 1):
    print(f"El factorial de {valor} es: {calcular_factorial(valor)}")

# punto 2
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

max_posicion = int(input("Ingrese la posición hasta la que desea ver la serie Fibonacci: "))
serie_fibonacci = [fibonacci(i) for i in range(max_posicion)]
print("Serie Fibonacci hasta la posición", max_posicion, ":", serie_fibonacci)

# punto 3
def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)

base_numero = int(input("Ingrese la base: "))
exponente_numero = int(input("Ingrese el exponente: "))
print(f"{base_numero}^{exponente_numero} =", calcular_potencia(base_numero, exponente_numero))

# punto 4
def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)

numero_decimal = int(input("Ingrese un número decimal: "))
print("Binario:", decimal_a_binario(numero_decimal))

# punto 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra_usuario = input("Ingrese una palabra: ").lower().replace(" ", "")
print("Es palíndromo?", es_palindromo(palabra_usuario))

# punto 6
def sumar_digitos(numero):
    if numero == 0:
        return 0
    return numero % 10 + sumar_digitos(numero // 10)

numero_usuario = int(input("Ingrese un número: "))
print("Suma de dígitos:", sumar_digitos(numero_usuario))

# punto 7
def contar_bloques_total(base):
    if base == 1:
        return 1
    else:
        return base + contar_bloques_total(base - 1)

bloques_base = int(input("Ingrese el número de bloques en la base: "))
print("Total de bloques:", contar_bloques_total(bloques_base))

# punto 8
def contar_digito_numero(numero, digito_a_contar):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito_a_contar else 0) + contar_digito_numero(numero // 10, digito_a_contar)

numero_ingresado = int(input("Ingrese un número: "))
digito_usuario = int(input("Ingrese el dígito a contar: "))
print(f"El dígito {digito_usuario} aparece {contar_digito_numero(numero_ingresado, digito_usuario)} veces")
