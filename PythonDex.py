from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pokebase as pb

window = Tk()
window.title('BobDex')
window.geometry('600x700')

label1 = Label(window, text="Enter Pokemon Name", fg="black", pady=20, font=("Arial", 12, "bold"))
label1.pack()

pokemon_input = Entry(window, font=('Arial', 18))
pokemon_input.pack(pady=20)

def search():
    details.delete('1.0', END)
    pokemon_name = pokemon_input.get()
    
    try:
        pokemon = pb.pokemon(pokemon_name)
        
        response = requests.get(pokemon.sprites.front_default)
        image = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))

        pokemon_image.config(image=image)
        pokemon_image.image = image

        abilities = ', '.join([ability.ability.name for ability in pokemon.abilities])
        types = ', '.join([poketype.type.name for poketype in pokemon.types])

        details.insert(END, f"Details for {pokemon_name.capitalize()}:\n")
        details.insert(END, f"Base Experience: {pokemon.base_experience}\n")
        details.insert(END, f"Height: {pokemon.height / 10} m\n")  
        details.insert(END, f"Weight: {pokemon.weight / 10} kg\n") 
        details.insert(END, f"Abilities: {abilities}\n")
        details.insert(END, f"Types: {types}\n")

    except AttributeError:

        missingno_image = ImageTk.PhotoImage(Image.open("missingno.png"))
        pokemon_image.config(image=missingno_image)
        pokemon_image.image = missingno_image

        details.insert(END, "MissingNo")

btn = Button(window, bd='4', text="Search", fg="red", bg="yellow", command=search)
btn.pack()

pokemon_image = Label(window)
pokemon_image.pack(pady=30)

details = Text(window, font=('Arial', 12), bg='light yellow')
details.pack()

window.mainloop()
