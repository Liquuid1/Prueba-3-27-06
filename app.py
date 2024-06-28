import utilidades as ff

op = 0
alumnos = []

#Se inicia el bucle del programa
while op!=5:
    #Se imprime el menu y se ingresa y valida la opción del user
    ff.clrs()
    ff.imprimir_menu()
    op = ff.validar_opcion_numerica(1,5)

    #Se llama a la funcion correspondiente
    if op==1:
        ff.clrs()
        alumnos.append(ff.registrar_alumno())
        ff.pause()
    elif op==2:
        ff.clrs()
        ff.listar_alumnos(alumnos)
        ff.pause()
    elif op==3:
        ff.clrs()
        ff.buscar_nivel(alumnos)
        ff.pause()
    elif op==4:
        ff.clrs()
        ff.calcular_promedio(alumnos)
        ff.pause()

ff.guardar_archivo(alumnos)