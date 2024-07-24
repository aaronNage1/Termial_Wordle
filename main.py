# Wordle

welcome_msg = "Welcome to Aaron's Version of Wordle!\n\nThis is just wordle without the GUI...\n\n For instructions to play press \"Y\", press \"N\" to skip."
print(welcome_msg)


details = input()
details_err_msg = "Can you read?!"
print(details)
if details != "Y" or details != "y" or details != "N" or details != "n":
    print(details_err_msg)

def pick_random_word ():
    our_word = "Hello"

def start_game ():
    make_your_guess()





def make_your_guess ():
    first_turn_msg = "You may make your guess:"
    guess = input(first_turn_msg)

    if len(guess>5):
        print("Error, you must guess a 5 letter word.")

start_game()