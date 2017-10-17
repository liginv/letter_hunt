# import datetime # unused
import time
import random
import string
strike_list = []
strike = 0

letters = (string.ascii_lowercase)
score = 0
fail = 0
active_letters = []
sleep_time = 2
initial_size = 10


def random_choice():
    return random.choice(letters)


def active_add_letters():
    if len(active_letters) < 5:
        for i in range(0, initial_size):
            random_letter = random_choice()
            # time.sleep(sleep_time)
            active_letters.extend(random_letter)
        return active_letters
    else:
        return active_letters


def count_strike(input):
    global strike_list
    global strike
    global sleep_time
    if len(strike_list) > 0:
        if strike_list[-1] == input:
            strike_list.append(input)
        else:
            strike_list = [input]
        if len(strike_list) == 5:
            if strike_list[0] == 1:
                if strike > 6:
                    pass
                else:
                    strike += 1
                    sleep_time -= 0.2
            strike_list = []
    else:
        strike_list = [input]


def letter_check(user_input):
    global score
    global fail
    # active_add_letters()
    # score=0
    # fail=0
    if user_input in active_letters:
        active_letters.remove(user_input)
        score += 1
        count_strike(1)
    else:
        fail += 1
        count_strike(0)

    print("score is {}".format(score))
    print("{} failed attempts".format(fail))
    print(active_letters)
    print("{} strike".format(strike))
    print(sleep_time)
