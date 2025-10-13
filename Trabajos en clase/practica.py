especialidades = []
cupos = []

salir = False

while not salir:
    print("Menu:")
    print("1. Ingresar especialidades")
    print("2. Ingresar cupos por especialidad")
    print("3. Mostrar agenda")
    print("4. Consultar cupos disponibles") 
    print("5. Listar especialidades sin cupos")
    print("6. Agregar especialidad")
    print("7. Actualizar cupos (reservar/cancelar)")
    print("8. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if(opcion == "1"):
        while True: 
            especialidad = input("Ingrese la especialidad: ")
            if especialidad.strip() == "" or not especialidad.isalpha():
                print("La especialidad no puede estar vacía y debe contener solo letras.")
            elif especialidad in especialidades:
                print("Esa especialidad ya existe en la agenda.")
            else:
                especialidades.append(especialidad.title())
                cupos.append(0)
                break
    elif opcion == "2":
        if not especialidades:
            print("No hay especialidades, agrega alguna para continuar.")
        else:
            for i in range(len(especialidades)):
                while True:
                    cupo = input(f"Ingrese la cantidad de cupos para {especialidades[i]}: ")
                    if cupo.strip() == "" or not cupo.isdigit():
                        print("El cupo no puede estar vacío y debe contener solo números.")
                    else:
                        cupos[i] = int(cupo)
                        break

    elif opcion == "3":
        if not especialidades: 
            print("No hay especialidades, agrega alguna para continuar.")
        else: 
            for i in range(len(especialidades)):
                print(f"{especialidades[i]}: {cupos[i]} cupos")
    elif opcion == "4":
        if not especialidades:
            print("No hay especialidades, agrega alguna para continuar.")
        else:
            while True:
                consulta = input("Ingrese la especialidad a consultar: ").title()
                if consulta.strip() == "" or not consulta.isalpha():
                    print("La especialidad no puede estar vacia y debe contener solo letras")
                elif consulta not in especialidades:
                    print("No existe la especialidad")
                else:
                    especialidad = especialidades.index(consulta)
                    print(f"La especialidad {especialidades[especialidad]} tiene {cupos[especialidad]}")
    elif opcion == "5":
        if not especialidades:
            print("No hay especialidades, agrega alguna para continuar.")
        else:
            for i in range(len(especialidades)):
                if cupos[i] == 0:
                    print(f"{especialidades[i]} tiene {cupos[i]}")