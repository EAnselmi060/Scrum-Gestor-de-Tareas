import os

class tarea:
    def __init__(usuario, nombre, categoria, fecha):
        usuario.nombre = nombre
        usuario.categoria = categoria
        usuario.fecha = fecha
        usuario.tarea_completada = False

def crear_tarea(tareas):

        nombre = input("Ingrese enunciado de la tarea: ")
        categoria = input("Ingrese la categoria: ")
        #fecha = input("Ingrese la fecha: ")
        while True:
            try:
                dia = int(input("Dia: "))
            except:
                print("Ingrese un numero entre 1-31")
                continue
            if(dia >= 1 and dia <= 31):
                break

        while True:
            try:
                mes = int(input("Mes: "))
            except:
                print("Ingrese un numero entre 1-12")
                continue
            if(mes >= 1 and mes <= 12):
                break

        while True:
            try:
                anio = int(input("Año: "))
            except:
                print("Ingrese un numero de 4 digitos")
                continue
            if(anio > 999):
                break

        fecha = str(dia) + "-" + str(mes) + "-" + str(anio)
        nueva_tarea = tarea(nombre, categoria, fecha)
        tareas.append(nueva_tarea)
        print("-----Tarea creada-----")
        input("Presiona Enter para continuar...")
        os.system ("cls")

def Editar_tarea(tareas): 
    if len(tareas) != 0:
        while True:
            for elemento in tareas:
                if elemento.tarea_completada == False:
                    print(f"{tareas.index(elemento)} | {elemento.nombre} | {elemento.categoria} | {elemento.fecha} | no completado") 
                else:
                    print(f"{tareas.index(elemento)} | {elemento.nombre} | {elemento.categoria} | {elemento.fecha} | completado")      
            print("1. Editar")
            print("0. Atras")
            option = input("Seleccione una opcion: ") 

            if option == "1":
                tarea_index = int(input("Ingrese el indice de la tarea a modificar: "))
                if tarea_index >= 0 and tarea_index < len(tareas):
                    tarea = tareas[tarea_index]
                    tarea.nombre = input("Ingrese enunciado de la tarea: ")
                    tarea.categoria =  input("Ingrese la categoria: ")
                    tarea.dia = int(input("Dia: "))
                    tarea.mes = int(input("Mes: "))
                    tarea.anio = int(input("Año: "))
                    tarea.fecha = str(tarea.dia) + "-" + str(tarea.mes) + "-" + str(tarea.anio)
                    print("Se ha editado correctamente")
                    input("Presiona Enter para continuar...")
                    os.system ("cls")
                else:
                    print("Tarea inexistente")
                    input("Presiona Enter para continuar...")
                    os.system ("cls")
            if option == "0":
                os.system ("cls")
                return
            if option == None or (option != "0" and option != "1"):
                print("OPCION NO VALIDA")
                input("Presiona Enter para continuar...")
                os.system ("cls")
                continue
            
    else: 
        print("Lista vacia. Agrege una nueva tarea")
        input("Presiona Enter para continuar...")
        os.system ("cls")

def eliminar(tareas):
    if len(tareas) != 0:
        while True:
            for elemento in tareas:
                if elemento.tarea_completada == False:
                    print(f"{tareas.index(elemento)} | {elemento.nombre} | {elemento.categoria} | {elemento.fecha} | no completado") 
                else:
                    print(f"{tareas.index(elemento)} | {elemento.nombre} | {elemento.categoria} | {elemento.fecha} | completado")      
            print("1. Eliminar")
            print("0. Atras")
            option = input("Seleccione una opcion: ")

            if option == "1":
                tarea_index = int(input("Ingrese el indice de la tarea a eliminar: "))
                if tarea_index >= 0 and tarea_index < len(tareas):
                    tareas.pop(tarea_index)
                    print("Se ha eliminado correctamente")
                else:
                    print("Tarea inexistente")
            if option == "0":
                os.system ("cls")
                return
            if option == None or (option != "0" and option != "1"):
                print("OPCION NO VALIDA")
                input("Presiona Enter para continuar...")
                os.system ("cls")
                continue
    else: 
        print("Lista vacia. Agrege una nueva tarea")
    input("Presiona Enter para continuar...")
    os.system ("cls")

