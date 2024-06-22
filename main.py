from window import window
from maze import maze


def main():
    num_rows = 14
    num_cols = 16
    margin = 40
    screen_x = 1000
    screen_y = 800
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
