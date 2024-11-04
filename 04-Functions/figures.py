import turtle


def draw_square(length):
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(5)

    for i in range(4):
        pen.forward(length)
        pen.right(90)

    pen.hideturtle()
    window.mainloop()

def draw_trangle(length):
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(5)

    for i in range (3):
        pen.forward(length)
        pen.left(120)
    
    pen.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    length = 100
    draw_trangle(length)