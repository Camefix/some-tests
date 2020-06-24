import time
from game_settings.index import game_settings as gs

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
    
    def add_centered_text(self, font, text):
        text_surface = font.render(text, True, gs["color"].black, gs["color"].white)
        text_surface.set_colorkey(gs["color"].white)
        text_rect = text_surface.get_rect()
        base_rect = self.surface.get_rect()
        text_rect.center = base_rect.center
        self.surface.blit(text_surface, text_rect)

