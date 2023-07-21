import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_neg = 0
        cant_neg = 0
        suma_pos = 0
        cant_pos = 0
        cant_ceros = 0
        dif_pos_neg = 0

        while True:
            numero = prompt("ej 6", "Ingrese un número")

            if numero == None:
                break

            numero = int(numero)

            for i in range(0,numero+1):
                if numero < 0:
                    suma_neg += numero
                    cant_neg += 1
                elif numero > 0:
                    suma_pos += numero
                    cant_pos += 1
                else:
                    cant_ceros += 1
            dif_pos_neg = suma_pos - suma_neg

        alert("suma de neg", f"{suma_neg}")            
        alert("suma de pos", f"{suma_pos}")            
        alert("suma de neg", f"{cant_neg}")            
        alert("suma de pos", f"{cant_neg}")            
        alert("cantidad de ceros", f"{cant_ceros}")
        alert("diferencia entre pos y neg", f"{dif_pos_neg}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
