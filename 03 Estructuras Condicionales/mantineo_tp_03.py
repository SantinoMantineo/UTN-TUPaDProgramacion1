import random
from statistics import mean, median, mode

# ejercicio 1
edad = int(input("Ingresa tu edad: "))
if edad > 18:
    print("Es mayor de edad")

# ejercicio 2
nota = int(input("Ingresa tu nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# ejercicio 3
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# ejercicio 4 
edad = int(input("Ingresa tu edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else: 
    print("Adulto/a")

# ejercicio 5
password = input("Ingresa tu contraseña: ")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
# ejercicio 6
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")

# ejercicio 7
frase = input("Ingresa una frase o palabra: ")
vocales = ["a", "e", "i", "o", "u"]
if frase[-1] in vocales:
    print(f"{frase}!")
else:
    print(frase)

# ejercicio 8
nombre = input("Ingresa tu nombre: ")
print("Ingresa 1 si queres tu nombre en mayusculas")
print("Ingresa 2 si queres tu nombre en minusculas")
print("Ingresa 3 si queres tu nombre con la primera letra mayuscula")
numero = int(input("Ingresa un número (1 - 2 - 3): "))
if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print("Número no válido")
    
# ejercicio 9
magnitud = float(input("Ingresa la magnitud del terremoto: "))
if magnitud < 3.0:
    print("Muy leve (imperceptible)")
elif magnitud >= 3.0 and magnitud < 4.0:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4.0 and magnitud < 5.0:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5.0 and magnitud < 6.0:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6.0 and magnitud < 7.0:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# ejercicio 10
hemisferio = input("Ingresa el hemisferio (N/S): ").upper()
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día (1-31): "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"

else:
    estacion = "Hemisferio no valido"

print("Estas en:", estacion)
