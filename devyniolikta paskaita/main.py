from turtle import Turtle, Screen

SIZE = 500

maz_x = -abs(SIZE/2)
max_x = SIZE/2


if __name__ == '__main__':
    turtle_1 = Turtle()
    turtle_2 = Turtle()
    turtle_3 = Turtle()
    turtle_4 = Turtle()
    
    screen = Screen()
    screen.setup(SIZE, SIZE)
    
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4]
    
    for index, turtle in enumerate(turtles):
        index = index + 1
        if index % 2 == 0:
            turtle.teleport(-abs(index*90))
        else:
            turtle.teleport(index * 90)
            
    input()
        