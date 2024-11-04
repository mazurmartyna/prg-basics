import turtle
import figures

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)  

length = 100

figures.draw_square(length)

pen.penup()
pen.goto(0, 0)
pen.pendown()

figures.draw_trangle(length)

pen.hideturtle()
window.mainloop()