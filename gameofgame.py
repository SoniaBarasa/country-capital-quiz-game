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



# Function to check if the guess is correct
def check_guess(guess, country):
    capital = countries_capitals[country]
    if guess.lower() == capital.lower():
        return True
    else:
        return False

# Initialize player scores
player1_score = 0
player2_score = 0

# Main game loop
#function to list all available countries
available_countries =list(countries_capitals.keys())
while True:
    if not available_countries:
        print("All countries have been played!")
        break

    # Choose a random country
    country=random.sample(available_countries,1) [0]
    available_countries.remove(country)

    # Both Players take turns to play
    print("Player 1's turn")
    player1_guess = getpass.getpass(prompt=f"What is the capital of {country}? ")

    print("Player 2's turn")
    player2_guess = getpass.getpass(prompt=f"What is the capital of {country}? ")

    # Reveal the correct answer
    capital = countries_capitals[country]
    print(f"The correct answer is {capital}.")

    # Check the guesses and update the scores
    if check_guess(player1_guess, country) and check_guess(player2_guess, country):
        print("Both players guessed correctly!")
        player1_score += 1
        player2_score += 1
    elif check_guess(player1_guess, country):
        print("Player 1 guessed correctly!")
        player1_score += 1
    elif check_guess(player2_guess, country):
        print("Player 2 guessed correctly!")
        player2_score += 1
    else:
        print("Neither player guessed correctly.")
        
    # Print the current scores
    print(f"Current scores: Player 1: {player1_score}, Player 2: {player2_score}")
    
    # Ask if the players want to continue playing
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        break

print("Thanks for playing!")