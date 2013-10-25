import curses
from time import sleep

class Menu:
    def __init__(self, choices):
        self.screen = curses.initscr()
        self.choices = choices
        self.position = 1
        self.length = len(choices)

        

        curses.start_color()
        curses.init_pair(1,curses.COLOR_RED, curses.COLOR_WHITE)
        self.h = curses.color_pair(1)

        curses.noecho()
        curses.curs_set(0)

    def display(self):
        self.screen.clear()
        line = 1
        
        for choice in self.choices:
            outstring = str(line) + ' - ' + choice
            self.screen.addstr(line,2, outstring,self.h)
            line += 1

        self.screen.refresh()
        self.select()

    def select(self):
        pos = self.position
        
        x = self.screen.getch()

        if x == 258:
            if pos == 1:
                pos = 2
            elif pos == 2:
                pos = 1
        elif x == 259:
            if pos == 1:
                pos = 2
            elif pos == 2:
                pos = 1

        elif x == ord('q'):
            self.screen.addstr(4,8, "Quitting")
            self.screen.refresh()
            sleep(1)
            curses.endwin()
            
        
        else:
            self.screen.addstr(5,8, "Invalid Key!")
            self.screen.refresh()
            sleep(1)
            
        return x
