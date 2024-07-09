import os
import time
import tabulate
from DAO.alumno_dao import AlumnoDAO
from Models.alumno_models import Alumno

class AlumnoViews:
    ANCHO = 50

    def __init__(self):
        self.dao = AlumnoDAO()
        self.opcion = 0

    def menu(self):
        while self.opcion != 5:
            os.system("clear")
            print("=" * self.ANCHO)
            print(" " * 10 + "PROGRAMA DE MATRICULA DE ALUMNOS")
            print("=" * self.ANCHO)
            print("""
                  [1] REGISTRAR ALUMNO
                  [2] MOSTRAR ALUMNOS
                  [3] ACTUALIZAR ALUMNO
                  [4] ELIMINAR ALUMNO
                  [5] SALIR
                  """)
            print("=" * self.ANCHO)

            self.opcion = int(input("INGRESE UNA OPCIÓN DEL MENU: "))

            os.system("clear")
            if self.opcion == 1:
                pass
            elif self.opcion == 2:
                pass
            elif self.opcion == 3:
                pass
            elif self.opcion == 4:
                pass
            elif self.opcion == 5:
                print("=" * self.ANCHO)
                print(" " * 10 + "SALIENDO DEL SISTEMA....")
                print("=" * self.ANCHO)
            else:
                print("=" * self.ANCHO)
                print(" " * 10 + "OPCIÓN INVÁLIDA!!!!")
                print("=" * self.ANCHO)

            time.sleep(1)

