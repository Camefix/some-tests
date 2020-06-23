import time

class Basic_item():
    def __init__(self, surface, position, speed):
        self.surface = surface
        self.position = position
        self.speed = speed
        self.time_stamp = time.time()
    
    def pre_update(self):
        return(0)
    
    def update(self):
        self.pre_update()
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

