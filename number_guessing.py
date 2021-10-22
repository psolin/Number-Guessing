import random
from time import sleep


def main():
    ceiling = int(input("Computer: How high do you want to guess? "))
    guess_range = [1, ceiling]
    selected_num = random.randrange(1, ceiling + 1)
    turns = 0
    move_choice = ["User", "Computer"]
    sleep(1)
    print("Computer: Flipping a coin...")
    sleep(1)
    move_first = random.choice(move_choice)
    if move_first == "User":
        print("Computer: Your turn.")
        user_guess(ceiling, guess_range, turns, selected_num)
    else:
        computer_guess(ceiling, guess_range, turns, selected_num)


# Checking a guess
def guess_check(guess, guess_range, selected_num):
    if guess < selected_num:
        returned_string = "Wrong. It's higher."
        if guess_range[0] <= guess:
            guess_range = [guess + 1, guess_range[1]]
    elif guess > selected_num:
        returned_string = "Wrong. It's lower."
        if guess_range[1] >= guess:
            guess_range = [guess_range[0], guess]
    else:
        guess_range = [guess, guess]
        returned_string = "Correct."
    return returned_string, guess_range


def computer_thinks():
    sleep(random.randrange(1, 3))
    print("")
    sleep(random.randrange(1, 3))
    print("Computer: Computing...")
    sleep(random.randrange(1, 3))
    print("")
    sleep(random.randrange(1, 3))


def computer_guess(ceiling, guess_range, turns, selected_num):
    sleep(1)
    print("Computer: My turn.")
    sleep(1)
    guess = random.randrange(guess_range[0], guess_range[1])
    print("Computer: I guess %i." % guess)
    computer_thinks()
    result = guess_check(guess, guess_range, selected_num)
    print("Computer: I'm " + result[0][0].lower() + result[0][1:])
    if result[1][0] != result[1][1]:
        user_guess(ceiling, result[1], turns, selected_num)
    else:
        print("Computer: I win. Haha.")


# Guess and check user result
def user_guess(ceiling, guess_range, turns, selected_num):
    guess_string = "Computer: Guess a number between 1 and %i: " % ceiling
    turns += 1
    guess = int(input(guess_string))
    computer_thinks()
    result = guess_check(guess, guess_range, selected_num)
    if result[1][0] != result[1][1]:
        print("Computer: You're " + result[0][0].lower() + result[0][1:])
        computer_guess(ceiling, result[1], turns, selected_num)
    else:
        if turns == 1:
            print("Computer: You win. It took you %s turn." % turns)
        else:
            print("Computer: You win. It took you %s turns." % turns)


if __name__ == "__main__":
    main()
