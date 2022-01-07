import tkinter as tk
from tkinter import ttk, messagebox


expression = ""

##### FUNCIONES ####


def clear():
    global expression
    expression = ""
    equation.set("0")


def press(num):
    global expression
    expression = expression + str(num)

    equation.set(expression)


# Funcion para evaluar la expresion final
def equalpress():
    try:
        global expression
        # La función eval() se utiliza para evaluar cadenas de
        # texto que pueden contener expresiones o distintos
        # tipos de estructuras de datos que pueden utilizarse con Python
        total = str(eval(expression))
        equation.set(total)
        # Cargar total en la expresión
        expression = total  # Si hay algún error
    except ZeroDivisionError:
        equation.set("0")
        expression = ""
        messagebox.showerror(title="Error", message="No se puede dividir por Cero")
    except Exception:
        equation.set("0")
        expression = ""
        messagebox.showerror(title="Error", message="Se produjo un error")


ventana = tk.Tk()

ventana.title("Calculadora Max...")

# Se configura el ancho y alto con .geometry()
ventana.geometry("265x125")

# Las variables de control son objetos especiales que se asocian a los widgets
#  para almacenar sus valores y facilitar su disponibilidad
# en otras partes del programa.
# Pueden ser de tipo numérico, de cadena y booleano.
equation = tk.StringVar()

# Caja para cargar y ver resultados
visor = tk.Entry(textvariable=equation)
visor.config(state="disabled")
# El metodo grid is usado para posicion los widget con posiciones relativas
# en una  estructura tipo tabla.
visor.grid(columnspan=4, ipadx=70)

equation.set("0")


button1 = tk.Button(
    text=" 1 ", command=lambda: press(1), fg="black", bg="white", height=1, width=7
)
button1.grid(row=2, column=0)

button2 = tk.Button(
    text=" 2 ", command=lambda: press(2), fg="black", bg="white", height=1, width=7
)
button2.grid(row=2, column=1)

button3 = tk.Button(
    text=" 3 ", command=lambda: press(3), fg="black", bg="white", height=1, width=7
)
button3.grid(row=2, column=2)

button4 = tk.Button(
    text=" 4 ", command=lambda: press(4), fg="black", bg="white", height=1, width=7
)
button4.grid(row=3, column=0)

button5 = tk.Button(
    text=" 5 ", command=lambda: press(5), fg="black", bg="white", height=1, width=7
)
button5.grid(row=3, column=1)


button6 = tk.Button(
    text=" 6 ", command=lambda: press(6), fg="black", bg="white", height=1, width=7
)
button6.grid(row=3, column=2)


button7 = tk.Button(
    text=" 7 ", command=lambda: press(7), fg="black", bg="white", height=1, width=7
)
button7.grid(row=4, column=0)

button8 = tk.Button(
    text=" 8 ", command=lambda: press(8), fg="black", bg="white", height=1, width=7
)
button8.grid(row=4, column=1)

button9 = tk.Button(
    text=" 9 ", command=lambda: press(9), fg="black", bg="white", height=1, width=7
)
button9.grid(row=4, column=2)

button0 = tk.Button(
    text=" 0 ", command=lambda: press(0), fg="black", bg="white", height=1, width=7
)
button0.grid(row=5, column=0)

bsuma = tk.Button(text=" + ", command=lambda: press("+"), fg="black", height=1, width=7)
bsuma.grid(row=2, column=3)


bresta = tk.Button(
    text=" - ", command=lambda: press("-"), fg="black", height=1, width=7
)
bresta.grid(row=3, column=3)


bmult = tk.Button(text=" * ", command=lambda: press("*"), fg="black", height=1, width=7)
bmult.grid(row=4, column=3)

bdiv = tk.Button(text=" / ", command=lambda: press("/"), fg="black", height=1, width=7)
bdiv.grid(row=5, column=3)


bigual = tk.Button(text=" = ", command=equalpress, fg="black", height=1, width=7)
bigual.grid(row=5, column=2)

bclear = tk.Button(text="Clear", command=clear, fg="black", height=1, width=7)
bclear.grid(row=5, column="1")

ventana.mainloop()
