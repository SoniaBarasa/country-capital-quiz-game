import random
import getpass
import pycountry
from countryinfo import CountryInfo

# Fetch all countries and their capitals using pycountry
countries_capitals = {}
for country in pycountry.countries:
    try:
        country_info = CountryInfo(country.alpha_2)
        capital = country_info.capital()
        if capital:
            countries_capitals[country.name] = capital
    except (KeyError, ValueError):
        continue

# Function to choose a random country from the dictionary
def choose_country():
    country = random.choice(list(countries_capitals.keys()))
    return country