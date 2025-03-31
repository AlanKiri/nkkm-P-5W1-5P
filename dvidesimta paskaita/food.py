from turtle import Turtle
from random import randint
import const

class Food(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.hideturtle()
        self.turtlesize(const.ENTITY_SIZE, const.ENTITY_SIZE)
        self.pensize(25)
        
        x = const.adapt_grid((randint(*const.X) // const.GRID_SIZE) * const.GRID_SIZE)
        
        y = const.adapt_grid((randint(*const.Y) // const.GRID_SIZE) * const.GRID_SIZE)
        
        self.teleport(x, y)
        
    def render(self):
        self.stamp()
        
    def sabotage(self):
        self.clearstamps()
        
        