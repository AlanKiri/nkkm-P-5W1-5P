from turtle import Turtle, Screen
from random import randint
from sys import exit

HEIGHT = 200
WIDTH = 400
MAX_MOVE = 5
OFFSET = 20

def setup_turtle(num):
    turtle = Turtle()
    turtle.teleport(-abs(WIDTH/2) + OFFSET, HEIGHT/4-num*OFFSET)
    return turtle

if __name__ == '__main__':
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    
    turtle_1 = setup_turtle(1)
    turtle_2 = setup_turtle(2)
    turtle_3 = setup_turtle(3)
    turtle_4 = setup_turtle(4)
    
    turtles_array = (turtle_1, turtle_2, turtle_3, turtle_4)
    
#   [] = () 

    while True:
        for turtle in turtles_array:
            turtle.forward(randint(0, MAX_MOVE))
            x, y = turtle.pos()
            if x >= WIDTH/2-OFFSET:
                input()
                exit()
