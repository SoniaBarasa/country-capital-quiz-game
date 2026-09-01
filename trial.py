#```python
import random
import getpass
import pycountry
from countryinfo import CountryInfo


# Function to check if the guess is correct
def check_guess(guess, country, countries_capitals):
    capital = countries_capitals[country]

    if guess.lower().strip() == capital.lower().strip():
        return True
    else:
        return False


# Fetch all countries and their capitals using pycountry
def get_countries_capitals():
    countries_capitals = {}

    for country in pycountry.countries:
        try:
            country_info = CountryInfo(country.alpha_2)
            capital = country_info.capital()

            if capital:
                countries_capitals[country.name] = capital

        except (KeyError, ValueError):
            continue

    return countries_capitals


def main():

    # Initialize player scores
    player1_score = 0
    player2_score = 0

    # Get countries and capitals
    countries_capitals = get_countries_capitals()
    available_countries = list(countries_capitals.keys())

    print("===================================")
    print("       CAPITAL CITY GAME")
    print("===================================")
    print("Player 1 and Player 2 will take turns.")
    print("The game can continue for as many rounds as you want!")
    print()

    # Endless game loop
    while True:

        # Select a random country
        # The country is NOT removed, so it can appear again later
        country = random.choice(available_countries)

        print("\n-----------------------------------")
        print(f"Player 1's turn")
        print("-----------------------------------")

        player1_guess = getpass.getpass(
            prompt=f"What is the capital of {country}? "
        )

        print("\n-----------------------------------")
        print(f"Player 2's turn")
        print("-----------------------------------")

        player2_guess = getpass.getpass(
            prompt=f"What is the capital of {country}? "
        )

        # Reveal the correct answer
        capital = countries_capitals[country]
        print(f"\nThe correct answer is: {capital}")

        # Check Player 1
        player1_correct = check_guess(
            player1_guess,
            country,
            countries_capitals
        )

        # Check Player 2
        player2_correct = check_guess(
            player2_guess,
            country,
            countries_capitals
        )

        # Update scores
        if player1_correct and player2_correct:

            print("Both players guessed correctly!")
            player1_score += 1
            player2_score += 1

        elif player1_correct:

            print("Player 1 guessed correctly!")
            print("Well done, Player 1!")
            player1_score += 1

        elif player2_correct:

            print("Player 2 guessed correctly!")
            print("Well done, Player 2!")
            player2_score += 1

        else:

            print("Neither player guessed correctly.")
            print("You both should learn about capital cities!")

        # Display scores after every round
        print("\n========== CURRENT SCORES ==========")
        print(f"Player 1: {player1_score}")
        print(f"Player 2: {player2_score}")
        print("====================================")

        # Ask whether players want another round
        play_again = input(
            "\nDo you want to continue playing? (y/n): "
        )

        if play_again.lower().strip() != "y":
            break

    # Determine the final winner
    print("\n===================================")
    print("           FINAL SCORES")
    print("===================================")
    print(f"Player 1: {player1_score}")
    print(f"Player 2: {player2_score}")
    print("===================================")

    if player1_score > player2_score:

        print("Congratulations Player 1, you are the winner!")

    elif player2_score > player1_score:

        print("Congratulations Player 2, you are the winner!")

    else:

        print("The game ended in a tie. Well played both players!")

    print("\nThanks for playing!")


# Call the main function
if __name__ == "__main__":
    main()
#```
