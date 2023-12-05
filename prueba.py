import requests
import tkinter as tk
from tkinter import messagebox

def obtener_informacion_pokemon(nombre):
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre.lower()}'
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()

def mostrar_estadisticas():
    nombrePokemon = entry.get()
    datosPokemon = obtener_informacion_pokemon(nombrePokemon)

    if datosPokemon:
        mensaje = f"\nEstadísticas de {nombrePokemon.capitalize()}:\n"
        mensaje += f"Nombre: {datosPokemon['name'].capitalize()}\n"
        mensaje += f"Número en la Pokédex: {datosPokemon['id']}\n"
        mensaje += f"Altura: {datosPokemon['height'] / 10} metros\n"  # Decímetros
        mensaje += f"Peso: {datosPokemon['weight'] / 10} kilogramos\n"  # Hectogramos
        tipos = [tipo['type']['name'] for tipo in datosPokemon['types']]
        tipos_capitalizados = [tipos[0].capitalize()] + tipos[1:]
        mensaje += f"Tipo: {','.join(tipos_capitalizados)}"
        messagebox.showinfo("Estadísticas Pokémon", mensaje)
    else:
        messagebox.showinfo("Error", "No existe tu Pokémon")

ventana = tk.Tk()
ventana.title("Pokémon Info App")

label = tk.Label(ventana, text="Ingresa el nombre de un Pokémon o Código de Pokédex:")
label.pack()

entry = tk.Entry(ventana)
entry.pack()

button = tk.Button(ventana, text="Mostrar Estadísticas", command=mostrar_estadisticas)
button.pack()

ventana.mainloop()