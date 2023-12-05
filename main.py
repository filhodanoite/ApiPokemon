import requests
import tkinter as tk
from tkinter import messagebox

class Pokemon:
    def __init__(self, nombre):
        # Inicializa un objeto Pokemon con el nombre ingresado y obtiene información del Pokemon.
        self.nombre = nombre.lower()
        self.datos = self.obtenerInformacionPokemon()

    def obtenerInformacionPokemon(self):
        # Consulta la API de Pokémon para obtener información sobre el Pokemon.
        url = f'https://pokeapi.co/api/v2/pokemon/{self.nombre}'
        respuesta = requests.get(url)
        # Si la solicitud es exitosa (código de estado 200), devuelve la respuesta en formato JSON.
        if respuesta.status_code == 200:
            return respuesta.json()

    def mostrarEstadisticas(self):
        # Muestra las estadísticas del Pokemon en una ventana emergente.
        if self.datos:
             # Obtiene informacion del Pokemon  como nombre, tipo y numero de la pokedex
            mensaje = f"\nEstadísticas de {self.nombre.capitalize()}:\n"
            mensaje += f"Nombre: {self.datos['name'].capitalize()}\n"
            mensaje += f"Número en la Pokédex: {self.datos['id']}\n"
            mensaje += f"Tipo: {', '.join([tipo['type']['name'].capitalize() for tipo in self.datos['types']])}\n"
            habilidades = [habilidad['ability']['name'].capitalize() for habilidad in self.datos['abilities']]
            mensaje += f"Habilidades: {', '.join(habilidades)}\n"
             # Agrega al mensaje las estadisticas del Pokemon 
            mensaje += "\nEstadísticas de combate:\n"
            for stats in self.datos['stats']:
                statNombre = stats['stat']['name'].capitalize()
                statValor = stats['base_stat']
                mensaje += f"{statNombre}: {statValor}\n"
            messagebox.showinfo("Estadísticas de Pokémon", mensaje)
        else:
            messagebox.showinfo("Error", "No existe tu Pokémon")

def mostrarEstadisticas():
    # Obtiene el nombre ingresado, crea un objeto Pokemon  y muestra sus estadísticas.
    nombrePokemon = entry.get()
    pokemon = Pokemon(nombrePokemon)
    pokemon.mostrarEstadisticas()

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Pokémon Info App")

# Etiqueta que indica al usuario que ingrese el nombre del Pokemon o su número en la Pokédex.
label = tk.Label(ventana, text="Ingresa el nombre de un Pokémon o Código de Pokédex:")
label.pack()

# Cuadro de entrada para que el usuario ingrese el nombre del Pokemon o su número en la Pokédex.
entry = tk.Entry(ventana)
entry.pack()

# Botón que, al hacer clic, muestra las estadísticas del Pokemon ingresado.
button = tk.Button(ventana, text="Mostrar Estadísticas", command=mostrarEstadisticas)
button.pack()

# Inicia el bucle principal de la interfaz gráfica.
ventana.mainloop()
