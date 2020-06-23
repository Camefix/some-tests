import pygame

from game_settings.display import window_width as width, window_height as height
from graphic_motor.graphic_items import Basic_item

class Title_button(Basic_item):
    def __init__(self, color):
        super().__init__(pygame.Surface((width * 0.2, height * 0.1)), [0, 0], [0, 0])
        self.surface.fill(color)
        self.surface.set_alpha(0)
        self.is_active = False
    
    def make_visible(self, time):
        alpha = int(255 * min((time - 1.3) / (1.8 - 1.3), 1))
        self.surface.set_alpha(alpha)
        if alpha > 250:
            self.is_active = True
