# Burgos Panta Jhon David
import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora Estilo iPhone")
ventana.geometry("360x600")
ventana.configure(bg="black")
ventana.resizable(False, False)

# Fuente y colores
FUENTE = ("Arial", 24)

# Pantalla
entrada = tk.Entry(ventana, font=("Arial", 48), bd=0, bg="black", fg="white",
                   justify="right", insertbackground="white")
entrada.insert(0, "0")
entrada.grid(row=0, column=0, columnspan=4, pady=20, padx=10, sticky="nsew")

# Funciones
def agregar(valor):
    actual = entrada.get()
    if actual == "0":
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, valor)
    else:
        entrada.insert(tk.END, valor)

def calcular():
    try:
        resultado = eval(entrada.get().replace("÷", "/").replace("×", "*").replace("−", "-"))
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def borrar():
    entrada.delete(0, tk.END)
    entrada.insert(0, "0")

# Configurar columnas y filas para expansión
for i in range(5):
    ventana.grid_rowconfigure(i+1, weight=1)
    ventana.grid_columnconfigure(i, weight=1)

# Botones: texto, función, color
botones = [
    ("AC", borrar, "#a5a5a5"), ("+/-", lambda: None, "#a5a5a5"), ("%", lambda: None, "#a5a5a5"), ("÷", lambda: agregar("÷"), "#ff9500"),
    ("7", lambda: agregar("7"), "#333333"), ("8", lambda: agregar("8"), "#333333"), ("9", lambda: agregar("9"), "#333333"), ("×", lambda: agregar("×"), "#ff9500"),
    ("4", lambda: agregar("4"), "#333333"), ("5", lambda: agregar("5"), "#333333"), ("6", lambda: agregar("6"), "#333333"), ("−", lambda: agregar("−"), "#ff9500"),
    ("1", lambda: agregar("1"), "#333333"), ("2", lambda: agregar("2"), "#333333"), ("3", lambda: agregar("3"), "#333333"), ("+", lambda: agregar("+"), "#ff9500"),
    ("0", lambda: agregar("0"), "#333333"), (".", lambda: agregar("."), "#333333"), ("=", calcular, "#ff9500")
]

# Posicionar botones en la cuadrícula
fila = 1
columna = 0
for texto, comando, color in botones:
    colspan = 2 if texto == "0" else 1

    btn = tk.Button(ventana, text=texto, command=comando, bg=color, fg="white", font=FUENTE,
                    bd=0, relief="flat", activebackground=color)
    
    btn.grid(row=fila, column=columna, columnspan=colspan, sticky="nsew", padx=1, pady=1)

    columna += colspan
    if columna >= 4:
        columna = 0
        fila += 1
ventana.mainloop()






