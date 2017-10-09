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
    return active_letters

def letter_check(user_input):
    global score
    global fail
    active_add_letters()
   # score=0
    #fail=0
    if user_input in active_letters:
        score += 1
    else:
        fail += 1

    print("score is {}".format(score))
    print("{} failed attempts".format(fail))
    
