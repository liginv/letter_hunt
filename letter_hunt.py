import datetime
import time
import random
import string

letters = list(string.ascii_lowercase)
score = 0
fail = 0
active_letters = []
sleep_time=2

def random_choice():
    return random.choice(letters)

def active_add_letters():
    random_letter=random_choice()
    time.sleep(sleep_time)
    active_letters.append(random_letter)
    print(active_letters)
    return active_letters

def letter_check(user_input):
    global score
    global fail
   # active_add_letters()
   # score=0
    #fail=0
    if user_input in active_letters:
        active_letters.remove(user_input)
        score += 1
    else:
        fail += 1

    print("score is {}".format(score))
    print("{} failed attempts".format(fail))
    print(active_letters)
   # return score,fail
    
