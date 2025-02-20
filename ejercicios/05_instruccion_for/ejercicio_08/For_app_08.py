import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        num = int(prompt("cantidad", "elige un numero"))
        for i in range(1,num+1):
            if num % i == 0 or num & 3 == 0 or num % 5 == 0 or num % 7 == 0:
                resultado = "Es primo"
            else:
                resultado = "No es primo"
        alert("", f"{resultado}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()