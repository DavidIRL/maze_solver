from window import Window
from maze import Maze
import sys


def main():
    num_rows = 14
    num_cols = 16
    margin = 40
    screen_x = 1000
    screen_y = 800
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(5000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("maze has been created")

    is_solveable = maze.solve()
    if not is_solveable:
        print("the created maze cannot be solved")
    else:
        print("maze solved!")

    win.wait_for_close()


main()
