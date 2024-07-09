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
                self.registrar_alumno()
            elif self.opcion == 2:
                self.mostrar_alumnos()
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

    def registrar_alumno(self):
        print("=" * self.ANCHO)
        print(" " * 10 + "[1] REGISTRAR ALUMNO")
        print("=" * self.ANCHO)
        nombre = input("NOMBRE : ")
        email = input("EMAIL :")
        celular = input("CELULAR :")

        nuevo_alumno = Alumno(nombre,email,celular)
        self.dao.registrar_alumno(nuevo_alumno)

        print("=" * self.ANCHO)
        print(" " * 10 + "ALUMNO REGISTRADO CON ÉXITO")
        print("=" * self.ANCHO)

    def mostrar_alumnos(self):
        print("=" * self.ANCHO)
        print(" " * 10 + "[2] MOSTRAR ALUMNOS")
        print("=" * self.ANCHO)
        alumnos = self.dao.mostrar_alumnos()
        cabeceras = ["NOMBRE","EMAIL","CELULAR"]
        data = [[alumno.nombre,alumno.email,alumno.celular] for alumno in alumnos]
        print(tabulate.tabulate(data,headers=cabeceras,tablefmt="grid"))
        input("presione ENTER para continuar...")
