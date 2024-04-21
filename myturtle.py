import turtle
tr = turtle.Turtle()

def olympics_logo(color, x, y):
    tr.pensize(5)
    tr.color(color)
    tr.penup()
    tr.goto(x, y)
    tr.pendown()
    tr.circle(45)

olympics_logo("blue", -110, -25) 
olympics_logo("black", 0, -25) 
olympics_logo("green", 110, -25)
olympics_logo("yellow", -55, -75)
olympics_logo("red", 55, -75)    