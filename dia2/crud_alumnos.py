import os
import tabulate
import time

lista_alumnos = [
    {
        'nombre':'César Mayta',
        'email':'cesar@gmail.com',
        'celular':'898989898'
    }
]
ANCHO = 50
opcion = 0
while(opcion < 5):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "CRUD DE ALUMNOS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR ALUMNO
         [2] MOSTRAR ALUMOS
         [3] ACTUALIZAR ALUMNO
         [4] ELIMINAR ALUMNO
         [5] SALIR
          """)
    print("="*ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    print(f"selecciono opción {opcion}")
    time.sleep(1)



