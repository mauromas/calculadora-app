import tkinter as tk
from tkinter import messagebox
import requests


def borrar():
    caja_compra.delete(0, tk.END)
    caja_venta.delete(0, tk.END)


def consultar():
    borrar()
    try:
        r = requests.get("https://api-dolar-argentina.herokuapp.com/api/dolaroficial")
        data = r.json()
        compra = data["compra"]
        venta = data["venta"]
        caja_compra.insert(0, compra)
        caja_venta.insert(0, venta)
    except Exception:
        messagebox.showerror("Hubo un error")
        caja_compra.insert(0, "No hay data")
        caja_venta.insert(0, "No hay data")


################################################


ventana = tk.Tk()
ventana.title("Cotización del dolar - API dolar")
ventana.config(width=300, height=300)


etiquta_compra = tk.Label(text="Compra: ")
etiquta_compra.place(x=60, y=20)

caja_compra = tk.Entry()
caja_compra.place(x=60, y=45)

etiqueta_venta = tk.Label(text="Venta: ")
etiqueta_venta.place(x=60, y=80)

caja_venta = tk.Entry()
caja_venta.place(x=60, y=100)

boton = tk.Button(text="Consulta!", command=consultar)
boton.place(x=60, y=140, width=125, height=30)


ventana.mainloop()
