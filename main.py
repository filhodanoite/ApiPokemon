import requests
import tkinter as tk
from tkinter import messagebox

class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre.lower()
        self.datos = self.obtenerInformacionPokemon()

    def obtenerInformacionPokemon(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.nombre}'
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            return respuesta.json()

    def mostrarEstadisticas(self):
        if self.datos:
            mensaje = f"\nEstadísticas de {self.nombre.capitalize()}:\n"
            mensaje += f"Nombre: {self.datos['name'].capitalize()}\n"
            mensaje += f"Número en la Pokédex: {self.datos['id']}\n"
            mensaje += f"Tipo: {', '.join([tipo['type']['name'].capitalize() for tipo in self.datos['types']])}\n"
            habilidades = [habilidad['ability']['name'].capitalize() for habilidad in self.datos['abilities']]
            mensaje += f"Habilidades: {', '.join(habilidades)}\n"
            mensaje += "\nEstadísticas de combate:\n"
            for stats in self.datos['stats']:
                statNombre = stats['stat']['name'].capitalize()
                statValor = stats['base_stat']
                mensaje += f"{statNombre}: {statValor}\n"
            messagebox.showinfo("Estadísticas de Pokémon", mensaje)
        else:
            messagebox.showinfo("Error", "No existe tu Pokémon")
a
def mostrarEstadisticas():
    nombre_pokemon = entry.get()
    pokemon = Pokemon(nombre_pokemon)
    pokemon.mostrarEstadisticas()

ventana = tk.Tk()
ventana.title("Pokémon Info App")

label = tk.Label(ventana, text="Ingresa el nombre de un Pokémon o Código de Pokédex:")
label.pack()

entry = tk.Entry(ventana)
entry.pack()

button = tk.Button(ventana, text="Mostrar Estadísticas", command=mostrarEstadisticas)
button.pack()

ventana.mainloop()
