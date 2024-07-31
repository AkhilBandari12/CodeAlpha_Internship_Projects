import random
import time

# Function to choose a random word from a list
def choose_word():
    words = ['python', 'hangman', 'computer', 'programming', 'coding', 'game', 'algorithm']
    return random.choice(words)

# Function to display the hangman
def display_hangman(tries):
    stages = [  
                '''
                   --------
                   |      |
                   |      
                   |      
                   |      
                   |     
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      
                   |      
                   |     
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   |     
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     /|
                   |      
                   |     
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      
                   |     
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |     / 
                   |     
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |     / \\
                   |     
                '''
    ]
    return stages[tries]

# Function to initialize the game
def hangman():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6
    start_time = time.time()

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print("\n")

    while tries > 0:
        # Displaying the word with guessed letters
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print(display_word)

        # Taking user input
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            if set(word_letters) == guessed_letters:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Congratulations! You guessed the word '{word}' correctly in {elapsed_time:.2f} seconds!")
                break
        else:
            tries -= 1
            print(display_hangman(tries))
            print(f"Wrong guess! You have {tries} tries left.")

        guessed_letters.add(guess)

    if tries == 0:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Sorry, you ran out of tries. The word was:", word)
        print(f"Time elapsed: {elapsed_time:.2f} seconds")

# Calling the hangman function to start the game
hangman()
