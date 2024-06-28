from os import system
import random
import math

#Limpia la pantalla
def clrs():
    system("cls")

#Pausa el programa hasta que el usuario aprete un boton
def pause():
    system("pause")

#Imprime el menu en pantalla
def imprimir_menu():
    menu = """                 SELECCIONA
[1] Registrar alumno.
[2] Listar Todos los alumnos
[3] Buscar alumnos por nivel
[4] Calcular nota promedio de los alumnos
[5] Salir del programa y guardar
--> """
    print(menu,end="")

#Valida las opciones numericas, requiere que se ingrese el rango para validar la opcion
def validar_opcion_numerica(menor,mayor):
    while True:
        try:
            op = int(input())
            if op>=menor and op<=mayor:
                return op
            else:
                raise ValueError
        except:
            print("Selecciona un número valido --> ",end="")

#Genera y retorna una lista de 5 notas elegidas aleatoriamente entre 1 y 10
def generar_notas(notas):
    for i in range(5):
        notas.append(random.randrange(1,10))
    return notas

#Pide al usuario los datos del alumno y los registra en un diccionario, luego retorna ese diccionario.
def registrar_alumno():
    notas=[]
    msg_edad = "Ingresa la edad: "
    msg_nivel = "Ingresa el nivel: "
    nom = input("Ingresa el nombre: ")
    ape = input("Ingresa el apellido: ")
    print("Ingresa la edad (Entre 1 y 100): ",end="")
    edad = validar_opcion_numerica(1,100)
    print("Ingresa el nivel (Entre 1 y 12): ",end="")
    nivel = validar_opcion_numerica(1,12)
    generar_notas(notas)
    print("Notas del alumno: ",notas[0],notas[1],notas[2],notas[3],notas[4])

    alumno = {"nom":nom,"ape":ape,"edad":edad,"nivel":nivel,"notas":notas}
    return (alumno)

#Muestra todos los alumnos en la lista
def listar_alumnos(lista):
    cont = 1
    for i in lista:
        print(f"Alumno {cont}")
        print(i["nom"],i["ape"],"Edad:",i["edad"],"Nivel:",i["nivel"])
        print(f"Notas: [{i["notas"][0]}] [{i["notas"][1]}] [{i["notas"][2]}] [{i["notas"][3]}] [{i["notas"][4]}]")
        print("*********************************************")
        cont += 1

#Muestra todos los usuarios de un mismo nivel
def buscar_nivel(lista):
    print("Ingresa el nivel que quieres buscar: ",end="")
    nivel = validar_opcion_numerica(1,12)
    for i in lista:
        if nivel==i["nivel"]:
            print("*********************************************")        
            print(i["nom"],i["ape"],"Edad:",i["edad"],"Nivel:",i["nivel"])
            print(f"Notas: [{i["notas"][0]}] [{i["notas"][1]}] [{i["notas"][2]}] [{i["notas"][3]}] [{i["notas"][4]}]")
            print("*********************************************")

#Calcula el promedio de todos los estudiantes
def calcular_promedio(lista):
    cont = 1
    for i in lista:
        suma_notas = math.fsum(i["notas"])
        promedio = suma_notas/5
        print(f"Alumno {cont}")
        print(i["nom"],i["ape"],"Edad:",i["edad"],"Nivel:",i["nivel"])
        print(f"Notas: [{i["notas"][0]}] [{i["notas"][1]}] [{i["notas"][2]}] [{i["notas"][3]}] [{i["notas"][4]}], PROMEDIO: {promedio}")
        print("*********************************************")
        cont += 1    

#Guarda los datos de la lista en un archivo
def guardar_archivo(lista):
    with open("alumnos.txt",'w') as archivo:
        for i in lista:
            escritor = i["nom"]+" "+i["ape"]+" "+"Edad:"+" "+str(i["edad"])+", "+"Nivel:"+" "+str(i["nivel"])+", "+f"Notas: [{i["notas"][0]}] [{i["notas"][1]}] [{i["notas"][2]}] [{i["notas"][3]}] [{i["notas"][4]}]"+"\n"
            archivo.write(escritor)