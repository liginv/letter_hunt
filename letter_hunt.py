import datetime
import time
import random
import string

letters = list(string.ascii_lowercase)
score = 0
fail = 0
active_letters = []

def random_choice():
    return random.choice(letters)
