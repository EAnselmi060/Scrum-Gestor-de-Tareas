
class tarea:
    def __init__(usuario, nombre, categoria, fecha):
        usuario.nombre = nombre
        usuario.categoria = categoria
        usuario.fecha = fecha
        usuario.tarea_completada = False

tareas = []

def crear_tarea():
    nombre = input("Ingrese enunciado de la tarea: ")
    categoria = input("Ingrese la categoria: ")
    #fecha = input("Ingrese la fecha: ")
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    anio = int(input("Año: "))
    fecha = str(dia) + "-" + str(mes) + "-" + str(anio)
    nueva_tarea = tarea(nombre, categoria, fecha)
    tareas.append(nueva_tarea)
    print("-----Tarea creada-----")

def Tarea_completada(): 
    while True:
        for elemento in tareas:
            if elemento.tarea_completada == False:
                print(f"{tareas.index(elemento)} {elemento.nombre} | no completado") 
            else:
                print(f"{tareas.index(elemento)} {elemento.nombre} | completado")      
        print("1. Marcar completado")
        print("0. Atras")
        option = int(input("Seleccione una opcion: ")) 

        if option == 1:
            tarea_index = int(input("Ingrese el indice de la tarea que desea marcar completada: "))
            if tarea_index >= 0 and tarea_index < len(tareas):
                tareas[tarea_index].tarea_completada = True
                print("¡Tu tarea fue completada!")
            else:
                print("Su tarea no fue encontrada")
        if option == 0:
            return


def lista_tareas():
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
        option = int(input("Seleccione una opcion: "))    
        if option == 0:
            return

def menu():
    while True:
        print("Menu:")
        print("1. Nueva Tarea")
        print("2. Marcar Tarea completada")
        print("3. Lista de tareas")
        print("0. Salir")
        option = int(input("Select an option: "))

        if option == 1:
            crear_tarea()
        elif option == 2:
            Tarea_completada()
        elif option == 3:
            lista_tareas()
        elif option == 0:
            print("Gracias por usar el gestor...")
            break
        else:
            print("Opcion no valida")

def main():
    menu()

if __name__ == "__main__":
    main()

