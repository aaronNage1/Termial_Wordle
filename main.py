#Termial Wordle

#By Aaron
#07/23/24

def instructions():
    instr_msg = "\nYou have 6 guesses to correctly guess a 5 letter word.\nEach guess you make will tell you information on what the word could be.\n\
        If you guessed a correct letter, this will appear in the correct letters list below each guess.\nIf the correct letter in the correct space, this will appear in the word progress bar below.\n"
    print(instr_msg)
    return

def pick_random_word ():
    our_word = "Hello"
    return our_word

def start_game ():
    print("A random word has been generated.\n")
    answer = pick_random_word()
    make_your_guess(answer)


def make_your_guess (answer):
        for x in range (6):
            player_input = "You are on guess " + str(x) + " out of 6:"
            guess = input(player_input)
            check_guess(guess, answer)

        out_of_turns()


def check_guess(guess, answer):
    if len(guess)!=5:
        print("Error, you must guess a 5 letter word.")

    if guess.upper() == answer.upper():
        correct_guess()

    
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
