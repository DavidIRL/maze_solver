from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("The Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="black", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.running = False


    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas, fill_color)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_to_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Maze Window Closed")


    def close(self):
        self.running = False


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y


class Line:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def draw(self, canvas, fill_color="white"):
        canvas.create_line(
            self.p1._x, self.p1._y, self.p2._x, self.p2._y, fill=fill_color, width=2
        )


