import random

# define a dictionary of countries and their capitals
countries_capitals = {
    "Kenya": "Nairobi",
    "Uganda": "Kampala",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Brazil": "Brasilia",
    "India": "New Delhi",
    "Japan": "Tokyo",
    "Russia": "Moscow",
    "China": "Beijing",
    "United Kingdom":"London",
    "USA": "Washington D.C."
}

# Function to choose a random country from the dictionary
def choose_country():
    country = random.choice(list(countries_capitals.keys()))
    return country

# Function to check if the guess is correct
def check_guess(guess, country):
    capital = countries_capitals[country]
    return guess.lower() == capital.lower()

# Main game loop
while True:
    # Choose a random country
    country = choose_country()

    # Player 1's turn
    print("Player 1's turn")
    guess = input(f"What is the capital of {country}? ")
    if check_guess(guess, country):
        print("Correct!")
    else:
        print("Incorrect.")

    # Player 2's turn
    print("Player 2's turn")
    guess = input(f"What is the capital of {country}? ")
    if check_guess(guess, country):
        print("Correct!")
    else:
        print("Incorrect.")

    # Ask if the players want to continue playing
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        break

print("Thanks for playing!")
