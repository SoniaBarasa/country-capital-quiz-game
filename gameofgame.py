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

# Function to check if the guess is correct


def check_guess(guess, country):
    capital = countries_capitals[country]
    if guess.lower() == capital.lower():
        return True
    else:
        return False   
# defining main game logic


def main():
    """Main game logic."""

# Initialize player scores


player1_score = 0
player2_score = 0

# Defining the congratulatory message
congrats_message = "Congratulations Player {winner}, you are the winner!"
# Defining the congratulatory message
congrats_message = "Congratulations Player {winner}, you are the winner!"

# defining string showing player's turn
# defining string showing player's turn
player_turn_str = "Player {player_num}'s turn"
# return False
# return False


# Main game loop
# listing available countries
available_countries = list(countries_capitals.keys())
while True:
    if not available_countries:
        print("All countries have been played!")
        break
    # Choose a random country with replacement
    country = random.sample(available_countries, 1)[0]
    country = random.choice(available_countries)
    available_countries.remove(country)

    # Both Players take turns to play
    # player1 goes first
    # player1 goes first
    print("Player 1's turn")
    player1_guess = input(f"What is the capital of {country}? ")
    player1_guess = getpass.getpass(prompt=f"What is the capital of {country}? ")
    # player 2 goes next
    print(player_turn_str.format(player_num=2))
    player2_guess = input(f"What is the capital of {country}? ")
    # player 2 goes next
    print("Player 2's turn")
    player2_guess = getpass.getpass(prompt=f"What is the capital of {country}? ")

    # Reveal the correct answer
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
        print("Well done, you know your Geography well!")
        player1_score += 1 
    elif check_guess(player2_guess, country):
        print("Player 2 guessed correctly!")
        print("Well done, you know your Geography well!")

        player2_score += 1
    else:
        print("Neither player guessed correctly.")
        print("You both should learn about capital cities in the world!!!")
    # Print the current scores
    print(
        f"Current scores: Player 1: {player1_score}, Player 2: {player2_score}"
        )
     
    print(
        f"Current scores: Player 1: {player1_score}, Player 2: {player2_score}"
        )
    # Ask if the players want to continue playing
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        break
    else:
        print("The game ended in a tie. Well played both players!")

print("Thanks for playing!")
# call the main function
if __name__ == "__main__":
    main()
