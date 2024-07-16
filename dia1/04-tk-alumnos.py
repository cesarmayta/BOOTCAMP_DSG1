from tkinter import *
from tkinter import messagebox

class AlumnoTk:

    def __init__(self,app):
        self.app = app
        self.app.title('Alumnos')
        self.app.geometry('640x480')

        frame = LabelFrame(self.app,text='Nuevo Alumno')
        frame.grid(row=0,column=0,columnspan=2,pady=10,padx=10)

        lb_nombre = Label(frame,text='Nombre : ')
        lb_nombre.grid(row=1,column=0)
        txt_nombre = Entry(frame)
        txt_nombre.grid(row=1,column=1)

        lb_email = Label(frame,text='Email : ')
        lb_email.grid(row=2,column=0)
        txt_email = Entry(frame)
        txt_email.grid(row=2,column=1)

        lb_celular = Label(frame,text='Celular : ')
        lb_celular.grid(row=3,column=0)
        txt_celular = Entry(frame)
        txt_celular.grid(row=3,column=1) 

        btn_insertar = Button(frame,text='Insertar Alumno',command=self.insertar)
        btn_insertar.grid(row=4,column=1,columnspan=2)

    def insertar(self):
        pass

if __name__ == "__main__":
    app = Tk()
    app_alumno = AlumnoTk(app)
    app.mainloop()