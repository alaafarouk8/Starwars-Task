import requests as requests

from timer import timer

SWAPI_BASE = 'https://swapi.dev/api/'


@timer
def get_Movies(movies_url):
    """ get movies list which the character appeared in"""
    moviesRes = movies_url
    movies_list = []
    for movie in moviesRes:
        movieUrl = requests.get(movie).json()
        movies_list.append(movieUrl['title'])
    return movies_list


@timer
def get_home_planet(planet_url):
    """ function to get name of the planet """
    planetRes = requests.get(planet_url).json()
    planet_name = planetRes['name']
    return planet_name


@timer
def get_species(species_url):
    """ function to get name of species and average life span """
    speciesRes = species_url
    spacesNames = ""
    spacesLifeSpan = ""
    for species in speciesRes:
        speciesUrl = requests.get(species).json()
        spacesNames = speciesUrl['name']
        spacesLifeSpan = speciesUrl['average_lifespan']

    return {'name': spacesNames, 'lifespan': spacesLifeSpan}


@timer
def getAllDetails(character):
    """Function to all details for the character"""
    charRes = requests.get(f'{SWAPI_BASE}people/?search={character}').json()
    if charRes['count'] == 0:
        return {'MessageError': 'Sorry, This Character Not Found '}
    data = charRes['results']
    results = []
    for char in data:
        char_data = {}
        char_data["character_name"] = char['name']
        char_data["character_gender"] = char['gender']
        speciesURL = char['species']
        planetURL = char['homeworld']
        moviesURL = char['films']
        species = get_species(speciesURL)
        char_data['species_name'] = species['name']
        char_data['lifespan'] = species['lifespan']
        planet = get_home_planet(planetURL)
        char_data["home_planet_name"] = planet
        movies = get_Movies(moviesURL)
        char_data["list_movies"] = movies

        results.append(char_data)
    return results
