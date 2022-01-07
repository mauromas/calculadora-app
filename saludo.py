import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

### FUNCIONES ####


def saludar():
    # Me permite acceder a la variable "saludos" definida
    # fuera de la función.
    global saludos

    # Chequear que los saludos no sean mayores a cinco.
    # Una vez alcanzados, se muestra un mensaje de error.
    if saludos == 5:
        messagebox.showerror(
            title="Error", message="Ya se han mostrado los 5 saludos permitidos."
        )
        return  # CON EL RETURN TERMINO LA FUNCIÓN

    # OBTENER EL NOMBRE EN LA CAJA DE TEXTO
    nombre = entry.get()

    # CHEQUEAR QUE NO ESTE VACIO

    if nombre:
        # MOSTRAR EL NOMBRE EN LA ETIQUETA
        label.configure(text=f"¡Hola, {nombre}!")

        # AÑADIR EL NOMBRE A LA LISTA
        lista_nombres.insert(tk.END, nombre)

        # BORRAR EL CONTENIDO DE LA CAJA DE TEXTO
        entry.delete(0, tk.END)

        # AUMENTAR EL CONTADOR DE SALUDOS
        saludos += 1

    else:
        messagebox.showinfo(
            title="Falta información", message="Debe ingresar un nombre."
        )


saludos = 0

ventana_principal = tk.Tk()

ventana_principal.title("Ejercicio Integrador ")


ventana_principal.config(width=300, height=200)


# CAJA DE TEXTO

entry = ttk.Entry()
entry.place(x=10, y=10)

# BOTÓN
boton = ttk.Button(text="¡Saludar!", command=saludar)
boton.place(x=150, y=8)

# ETIQUETA
label = ttk.Label(text="Nombre")
label.place(x=10, y=40)

# LISTA
lista_nombres = tk.Listbox()
lista_nombres.place(x=10, y=60, width=278, height=120)


ventana_principal.mainloop()
