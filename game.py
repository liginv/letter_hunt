import letter_hunt
import curses
import random
import time
from curses import wrapper

score = letter_hunt.score
life = letter_hunt.life
screen = curses.initscr()
curses.noecho()
curses.cbreak()

# # Check if screen was re-sized (True or False)
# resize = curses.is_term_resized(y, x)

# # Action in loop if resize is True:
# if resize is True:
#     y, x = screen.getmaxyx()
#     screen.clear()
#     curses.resizeterm(y, x)
#     screen.refresh()

screen.border(0)
# screen.addstr(0, 2, "Score:")
# screen.addstr(0, 8, str(score))
screen.addstr(0, 20, "Welcome to Letter Hunt!")
# screen.addstr(0, 50, "Life Remaining: ")
# screen.addstr(0, 65, str(life))


while life > 0:
    user_input = []
    # letter = chr(screen.getch())
    # user_input.extend(letter)

    for i in range(0, len(letter_hunt.active_add_letters()) - 1):
        screen.addstr(0, 50, "Life Remaining: ")
        screen.addstr(0, 65, str(life))
        screen.addstr(0, 2, "Score:")
        screen.addstr(0, 8, str(score))
        screen.addstr(
            2, i + 2, str(letter_hunt.active_letters[i]))
        time.sleep(letter_hunt.sleep_time)

        letter = chr(screen.getch())
        user_input.extend(letter)
        
        for i in user_input:
            letter_hunt.letter_check(i)
            user_input.remove(i)
        life -= 1
        score = letter_hunt.score
        # screen.addstr(0, 50, "Life Remaining: ")
        # screen.addstr(0, 65, str(life))
        # screen.addstr(0, 2, "Score:")
        # screen.addstr(0, 8, str(score))
        # screen.refresh()
# else:
#     curses.endwin()

