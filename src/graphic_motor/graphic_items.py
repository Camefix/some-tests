class Basic_item():
    def __init__(self, surface, position=[0, 0], speed=[0, 0]):
        self.surface = surface
        self.position = position
        self.speed = speed
    
    def update(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

