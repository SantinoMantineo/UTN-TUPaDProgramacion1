# punto 1
def hola_mundo(): 
    print("Hola Mundo!")
    
hola_mundo()

# punto 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese un nombre: ")
print(saludar_usuario(nombre))

# punto 3 
def informacion_personal(nombre, apellido, edad, residencia): 
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
    
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# punto 4
def calcular_area_circulo(radio): 
    area = 3.1416 * radio ** 2
    return area

def calcular_perimetro_circulo(radio): 
    perimetro = 2 * 3.1416 * radio
    return perimetro

radio = float(input("Ingrese el radio del círculo: "))
print("Área:", calcular_area_circulo(radio))
print("Perímetro:", calcular_perimetro_circulo(radio))

# punto 5
def segundos_a_horas(segundos): 
    horas = segundos // 3600
    return horas

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"{segundos_a_horas(segundos)} horas")

# punto 6
def tabla_multiplicar(numero): 
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
        
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# punto 7
def operaciones_basicas(num1, num2): 
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2 if num2 != 0 else "Indefinida (división por cero)"
    
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")
    return (suma, resta, multiplicacion, division)

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operaciones_basicas(num1, num2)
# punto 8
def calcular_imc(peso, altura): 
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")

# punto 9
def celcius_a_fahrenheit(celsius): 
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}°C son {fahrenheit}°F"

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print(celcius_a_fahrenheit(celsius))

# punto 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

print("Ingrese tres notas para calcular el promedio:")
a = float(input("Nota 1: "))
b = float(input("Nota 2: "))
c = float(input("Nota 3: "))
print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")