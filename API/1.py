import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    return name, abilities

pokemon_name, abilities = fetch_pokemon_data('pikachu')
print(f"Name: {pokemon_name}, Abilities: {', '.join(abilities)}")


import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    weight = data['weight'] / 10.0  # Weight is in hectograms, converting to kilograms
    return name, abilities, weight

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        _, _, weight = fetch_pokemon_data(pokemon)
        total_weight += weight
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
for pokemon in pokemon_names:
    name, abilities, weight = fetch_pokemon_data(pokemon)
    print(f"Name: {name}, Abilities: {', '.join(abilities)}, Weight: {weight} kg")

average_weight = calculate_average_weight(pokemon_names)
print(f"Average Weight of the Pokémon: {average_weight:.2f} kg")


