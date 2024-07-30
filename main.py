#Termial Wordle

#By Aaron
#07/23/24

import random

def instructions():
    instr_msg = "\nYou have 6 guesses to correctly guess a 5 letter word.\nEach guess you make will tell you information on what the word could be.\n\
    If you guessed a correct letter, this will appear in the correct letters list below each guess.\nIf the correct letter in the correct space, this will appear in the word progress bar below.\n"
    print(instr_msg)
    return

def pick_random_word ():

    with open("random_words.txt", "r") as file:
        content = file.readlines()

    with open("random_words.txt", "r") as file:    
        num_lines = len(file.readlines())

    global value
    value = random.randint(0,num_lines)

    print(content[value])

    our_word = "Hello"

    file.close()
    return our_word

# Base function to provide a clear structure of how the game is setup.
def start_game ():
    print("A random word has been generated.\n")
    answer = pick_random_word()
    make_your_guess(answer)


def make_your_guess (answer):
        
        correct_letters = ""

        for x in range (6):
            player_input = "You are on guess " + str(x) + " out of 6:"
            guess = input(player_input)
            if len(guess)!=5:
                print("Error, you must guess a 5 letter word.")
        guess = guess.upper()
        answer = answer.upper()

        if guess == answer:
            correct_guess()
            return

        for i in range(5):
            for j in range (5):
                if guess[i] == answer[j]:
                    correct_letters = correct_letters + guess[i]

        if correct_letters == "":
            print("\nNo correct letters are guessed so far.\n")
        else:
            print("\nThe letters " + correct_letters + " are in the answer.\n\n")

        return
    
def correct_guess():
    print("That is correct!, You WIN!!\n")

def out_of_turns():
    print("You lost, unfortunate....Get good.")

welcome_msg = "Welcome to Aaron's Version of Wordle!\n\nThis is just wordle without the GUI...\n\nFor instructions to play press \"Y\", press \"N\" to skip."
print(welcome_msg)

details = input()
details_err_msg = "Can you read?!"

if details.upper() != "Y" and details.upper() != "N":
    print(details_err_msg)
elif details.upper() == "Y":
    instructions()

start_game()
