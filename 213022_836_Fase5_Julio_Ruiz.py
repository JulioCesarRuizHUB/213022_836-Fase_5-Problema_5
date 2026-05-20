# Nombre del estudiante: Julio Cesar Ruiz Herrera
# Grupo: 213022_836
# Programa: Ingeniería de sistemas
# Problema 5: Matriz registra horas laborales de empleados
Recursos = 4
Dias_laborales = 6  # columna 0 = nombre, columnas 1-5 = Lunes-Viernes

# Matriz para registrar las horas laborales de cada recurso durante la semana.
matriz_general = [[0] * Dias_laborales for _ in range(Recursos)]

# Matriz de días laborales para referencia.
matriz_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Informacion de empleados y horas trabajadas durante la semana.
matriz_general[0] = ["Ana", 8, 8, 6, 8, 8]    # 38 horas - Parcial
matriz_general[1] = ["Luis", 8, 8, 8, 8, 8]   # 40 horas - Completa
matriz_general[2] = ["Maria", 8, 8, 8, 8, 9]  # 41 horas - Sobretiempo
matriz_general[3] = ["Carlos", 7, 8, 8, 8, 6] # 37 horas - Parcial

# funcion para sumar horas laborales de un empleado seleccionado.
def suma_horas_laborales(opcion):
    total = sum(matriz_general[opcion-1][1:6])
    return total

# funcion para clasificar la jornada laboral de un empleado dependiendo del total de horas trabajadas.
def clasificacion_jornada(total):
    if total > 40:
        clasificacion = "Parcial"
    elif total == 40:
       clasificacion = "Completa"
    else:
        clasificacion = "Sobretiempo"

    return clasificacion

# funcion del menu principal
def menu_principal():
    while_control = 1
    while while_control == 1:
        print("----------  Matriz de horas laborales  ----------")
        print("Empleados registrados:")
        for i in range(Recursos):
            print(f"{i+1}. {matriz_general[i][0]}")
        print("5. Salir")

        try:
            opcion = int(input("¿Cual empleado desea consultar? "))
        except ValueError:
            print("Opción no válida.")
            continue

        if opcion == 5:
            break
        if 1 <= opcion <= Recursos:
            total = suma_horas_laborales(opcion)
            clasificacion = clasificacion_jornada(total)
            nombre = matriz_general[opcion-1][0]        
            
            print(f"---------- RESUMEN DEL EMPLEADO ----------")
            print(f"Nombre: {nombre}")
            print(f"Total de horas laboradas: {total}")
            print(f"clasificacion de jornada: {clasificacion}")
            print("-------------------------------------------")
        else:
            print("Opción no válida.")


        while True:
             print ('¿Desea continuar?')
             print("Si (1)")
             print("No (0)")
             control_while = int(input("Respuesta: "))
             if control_while == 1:
                while_control = 1
                break
             elif control_while == 0:
                while_control = 0
                break
             else:
                print('Respuesta incorrecta')

if __name__ == "__main__":
    menu_principal()
