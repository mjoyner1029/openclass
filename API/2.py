import requests


def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
# Check for request errors
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code}")
    
    planets = response.json()['bodies']
    planet_data = []
    for planet in planets:
        if planet.get('isPlanet'):
            name = planet.get('englishName', 'N/A')
            mass = planet.get('mass', {}).get('massValue', 'N/A')
            orbit_period = planet.get('sideralOrbit', 'N/A')
 # Ensure mass and orbit period are not 'N/A'
            if mass != 'N/A' and orbit_period != 'N/A':
                planet_data.append({'name': name, 'mass': mass, 'orbit_period': orbit_period})
    
    return planet_data

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda p: p['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']

planets = fetch_planet_data()
for planet in planets:
    print(f"Planet: {planet['name']}, Mass: {planet['mass']}, Orbit Period: {planet['orbit_period']} days")

name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")
