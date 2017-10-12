import datetime
import time
import random
import string

letters = list(string.ascii_lowercase)
score = 0
fail = 0
active_letters = []
life = 10
sleep_time=2.0
streak = 0

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
    elif user_input == "":
        pass
        
    else:
        fail += 1

    print("score is {}".format(score))
    print("{} failed attempts".format(fail))
    print(active_letters)

def main():
    while life > 0:
        active_add_letters()
        try:
            input1 = input
            letter_check(input1)

        except:
            pass
        
    
# def streak_time():
#     global sleep_time
#     tmp = streak
#     if tmp not == streak
#     streak_list = { 0 : 2.0
#                     1 : 1.8
#                     2 : 1.6
#                     3 : 1.4000000000000001
#                     4 : 1.2000000000000002
#                     5 : 1.0000000000000002
#                     6 : 0.8000000000000003
#                     7 : 0.6000000000000003
#                     }

                    # if streak == 1:
    #     sleep_time -= 0.2
    # if streak == 2:
    #     sleep_time -= 0.2
    # if streak == 3:
    #     sleep_time -= 0.2
    # if streak == 4:
    #     sleep_time -= 0.2
    # if streak == 5:
    #     sleep_time -= 0.2
    # if streak == 6:
    #     sleep_time -= 0.2
    # if streak == 7:
    #     sleep_time -= 0.2
    # if streak == 8:
    #     sleep_time -= 0.2
    # if streak == 9:
    #     sleep_time -= 0.2
    # if streak == 10:
    #     sleep_time -= 0.2
    # print(sleep_time)
