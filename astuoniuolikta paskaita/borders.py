from turtle import Turtle, Screen

if __name__ == '__main__':
    screen= Screen()
    screen.setup(width=500, height=500)
    turtle = Turtle()
    turtle.pensize(10)
    
    # Kaire virsutine
    turtle.teleport(-250, 250)
    turtle.seth(305)
    turtle.forward(150)
    
    # Desine virsutine
    turtle.teleport(250, 250)
    turtle.seth(225)
    turtle.forward(150)
    
    # Kaire apatine
    turtle.teleport(-250, -250)
    turtle.seth(45)
    turtle.forward(150)
    
    # Desine apatine
    turtle.teleport(250, -250)
    turtle.seth(135)
    turtle.forward(150)
    
    input()