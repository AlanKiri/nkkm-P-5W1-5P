from turtle import Turtle
import const

class Snake(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.penup()
        self.teleport(const.adapt_grid(0), const.adapt_grid(0))
        
        self.paths = []
        self.queue = 0
        self.generate_initial_paths()
        
        self.color('green')
        self.turtlesize(const.ENTITY_SIZE, const.ENTITY_SIZE)
        
    def generate_initial_paths(self):
        for x in range(const.STARTING_SNAKE_SIZE, 0, -1):
            self.append_path(const.adapt_grid(0), const.adapt_grid(0 - x * const.GRID_SIZE))
        
    def append_path(self, x, y):
        tail = Turtle(shape='square')
        tail.color('green')
        tail.turtlesize(const.ENTITY_SIZE-0.5, const.ENTITY_SIZE-0.5)
        tail.teleport(x,y)
        self.paths.append(tail)
        
    def sabotage_path(self, path:Turtle):
        path.hideturtle()
        
    def move(self):
        self.append_path(*self.pos())
        if self.queue == 0:
            path_for_removal_index = 0
            self.sabotage_path(self.paths[path_for_removal_index])
            del self.paths[path_for_removal_index]
        else:
            self.queue -= 1
        
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
        


