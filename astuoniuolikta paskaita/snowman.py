from turtle import Turtle, Screen

RADIUS = 30
DIAMETER = RADIUS * 2

if __name__ == '__main__':
    turtle = Turtle()
    screen = Screen()
    screen.setup(width=500, height=500)
    
    turtle.circle(RADIUS)
    turtle.penup()
    turtle.sety(-abs(DIAMETER*1.5))
    turtle.pendown()
    turtle.circle(RADIUS*1.5)
    turtle.penup()
    turtle.sety(-abs(DIAMETER*1.5 + DIAMETER*2))
    turtle.pendown()
    turtle.circle(RADIUS*2)
    input()
    
    