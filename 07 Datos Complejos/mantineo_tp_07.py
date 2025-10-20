# punto 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Precio de la Banana:", precios_frutas)

# punto 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# punto 3

lista_frutas = list(precios_frutas.keys())

# punto 4

contactos = {}

def agregar_contacto(nombre, numero):
    contactos[nombre] = numero
    
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número telefónico de {nombre}: ")
    agregar_contacto(nombre, numero)

nombre_buscar = input("Ingresá el nombre del contacto: ")

if nombre_buscar in contactos:
    print(f"El número de {nombre_buscar} es: {contactos[nombre_buscar]}")
else:
    print("El contacto no existe")

# punto 5

frase = input("Ingrese una frase: ")
palabras = frase.split(" ")
palabras_unicas = set(palabras)
print("Palabras unicas en la frase:", palabras_unicas)

recuento = {}

for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
    
print("Recuento de palabras:", recuento)

# punto 6
alumnos = {}

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = (
        float(input("Ingrese la primera nota: ")),
        float(input("Ingrese la segunda nota: ")),
        float(input("Ingrese la tercera nota: "))
    )
    alumnos[nombre] = notas 

print("Promedio de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
    
# punto 7

parcial_1 = {"Santino", "Bruno", "Camila", "Valentina"}
parcial_2 = {"Bruno", "Camila", "Valentina", "Diego"}
aprobados_ambos = parcial_1 & parcial_2
solo_uno = parcial_1 ^ parcial_2 

al_menos_uno = parcial_1 | parcial_2  

print("Aprobaron ambos parciales:", aprobados_ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

# punto 8

diccionario = {
    "Colgate": 200,
    "Pepsi": 150,
    "Arroz": 100,
}

producto = input("Ingrese el nombre del producto: ")
consulta = input("De que producto quiere saber el stock?: ")
if consulta in diccionario:
    print(f"El stock de {consulta} es: {diccionario[consulta]}")
    respuesta = input("Deseas cambiar el stock? (si/no)")
    if respuesta.lower() == "si":
        nuevo_stock = int(input("Ingrese el nuevo stock: "))
        diccionario[consulta] = nuevo_stock
        print(f"El stock de {consulta} ha sido actualizado a: {diccionario[consulta]}")
else:
    print("El producto no está en el diccionario")

producto_nuevo = input("Deseas agregar un nuevo producto? (si/no)")
if producto_nuevo.lower() == "si":
    nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
    nuevo_stock = int(input("Ingrese el stock del nuevo producto: "))
    diccionario[nuevo_producto] = nuevo_stock
    print(f"El producto {nuevo_producto} ha sido agregado con un stock de: {nuevo_stock}")
    
    
# punto 9

agenda = {}

agenda[("Lunes", "10:00")] = "Programación 1"
agenda[("Martes", "14:00")] = "Matemática"
agenda[("Miércoles", "09:00")] = "Inglés Técnico"
agenda[("Jueves", "16:00")] = "Laboratorio de Computación"
agenda[("Viernes", "11:00")] = "Sistemas de Información"

print("AGENDA COMPLETA:\n")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

print("\nConsulta de actividad:\n")
dia_consulta = input("Ingrese el día: ").capitalize()
hora_consulta = input("Ingrese la hora (formato HH:MM): ")

evento = agenda.get((dia_consulta, hora_consulta))

if evento:
    print(f"\nEl {dia_consulta} a las {hora_consulta} hay: {evento}")
else:
    print(f"\nNo hay ninguna actividad el {dia_consulta} a las {hora_consulta}.")
    
# punto 10
capitales = {
    "Buenos Aires": "Argentina",
    "Madrid": "España",
    "París": "Francia",
    "Lisboa": "Portugal",
    "Londres": "Reino Unido"
}

capitales_invertidas = {pais: ciudad for ciudad, pais in capitales.items()}