import time
import curses

#initial conditions

i_s_x = 3         # m
i_s_y = 3       # m

i_v_x = 40         # m/s
i_v_y = 80         # m/s

i_a_x = 0        # m/s**2
i_a_y = 10       # m/s**2

d = 0.95

#introduction

def intro():

    global i_s_x, i_s_y, i_v_x, i_v_y, i_a_x, i_a_y, d

    print("Ball Simulator:")
    print("- Ball (O) moves inside the field (# = border)")
    print("- Bounces off walls, speed slightly damped or amplified")
    print("- Field adapts to terminal size")
    print("- If it crashes, resize your terminal a bit (best fullscreen and zoomed out a bit) and try again")
    print("- Press Enter to start or the letter x to edit the initial conditions")
    print("- Press any key to stop the simulation")
    choice = input().lower()

    if choice == "x":

        i_s_x = int(input("init. position x (m): ")) 
        i_s_y = int(input("init. position y (m): "))
        i_v_x = int(input("init. velocity x (m/s): "))
        i_v_y = int(input("init. velocity y (m/s): "))
        i_a_x = int(input("init. acceleration x (m/s²): "))
        i_a_y = int(input("init. acceleration y (m/s²): "))
        d     = float(input("damping factor (0.9 - 1.1): "))
    else:
        pass

#display field

def display(stdscr):
    global i_s_x, i_s_y

    max_y, max_x = stdscr.getmaxyx()

    if max_y < 35 or max_x < 60:
        stdscr.clear()
        stdscr.addstr(0, 0, "Terminal zu klein!")
        stdscr.refresh()
        return

    field_height = max_y - 2
    field_length = (max_x - 2) // 2 - 1

    x = int(round(i_s_x))
    y = int(round(i_s_y))

    x = min(max(x, 0), field_length - 1)
    y = min(max(y, 0), field_height - 1)

    stdscr.clear()

    for h in range(field_height + 2):
        for l in range(field_length + 2):
            if h == 0 or h == field_height + 1 or l == 0 or l == field_length + 1:
                char = "#"
                if l * 2 + 1 < max_x:
                    stdscr.addstr(h, l * 2, char * 2)
            elif h == y + 1 and l == x + 1:
                if l * 2 < max_x:
                    stdscr.addch(h, l * 2, "O")  # Ball nur einmal
            else:
                char = " "
                if l * 2 + 1 < max_x:
                    stdscr.addstr(h, l * 2, char * 2)

    stdscr.refresh()
    

#incremental calc. of conditions

def calc_pos(stdscr):
    global i_s_x, i_s_y, i_v_x, i_v_y, i_a_x, i_a_y
    t = 0.008
    stdscr.nodelay(True)
    while True:
        
        max_y, max_x = stdscr.getmaxyx()
        field_height = max_y - 2
        field_length = (max_x - 2) // 2

        
        i_s_x += i_v_x * t + 0.5 * i_a_x * t**2
        i_s_y += i_v_y * t + 0.5 * i_a_y * t**2

        i_v_x += i_a_x * t
        i_v_y += i_a_y * t

        
        if i_s_x <= 0:
            i_s_x = 0
            i_v_x = -i_v_x*d
        elif i_s_x >= field_length - 1:
            i_s_x = field_length - 1
            i_v_x = -i_v_x*d

        if i_s_y <= 0:
            i_s_y = 0
            i_v_y = -i_v_y*d
        elif i_s_y >= field_height - 1:
            i_s_y = field_height - 1
            i_v_y = -i_v_y*d

        
        display(stdscr)
        time.sleep(t)
        key = stdscr.getch()
        if key != -1:  # irgendeine Taste gedrückt
            break

intro()
curses.wrapper(calc_pos)






