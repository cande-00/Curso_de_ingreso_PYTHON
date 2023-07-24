'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        total_de_votos = 0
        suma_edad = 0
        max_votos = 0
        min_votos = 0
        max_nombre_votos = ""
        min_nombre_votos = ""
        min_edad_votos = 0
        cant_edades = 0
        promedio_edades = 0
        

        while True:
            nombre = prompt("Candidato", "Ingrese el nombre")
            while nombre == None or nombre == "" or not nombre.isalpha():
                nombre = prompt("Candidato", "Reingrese el nombre")
            
            edad = prompt("Candidato", "Ingrese la edad")
            if edad == None or not edad.isdigit() or int(edad) < 25 or int(edad) > 90:
                edad = prompt("Candidato", "Reingrese la edad")
            else:
                suma_edad += int(edad)
                cant_edades += 1
            edad = int(edad)

            cant_de_votos = prompt("Candidato", "Ingrese cant de votos")
            while cant_de_votos == None or not cant_de_votos.isdigit() or int(cant_de_votos) < 0:
                cant_de_votos = prompt("Candidato", "Reingrese cant de votos")
            cant_de_votos = int(cant_de_votos)

            if max_votos == None or cant_de_votos > max_votos:
                max_votos = cant_de_votos
                max_nombre_votos = nombre

            if min_votos == None or cant_de_votos < min_votos:
                min_votos = cant_de_votos
                min_nombre_votos = nombre
                min_edad_votos = edad

            total_de_votos += cant_de_votos
            promedio_edades = suma_edad / cant_edades

            print(f"El candidato mas votado es: {max_nombre_votos}" )
            print(f"El candidato menos votado es: {min_nombre_votos} y su edad es: {min_edad_votos}")
            print(f"El promedio de las edades es: {promedio_edades}")
            print(f"La cantidad de votos es: {total_de_votos}")

            continuar = question("Candidato", "¿Desea continuar?")
            if not continuar:
                break


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
