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
    "United Kingdom": "London",
    "USA": "Washington D.C."
}

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

# Initialize player scores
player1_score = 0
player2_score = 0

#Defining the congratulatory message
congrats_message ="Congratulations Player {winner}, you are the winner!"

# Main game loop
while True:
    # Choose a random country
    country = choose_country()

    # Both Players take turns to play
    # player 1 goes first
    print("Player 1's turn")
    player1_guess = input(f"What is the capital of {country}? ")
    
    # player 2 goes next
    print("Player 2's turn")
    player2_guess = input(f"What is the capital of {country}? ")

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
        print("You both should learn about capital cities in the world!!")
        
    # Print the current scores
    print(f"Current scores: Player 1: {player1_score}, Player 2: {player2_score}")
    
    # Ask if the players want to continue playing
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        break
else:
    print("The game ended in a tie. Well played both players!")
# Print the final scores and congratulate the winner
print(f"Final scores: Player 1: {player1_score}, Player 2: {player2_score}")
if player1_score > player2_score:
    print(congrats_message.format(winner=1))
elif player2_score > player1_score:
    print(congrats_message.format(winner=2))
else:
    print("The game ended in a tie. Well played both players!")
    
print("Thanks for playing!")
