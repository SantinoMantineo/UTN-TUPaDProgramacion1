dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]

userInput = input("Ingrese fecha actual en formato dia, DD/MM: ")
dia, fecha = userInput.split(", ")
dia = dia.lower()
dd_mm = fecha.split("/")

if dia not in dias: 
    raise ValueError(f"Error: '{dia}' no es un día válido")


if len(dd_mm) != 2:
    raise ValueError("Error: la fecha debe tener formato DD/MM")

dd, mm = dd_mm

if not (dd.isdigit() and mm.isdigit()):
    raise ValueError("Error: DD y MM deben ser números")

dd = int(dd)
mm = int(mm)

if (dd > 31 or dd < 0) and (mm > 12 or mm < 0):
    raise ValueError("Error: El dia tiene que ser menor a 31 y mayor a 0 y el mes debe ser menor a 12 y mayor a 0.")

if dia == "lunes" or dia == "martes" or dia == "miercoles": 
    examenInput = input("El dia ingresado se tomaron examenes?: (Afirmativo por si, Negativo por no) ")
    examenInput = examenInput.lower()
    if examenInput == "afirmativo":
        aprobadosInput = int(input("ingrese la cantidad de alumnos aprobados: "))
        desaprobadosInput = int(input("ingrese la cantidad de alumnos desaprobados: "))
    
        total = aprobadosInput + desaprobadosInput
        porc_aprobados = (aprobadosInput / total) * 100
        print(f"El promedio de aprobados es {porc_aprobados}")
    else:
        print("No se tomaron examenes.")

if dia == "jueves": 
    asistenciaInput = float(input("Ingrese el porcentaje de asistencia en numero: "))
    if asistenciaInput > 50:
        print("asistio la mayoria")
    else:
        print("no asistio la mayoria")

if dia == "viernes":
    if (dd == 1 and (mm == 1 or mm == 7)):
        print("Comienzo de nuevo ciclo")
        alumnosInput = int(input("ingrese la catidad de alumnos del nuevo ciclo: "))
        arancelInput = float(input("ingrese el valor del arancel: "))
        totalRecaudado = alumnosInput * arancelInput
        print(f"El total recaudado por los aranceles es: ${totalRecaudado}") 
        
    