from triangulo import Triangulo
import tkinter as tk
from tkinter import ttk

datos=[]  
def calcular():
    try:
        base=float(input_base.get())
        altura=float(input_altura.get())
    except:
        label_resultado.config(text="Deben ser números")
    else:
        nuevo=Triangulo(base, altura)
        datos.append(nuevo.area())
        label_resultado.config(text=f"Resultado: {str(nuevo.area())}")
        label_calculadas.config(text=f"Áreas calculadas: {datos}")

root = tk.Tk()

root.title("Calcula área de un triángulo")
root.config(width=400, height=300)

label_base=ttk.Label(text="Escribe el valor de la base")
label_base.place(x=20,y=20)

input_base=ttk.Entry()
input_base.place(x=180,y=20)

label_altura=ttk.Label(text="Escribe el valor de la altura")
label_altura.place(x=20,y=50)

input_altura=ttk.Entry()
input_altura.place(x=180,y=50)

boton_calcular = ttk.Button(text="Calcular",command=calcular)
boton_calcular.place(x=20, y=80)

label_resultado=ttk.Label(text="Resultado: ")
label_resultado.place(x=20,y=110)

label_calculadas=ttk.Label(text="Áreas calculadas: ")
label_calculadas.place(x=20,y=140)

root.mainloop()
