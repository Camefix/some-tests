import pygame
import time

from game_settings.color import grey
from game_settings.display import window_width as width, window_height as height
from graphic_motor.graphic_items import Basic_item

class Title(Basic_item):
    def __init__(self):
        super().__init__(pygame.Surface((width * 0.8, height * 0.4)), [width * 0.1, height * 0.3], [0, 0])
        self.surface.fill(grey)
    
    def pre_update(self):
        delta_time = time.time() - self.time_stamp
        if delta_time > 1 and delta_time <= 1.8:
            self.speed = [0, -2]
        else:
            self.speed = [0, 0]


class Title_button(Basic_item):
    def __init__(self, props, position, has_appeared):
        super().__init__(pygame.Surface((width * 0.2, height * 0.1)), position, [0, 0])
        self.surface.fill(props["color"])
        if not has_appeared:
            self.surface.set_alpha(0)
        self.has_appeared = has_appeared
        self.is_active = has_appeared
    
    def make_visible(self):
        delta_time = time.time() - self.time_stamp
        alpha = int(255 * min((delta_time - 1.3) / (1.8 - 1.3), 1))
        self.surface.set_alpha(alpha)
     
    def pre_update(self):
        if not self.has_appeared:
            self.make_visible()
            if time.time() - self.time_stamp > 1.8:
                self.has_appeared = True
                self.is_active = True
        elif not self.is_active:
            if time.time() - self.time_stamp > 0.33:
                self.is_active = True
                self.speed[0] = 0
        else:
            return 0