def categoria(tareas):
    categoria = input("Ingrese la categoria: ")
    filtro = [tarea for tarea in tareas if tarea.categoria == categoria]
    if not filtro:
        print(f"no se encuentras tareas relacionadas a \"{categoria}\"")
    else:
        print(f"Tarea(s) en la categoria \"{categoria}\":")
        for item in filtro:
            print("Nombre:", item.nombre)
            print("Fecha:", item.fecha)
            print("Completeado:", "SI" if item.tarea_completada == True else "NO")
            print("--------------------------")
    input("Presiona Enter para continuar...")
    os.system ("cls")

def Tarea_completada(tareas): 
    while True:
        for elemento in tareas:
            if elemento.tarea_completada == False:
                print(f"{tareas.index(elemento)} {elemento.nombre} | no completado") 
            else:
                print(f"{tareas.index(elemento)} {elemento.nombre} | completado")      
        print("1. Marcar completado")
        print("0. Atras")
        option = input("Seleccione una opcion: ")

        if option == "1":
            tarea_index = int(input("Ingrese el indice de la tarea que desea marcar completada: "))
            if tarea_index >= 0 and tarea_index < len(tareas):
                tareas[tarea_index].tarea_completada = True
                print("¡Tu tarea fue completada!")
                input("Presiona Enter para continuar...")
                os.system ("cls")
            else:
                print("Su tarea no fue encontrada")
                input("Presiona Enter para continuar...")
                os.system ("cls")
        if option == "0":
            os.system ("cls")
            return
        if option == None or (option != "0" and option != "1"):
                print("OPCION NO VALIDA")
                input("Presiona Enter para continuar...")
                os.system ("cls")
                continue

def lista_tareas(tareas):
    while True:
        print("Lista de tareas:")
        if len(tareas) != 0:
            for elemento in tareas:
                if elemento.tarea_completada == False: 
                    print(f"{tareas.index(elemento)} | {elemento.nombre} | {elemento.categoria} | {elemento.fecha} | no completado")

                else:
                    print(f"{tareas.index(elemento)} | {elemento.nombre} | {elemento.categoria} | {elemento.fecha} | completado")

        else:
            print("Lista vacia. Agrege una nueva tarea")

        print("0. Atras")
        option = input("Seleccione una opcion: ")   
        
        if option == "0":
            os.system ("cls")
            return
        if option == None or option != "0":
                print("OPCION NO VALIDA")
                input("Presiona Enter para continuar...")
                os.system ("cls")
                continue

def verificar_completada(tareas):
    tareas_completadas = [tarea for tarea in tareas if tarea.tarea_completada]
    if not tareas_completadas:
        print("No existen tareas completadas")
        input("Presiona Enter para continuar...")
        os.system ("cls")
    else:
        print("Lista de tareas completadas: ")
        for item in tareas_completadas:
            print(f"{tareas.index(item)} | {item.nombre} | {item.categoria} | {item.fecha} ")
        input("Presiona Enter para continuar...")
        os.system ("cls")

def menu():
    tareas = []
    while True:
        print("\n--- Menú Principal ---")
        print("1. Nueva Tarea")
        print("2. Marcar Tarea completada")
        print("3. Lista de tareas")
        print("4. Editar tarea")
        print("5. Eliminar tarea")
        print("6. Filtrar por categoria")
        print("7. Visualizar tareas completadas")
        print("0. Salir")
        option = input("Seleccione una opcion: ")

        if option == "1":
            os.system ("cls")
            crear_tarea(tareas)
        elif option == "2":
            os.system ("cls")
            Tarea_completada(tareas)
        elif option == "3":
            os.system ("cls")
            lista_tareas(tareas)
        elif option == "4":
            os.system ("cls")
            Editar_tarea(tareas)
        elif option == "5":
            os.system ("cls")
            eliminar(tareas)
        elif option == "6":
            os.system ("cls")
            categoria(tareas)
        elif option == "7":
            os.system ("cls")
            verificar_completada(tareas)
        elif option == "0":
            print("Gracias por usar el gestor...")
            break
        elif option == None or option < "8":
            print("OPCION NO VALIDA")
            input("Presiona Enter para continuar...")
            os.system ("cls")
        else:
            print("Opcion no valida")

def main():
    menu()

if __name__ == "__main__":
    main()