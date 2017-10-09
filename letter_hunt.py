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
