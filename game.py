import letter_hunt
import curses
import curses.panel
import random
import time
from curses import wrapper

screen = curses.initscr()
curses.noecho()
dims = screen.getmaxyx()


def game():
    screen.clear()
    score = letter_hunt.score
    life = letter_hunt.life
    gameover = 10
    row = 1
    column = 1

    window = curses.newwin(2, dims[1] - 2)
    view = curses.panel.new_panel(window)

    screen.border()
    screen.addstr(0, int(dims[1] / 2 - 6), "Letter Hunt!", curses.A_BOLD)
    screen.addstr(int(dims[0] - 2), 2, "Score:", curses.A_BOLD)
    screen.addstr(int(dims[0] - 2), int(dims[1] - 10), "Life:", curses.A_BOLD)

    def get_letter():
        letter_hunt.active_add_letters()
        letter = random.choice(letter_hunt.active_letters)
        return letter.upper()

    def random_column():
        column = random.choice(range(1, dims[1] - 1))
        return column

    def each_letter():
        letter = window.addstr(1, random_column(), get_letter(), curses.A_BOLD)
        return letter

    def move_down():
        current_row = each_letter()
        new_point = window.addstr()
        return new_point

    while gameover > 0:
        # move_down()
        each_letter()
        view.move(row, column)
        row += 1
        curses.panel.update_panels()
        curses.doupdate()
        time.sleep(0.5)
        screen.refresh()
        gameover -= 1
    window.getch()

wrapper(game())
curses.endwin()
