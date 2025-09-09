import random 

numeros = random.sample(range(1, 51), 25)

carton = []
indice = 0
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(numeros[indice])
        indice += 1
    carton.append(fila)

numeros_random = list(random.sample(range(1, 51), 50))
random.shuffle(numeros_random)

for i in range (50):
    print(f'Numero sacado: {numeros_random[i]}')
    for fila in carton:
        if numeros_random[i] in fila:
            fila[fila.index(numeros_random[i])] = 0
    
def mostrar_carton(carton):
    for fila in carton:
        print(' '.join(f'{num:2}' for num in fila))
    print("\n")


mostrar_carton(carton)

numeros_random = list(range(1, 51))
random.shuffle(numeros_random)

for num in numeros_random:
    print(f"Número sacado: {num}")
    encontrado = False

    for fila in carton:
        if num in fila:
            fila[fila.index(num)] = 0
            encontrado = True

    if not encontrado:
        print("El número no está en el cartón.")

    mostrar_carton(carton)

    for fila in carton:
        if all(n == 0 for n in fila):
            print("linea")

    if all(all(n == 0 for n in fila) for fila in carton):
        print("BINGO")
        break
