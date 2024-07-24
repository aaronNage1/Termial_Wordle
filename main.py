

welcome_msg = "Welcome to Aaron's Version of Wordle!\n\nThis is just wordle without the GUI...\n\n For instructions to play press \"Y\", press \"N\" to skip."
print(welcome_msg)


details = input()
details_err_msg = "Can you read?!"
print(details)
if details != "Y" or details != "y" or details != "N" or details != "n":
    print(details_err_msg)

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

    if guess == answer:
        correct_guess()

    
def correct_guess():
    print("That is correct!, You WIN!!\n")

def out_of_turns():
    print("You lost, unfortunate....Get good.")


start_game()# Wordle
