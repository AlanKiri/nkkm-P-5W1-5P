from turtle import Turtle
import const

class Snake(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.penup()
        self.teleport(const.adapt_grid(0), const.adapt_grid(0))
        self.paths = []
        self.queue = 0
        self.color('green')
        self.turtlesize(const.ENTITY_SIZE, const.ENTITY_SIZE)
        
    def move(self):
        self.forward(const.GRID_SIZE)
        
    def can_rotate(self, move):
        if move == self.heading() or move == self.heading() + 180:
            return False
        else:
            return True
        
    def rotate_right(self):
        if not self.can_rotate(360):
            return
        self.seth(360)
    
    def rotate_bottom(self):
        if not self.can_rotate(270):
            return
        self.seth(270)
        
    def rotate_left(self):
        if not self.can_rotate(180):
            return
        self.seth(180)
        
    def rotate_top(self):
        if not self.can_rotate(90):
            return
        self.seth(90)
        


