import letter_hunt
import curses
import random
import time
from curses import wrapper

score = letter_hunt.score
life = 10
screen = curses.initscr()

# # Check if screen was re-sized (True or False)
# resize = curses.is_term_resized(y, x)

# # Action in loop if resize is True:
# if resize is True:
#     y, x = screen.getmaxyx()
#     screen.clear()
#     curses.resizeterm(y, x)
#     screen.refresh()

screen.border(0)
screen.addstr(0, 2, "Score:")
screen.addstr(0, 8, str(score))
screen.addstr(0, 20, "Welcome to Letter Hunt!")


if life > 0:
    for i in range(2, len(letter_hunt.active_add_letters()) + 1):
        screen.addstr(
            i, i + 10, str(random.choice(letter_hunt.active_add_letters())))
        time.sleep(letter_hunt.sleep_time)
        life -= 1
        screen.addstr(0, 50, "Life Remaining: ")
        screen.addstr(0, 65, str(life))
        screen.refresh()
else:
    curses.endwin()

screen.getch()
curses.endwin()
