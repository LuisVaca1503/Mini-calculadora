import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import PIL
from PIL import Image, ImageTk
def geometria():
    # Caracteristicas ventana principal
    ven_geometria = Toplevel()
    ven_geometria.title("Geometria")
    ven_geometria.resizable(0, 0)

    # Definicion del notebook
    control_subventanas = ttk.Notebook(ven_geometria)
    # Configuracion primera ventana
    subven_1 = Frame(control_subventanas)
    subven_1.config(width="300", height="400", bg="Grey")
    subven_1.pack(fill='y', expand=0)
    #Fondo ventana 1
    fondo = Image.open('formulas.png')
    fondo = fondo.resize((300, 400), Image.ANTIALIAS)
    fondo = ImageTk.PhotoImage(fondo)
    subven_1_label = Label(subven_1, image=fondo)
    subven_1_label.place(x=0, y=0)
    subven_1.config(width="300", height="400", bg="Grey")
    #Configuracion 2nda ventana:
    subven_2 = Frame(control_subventanas)
    fondo_ven2 = Image.open('figuras geometricas.png')
    fondo_ven2 = ImageTk.PhotoImage(fondo_ven2)
    subven_2_label = Label(subven_2, image=fondo_ven2)
    subven_2_label.place(x=0, y=0)
    subven_2.config(width="300", height="300", bg="Purple")
    # Config. Barra de Scroll
    Barra_de_Scroll = Scrollbar(subven_2, orient=tk.HORIZONTAL)
    Barra_de_Scroll.pack(side="bottom", fill="x")




    control_subventanas.add(subven_1, text='Formulas')
    control_subventanas.add(subven_2, text='Formas')
    control_subventanas.pack(expand=1, fill='both')
    ven_geometria.mainloop()

def calculadora(num1, num2, operador,redondeo=0):
    resultado = ''
    if operador == '+':
        resultado = num1+num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1*num2
    elif operador == '/':
        resultado = (num1/num2)
    elif operador == "^":
        resultado = num1**num2
    elif operador == "√":
        resultado = num1 ** (1/num2)
    if redondeo == 1:
        return round(resultado,2)
    else:
        return resultado

def click_calcular(label,num1,num2,operador,redondeo):
    #Conversion de Valores
    valor1 = float(num1)
    valor2 = float(num2)

    #Calculo dados los valores
    res = calculadora(valor1,valor2,operador,redondeo)

    #Text Update
    label.configure(text = 'Resultado: '+ str(res))

def init_window():

    window = tk.Tk()
    window.title('Mi primera aplicacion')
    window.geometry('400x400')
    window.resizable(0,0)

    fondo = PhotoImage(file="fondo.png")
    fondo2 = Label(window, image=fondo).place(x=0, y=0)

    label = tk.Label(window,text='Calculadora', font= ('Bauhaus 93', 20))
    label.place(x=105,y=10)

    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)

    entrada1.place(x=250,y=50)
    entrada2.place(x=250,y=100)

    label_entrada1 = tk.Label(window, text = 'Ingrese primer numero', font = ('Rockwell',13))
    label_entrada1.place(x=10,y=50)

    label_entrada2 = tk.Label(window, text='Ingrese segundo numero', font=('Rockwell', 13))
    label_entrada2.place(x=10,y=100)

    #Crear una etiqueda del combobox
    label_operador = tk.Label(window,text = 'Escoja un operador', font = ('Rockwell', 13))
    label_operador.place(x=10,y=150)

    #Crear un seleccionador
    combo_operadores = ttk.Combobox(window)
    #Asignar los valores
    combo_operadores['values'] = ['+','-','*','/','^','√']
    #Asigna opcion por defecto
    combo_operadores.current(0)
    combo_operadores.place(x=200,y=150)

    #agregar etiqueta para mostrar el resultado
    label_resultado = tk.Label(window, text = 'Resultado: ', font = ('Rockwell', 15))
    label_resultado.place(x=50,y=300)

    #Boton redondear
    seleccion = IntVar()
    redondeo = Radiobutton(window,text = 'Redondear',value = 1, variable = seleccion)
    redondeo.place(x=210,y= 190)
    Noredondeo = Radiobutton(window, text=' No Redondear', value=2, variable = seleccion)
    Noredondeo.place(x=90, y=190)

    #Botn calcular
    boton = tk.Button(window,
                      command = lambda: click_calcular(
                                label_resultado,
                                entrada1.get(),
                                entrada2.get(),
                                combo_operadores.get(),
                                seleccion.get()),
                      text = 'Calcular',
                      bg = "DeepSkyblue2",
                      fg = "gray1")
    boton.place(x=170,y=250)

    #Boton geometria
    fondo_boton6 = Image.open('Logo_geometria.png')
    fondo_boton6 = fondo_boton6.resize((70, 70), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
    fondo_boton6 = ImageTk.PhotoImage(fondo_boton6)
    boton6 = tk.Button(window, text = 'Geometria!',image=fondo_boton6, bg='white',fg = "DeepSkyblue4" ,compound = 'top',
                       command = lambda: geometria())
    boton6.place(x=300, y=280)

    window.mainloop()

def main():
    init_window()
main()