import math

# ejercicio 1
print("Hola Mundo!")

# ejercicio 2
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

# ejercicio 3
nombre = input("Ingresa tu nombre: ")  
apellido = input("Ingresa tu apellido: ")   
edad = input("Ingresa tu edad: ")   
residencia = input("Ingresa tu lugar de residencia: ")      
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.") 

# ejercicio 4
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# ejercicio 5
segundos = int(input("Ingresa el tiempo en segundos: "))
horas = segundos // 3600
print(f"{segundos} segundos son {horas} horas.")

# ejercicio 6
numero = int(input("Ingresa un numero: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# numero 7
numero = int(input("Ingresa el primer número distinto de cero: "))

numero2 = int(input("Ingresa el segundo número distinto de cero: "))

print(f"{numero} + {numero2} = {numero + numero2}")
print(f"{numero} - {numero2} = {numero - numero2}")
print(f"{numero} x {numero2} = {numero * numero2}")
print(f"{numero} / {numero2} = {numero // numero2}")

# ejercicio 8
altura = int(input("Ingresa tu altura en centímetros: "))
peso = int(input("Ingresa tu peso en kilogramos: "))
altura_metros = altura / 100
print(f"Tu altura en metros es: {altura_metros}")

imc = peso / (altura_metros ** 2)
print(f"Tu índice de masa corporal es: {imc}")

# ejercicio 9 
temperatura = int(input("Ingresa la temperatura en grados Celsius: "))
print(f"La temperatura en grados Fahrenheit es: {temperatura * 9/5 + 32}")

# ejercicio 10
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los tres números es: {promedio}")