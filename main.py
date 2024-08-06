#Termial Wordle

#By Aaron
#07/23/24

import random

error_msg = "Please select \"Y\" or \"N\"."

def instructions():
    instr_msg = "\nYou have 6 guesses to correctly guess a 5 letter word.\nEach guess you make will tell you information on what the word could be.\nYour guess will appear above the progress word for better visualization\n\
    If you guessed a correct letter, this will appear as a lowercase letter.\nIf the correct letter in the correct space, this will appear as an uppercase letter.\n"
    print(instr_msg)
    return

def pick_random_word ():

    with open("random_words.txt", "r") as file:
        content = file.readlines()

    with open("random_words.txt", "r") as file:    
        num_lines = len(file.readlines())

    global value
    value = random.randint(0,num_lines)

    print(content[value].rstrip("\n"))

    file.close()
    return content[value].rstrip("\n")

# Base function to provide a clear structure of how the game is setup.
def start_game ():
    print("A random word has been generated.\n")
    answer = pick_random_word()
    make_your_guess(answer)



def make_your_guess (answer):
        
        correct_letters = ""

        for x in range (6):
            correct_space = list("-----")
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
                        if i == j:
                            correct_space[i] = guess[i] 
                        elif correct_space[i] =="-" or correct_space[i].islower():
                            correct_space[i] = guess[i].lower()
            
            breakdown = list("-----")
            breakdown2 = list("-----")
            for i in range (5):
                breakdown[i] = answer.count(correct_space[i].upper())
                breakdown2[i] = guess.count(correct_space[i].upper())

            for i in range(5):
                # If the guess has more identical characters than in the answer
                if breakdown[i] < breakdown2[i] and correct_space[i].islower():
                    for j in range(5):
                        # 
                        if correct_space[j].isupper() and correct_space[i] == correct_space[j]:
                            continue
                        else:
                            correct_space[i] = "-"

            print(breakdown)
            print(breakdown2)
                

            print(guess)
            print("".join(correct_space))


        out_of_turns()
        return
    
def correct_guess():
    print("That is correct!, You WIN!!\n")

    replay = input("Would you like to play again? (Y/N)")

    if replay.upper() != "Y" and replay.upper() != "N":
        print(error_msg)
    elif replay.upper() == "Y":
        start_game()
    else:
        return

def out_of_turns():
    print("You lost, unfortunate....Get good.")

welcome_msg = "Welcome to Aaron's Version of Wordle!\n\nThis is just wordle without the GUI...\n\nFor instructions to play press \"Y\", press \"N\" to skip."
print(welcome_msg)

details = input()

if details.upper() != "Y" and details.upper() != "N":
    print(error_msg)
elif details.upper() == "Y":
    instructions()

start_game()
