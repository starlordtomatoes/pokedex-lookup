import requests
import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

def play_sound():
    sound = pygame.mixer.Sound("pokedex_beep.mp3")
    sound.play()
    time.sleep(1)  # Keeps the program open so the sound finishes playing

def get_pokedex_entry(pokemon):
    species_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon.lower()}"
    response = requests.get(species_url)

    if response.status_code == 200:
        data = response.json()
        name = data["name"].capitalize()

        # Get the latest English Pokédex entry
        for entry in data["flavor_text_entries"]:
            if entry["language"]["name"] == "en":
                pokedex_entry = entry["flavor_text"].replace("\n", " ").replace("\f", " ")
                break
        
        # Play the Pokédex sound before showing the entry
        play_sound()

        print(f"📜 Name: {name}")
        print(f"📖 Pokédex Entry: {pokedex_entry}")
    else:
        print("❌ Pokémon not found!")

if __name__ == "__main__":
    pokemon = input("Enter Pokémon name or number: ")
    get_pokedex_entry(pokemon)
