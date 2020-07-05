import pygame
import time

from game_settings.index import game_settings as gs
from graphic_motor.graphic_items import Basic_item

grey = gs["color"].grey
title_width = gs["title_screen"].title_width
title_height = gs["title_screen"].title_height
time_start_appear = gs["title_screen"].time_start_appear
time_end_intro = gs["title_screen"].time_end_intro

class Title(Basic_item):
    def __init__(self):
        super().__init__(pygame.Surface((title_width, title_height)), 
            [gs["title_screen"].title_left, gs["title_screen"].title_top], 
            [0, 0]
        )
        self.surface.fill(grey)
        self.add_centered_text(gs["font"].title_font, "Title")
    
    def pre_update(self):
        delta_time = time.time() - self.time_stamp
        if delta_time > gs["title_screen"].time_end_standstill and delta_time <= time_end_intro:
            self.speed = gs["title_screen"].title_speed
        else:
            self.speed = [0, 0]


class Title_button(Basic_item):
    def __init__(self, props, position, has_appeared):
        super().__init__(pygame.Surface((gs["title_screen"].button_width, gs["title_screen"].button_height)), position, [0, 0])
        self.surface.fill(props["color"])
        self.add_centered_text(gs["font"].button_font, props["label"])
        if not has_appeared:
            self.surface.set_alpha(0)
        self.has_appeared = has_appeared
        self.is_active = has_appeared
        self.effect = props["effect"]
    
    def make_visible(self):
        delta_time = time.time() - self.time_stamp
        alpha = int(255 * min((delta_time - time_start_appear) / (time_end_intro - time_start_appear), 1))
        self.surface.set_alpha(alpha)
     
    def pre_update(self):
        if not self.has_appeared:
            self.make_visible()
            if time.time() - self.time_stamp > time_end_intro:
                self.has_appeared = True
                self.is_active = True
        elif not self.is_active:
            if time.time() - self.time_stamp > gs["title_screen"].time_move:
                self.is_active = True
                self.speed[0] = 0
        else:
            return 0

