from window import Window, Point, Line

win = Window(800, 600)
p1 = Point(100, 100)
p2 = Point(200, 200)
line1 = Line(p1, p2)
win.draw_line(line1, "black")
win.wait_for_close()