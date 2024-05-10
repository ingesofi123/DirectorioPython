# Ejercicio 2
# Autores:
# - Sofia Burbano Bastidas
# - Cristhian David Padilla Delgado 

contacto = []
todosContactos = []

def agregarContacto():
    nombre = input("Digite el nombre del contacto: ")
    apellido = input("Digite el apellido del contacto:")
    cedula = input("Digite el cedula del contacto: ")
    celular = input("Digite el celular del contacto: ")
    correo = input("Digite el correo del contacto: ")
    direccion = input("Digite el direccion del contacto: ")

    nuevo_contacto = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Cedula": cedula,
        "Celular": celular,
        "Correo": correo,
        "Direccion": direccion
    }

    contacto_resumen = {
        "Nombre": nombre,
        "Cedula": cedula
    }
    contacto.append(nuevo_contacto)
    todosContactos.append(contacto_resumen)
    print("Contacto agregado con éxito")

def listarContacto():
    if contacto:
        id = input("Digite la cedula del contacto que desea buscar: ")
        for contactoActual in contacto:
            if contactoActual["Cedula"] == id:
                print("Información del contacto:")
                print("Nombre:", contactoActual["Nombre"])
                print("Apellido:", contactoActual["Apellido"])
                print("Cédula:", contactoActual["Cedula"])
                print("Celular:", contactoActual["Celular"])
                print("Correo:", contactoActual["Correo"])
                print("Dirección:", contactoActual["Direccion"])
                break
        else:
            print("No se encontró ningún contacto con la cédula proporcionada")
    else:
        print("No hay contactos registrados :(")

def listarTodosContactos():
    if len(todosContactos) == 1:
        print("Existe ", len(todosContactos), " contacto")
        for contacto in todosContactos:
            print(contacto)
    elif len(todosContactos) > 1:
        print("Existen ", len(todosContactos), " contactos")
        for contacto in todosContactos:
            print(contacto)
    else:
        print("No hay contactos registrados")

def editarContacto():
    cedula = input("Digite la cédula del contacto que desea editar: ")
    encontrado = False
    for contactoActual in contacto:
        if contactoActual["Cedula"] == cedula:
            encontrado = True
            print("Información actual del contacto que desea editar es:")
            print("Nombre:", contactoActual["Nombre"])
            print("Apellido:", contactoActual["Apellido"])
            print("Cédula:", contactoActual["Cedula"])
            print("Celular:", contactoActual["Celular"])
            print("Correo:", contactoActual["Correo"])
            print("Dirección:", contactoActual["Direccion"])
            
            opcion_editar = input("¿Porfavor digite qué campo desea editar? (Nombre, Apellido, Celular, Correo, Dirección): ").capitalize()
            if opcion_editar in contactoActual:
                nuevo_valor = input(f"Ingrese la actualizacion que decea realizarle a {opcion_editar}: ")
                contactoActual[opcion_editar] = nuevo_valor
                print("Información del contacto actualizada exitosamente")
            else:
                print("Campo inválido.")
            break

    if not encontrado:
        print("No se encontró ningún contacto con la cédula proporcionada :( ")

def eliminarContacto():
    cedula = input("Digite la cédula del contacto que desea eliminar: ")
    for i, contactoActual in enumerate(contacto):
        if contactoActual["Cedula"] == cedula:
            del contacto[i]
            print("Contacto eliminado exitosamente.")
            # se actualiza la lista de contactos
            todosContactos.clear()
            for c in contacto:
                contacto_resumen = {
                    "Nombre": c["Nombre"],
                    "Cedula": c["Cedula"]
                }
                todosContactos.append(contacto_resumen)
            return
    print("No se encontró ningún contacto con la cédula proporcionada")

opcion = 0
while opcion != 6:
    print("*************************************")
    print("1. Agregar un contacto")
    print("2. Consultar todos los contactos")
    print("3. Consultar la información de un contacto")
    print("4. Editar información de un contacto")
    print("5. Eliminar un contacto")
    print("6. Salir")
    try:
        opcion = int(input("Digite una opcion "))
    except ValueError:
        print("*************************************")
        print("ERROR")
    print("*************************************")

    if opcion == 1:
        agregarContacto()
    elif opcion == 2:
        listarTodosContactos()
    elif opcion == 3:
        listarContacto()
    elif opcion == 4:
        editarContacto()
    elif opcion == 5:
        eliminarContacto()
    elif opcion == 6:
        print("Gracias por usar el script🥵")
    else:
        print("Digite una opcion valida porfavor")