from window import Point, Line
class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None

        self.__win = win

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            p1 = Point(x1, y1)
            p2 = Point(x1, y2)
            line = Line(p1, p2)
            self.__win.draw_line(line)
        if self.has_right_wall:
            p1 = Point(x2, y1)
            p2 = Point(x2, y2)
            line = Line(p1, p2)
            self.__win.draw_line(line)
        if self.has_top_wall:
            p1 = Point(x1, y2)
            p2 = Point(x2, y2)
            line = Line(p1, p2)
            self.__win.draw_line(line)
        if self.has_bottom_wall:
            p1 = Point(x1, y1)
            p2 = Point(x2, y1)
            line = Line(p1, p2)
            self.__win.draw_line(line)
