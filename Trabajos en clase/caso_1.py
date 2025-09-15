titulos = []
ejemplares = []

salir = False

while not salir:
    print("MENÚ")
    print("1. Ingresar lista de títulos")
    print("2. Ingresar lista de ejemplares")
    print("3. Mostrar catálogo con stock")
    print("4. Consultar disponibilidad de un título")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Ver catálogo (sólo títulos)")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        titulo = input("Ingrese el título (o 0 para terminar): ")
        while titulo != "0":
            if titulo.strip() == "":
                print("El título no puede estar vacío.")
            elif titulo in titulos:
                print("Ese título ya existe en el catálogo.")
            else:
                titulos.append(titulo)
                ejemplares.append(0)
            titulo = input("Ingrese otro título (o 0 para terminar): ")

    elif opcion == "2":
        if not titulos:
            print("No hay títulos cargados aún.")
        else:
            for i in range(len(titulos)):
                valido = False
                while not valido:
                    try:
                        cant = int(input(f"Ingrese la cantidad de ejemplares para '{titulos[i]}': "))
                        if cant < 0:
                            print("No puede ingresar un número negativo.")
                        else:
                            ejemplares[i] = cant
                            valido = True
                    except ValueError:
                        print("Debe ingresar un número entero.")

    elif opcion == "3":
        if not titulos:
            print("No hay catálogo cargado.")
        else:
            print("Catálogo con stock:")
            for i in range(len(titulos)):
                print(f"{titulos[i]}: {ejemplares[i]} copias")

    elif opcion == "4":
        buscar = input("Ingrese el título a consultar: ")
        if buscar in titulos:
            indice = titulos.index(buscar)
            print(f"'{buscar}' tiene {ejemplares[indice]} copias disponibles.")
        else:
            print(f"El título '{buscar}' no existe en el catálogo.")

    elif opcion == "5":
        print("Libros agotados:")
        agotados = False
        for i in range(len(titulos)):
            if ejemplares[i] == 0:
                print(f"'{titulos[i]}' no tiene copias disponibles.")
                agotados = True
        if not agotados:
            print("No hay títulos agotados.")

    elif opcion == "6":
        nuevo = input("Ingrese el nuevo título: ")
        if nuevo.strip() == "":
            print("El título no puede estar vacío.")
        elif nuevo in titulos:
            print("Ese título ya está en el catálogo.")
        else:
            valido = False
            while not valido:
                try:
                    cant = int(input(f"Ingrese la cantidad de ejemplares para '{nuevo}': "))
                    if cant < 0:
                        print("No puede ingresar un número negativo.")
                    else:
                        titulos.append(nuevo)
                        ejemplares.append(cant)
                        valido = True
                except ValueError:
                    print("Debe ingresar un número entero.")

    elif opcion == "7":
        accion = input("Ingrese 'p' para préstamo, 'd' para devolución: ").lower()
        titulo_accion = input("Ingrese el título: ")

        if titulo_accion in titulos:
            indice = titulos.index(titulo_accion)
            try:
                cant = int(input("Ingrese la cantidad: "))
                if cant <= 0:
                    print("La cantidad debe ser mayor a 0.")
                else:
                    if accion == "p":
                        if cant <= ejemplares[indice]:
                            ejemplares[indice] -= cant
                            print(f"Se prestaron {cant} ejemplares de '{titulo_accion}'. Quedan {ejemplares[indice]}.")
                        else:
                            print("No hay suficientes ejemplares disponibles.")
                    elif accion == "d":
                        ejemplares[indice] += cant
                        print(f"Se devolvieron {cant} ejemplares de '{titulo_accion}'. Ahora hay {ejemplares[indice]}.")
                    else:
                        print("Opción inválida.")
            except ValueError:
                print("Debe ingresar un número entero.")
        else:
            print(f"El título '{titulo_accion}' no está en el catálogo.")

    elif opcion == "8":
        if not titulos:
            print("No hay títulos en el catálogo.")
        else:
            print("Catálogo de títulos:")
            for t in titulos:
                print(f"- {t}")

    elif opcion == "0":
        salir = True
        print("Saliendo del sistema")

    else:
        print("Opción inválida. Intente de nuevo.")
