from turtle import Turtle, Screen

if __name__ == '__main__':
    screen = Screen()
    screen.setup(height=500, width=500)
    screen.title('Lango pavadinimas')
    screen.bgcolor('lightblue')
    
    turtle = Turtle()
    turtle.shape('square')
    turtle.color('green')
    turtle.pensize(5)
    turtle.speed(0)
    
    turtle.penup()
    turtle.pu()
    turtle.up()
    
    turtle.pendown()
    turtle.pd()
    turtle.down()
    
    turtle.forward(50)
    turtle.fd(50)
    
    turtle.backward(50)
    turtle.back(50)
    
    turtle.right(90)
    turtle.left(90)
    
    turtle.setheading(270)
    turtle.seth(270)
    
    turtle.goto(-100, 100)
    turtle.setpos(100, -100)
    turtle.setposition(-100, -100)
    
    turtle.teleport(250, 250)
    
    turtle.home()
    
    turtle.teleport(-125, 125)
    
    turtle.stamp()
    
    turtle.teleport(125, -200)
    
    print(turtle.position())
    print(turtle.pos())
    
    print(turtle.heading())
    
    turtle.hideturtle()
    turtle.color('red')
    turtle.forward(100)
    
    turtle.teleport(-125, -125)
    turtle.circle(30)
    input()
    
    