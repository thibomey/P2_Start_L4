import tkinter
import requests

window = tkinter.Tk()
window.title("Kleuren kiezer")
window.geometry("300x200")

label = tkinter.Label(window, text="Welkom bij pokedex!")
label.pack()

pokemon = tkinter.Entry(window)
pokemon.pack()



def zoek():
    pokemonnaam = pokemon.get().lower()
    request = requests.get(
        url=f"https://pokeapi.co/api/v2/pokemon/{pokemonnaam}",
    )
    if request.status_code == 200:
        data = request.json()
        print(data['abilities'][0]['ability']['name'])
        print(data['abilities'])
        pass
    else:
        print ("Error")

label = tkinter.Label(window, text=zoek)
label.pack()

button = tkinter.Button(window, text="Zoek pokemon", command=zoek)
button.pack()






window.mainloop()