from window import Window, Point, Line
from maze import Cell

def main():
    win = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    line1 = Line(p1, p2)
    win.draw_line(line1, "black")

    cell_1 = Cell(win)
    cell_1.draw(50, 50, 100, 100)
    cell_1.draw(200, 200, 500, 500)
    cell_1.has_left_wall = False
    cell_1.draw(300, 300, 400, 400)
    cell_1.has_left_wall = True
    cell_1.has_bottom_wall = False
    cell_1.draw(150, 200, 200, 150)

    win.wait_for_close()

main()