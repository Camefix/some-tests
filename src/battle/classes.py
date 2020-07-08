import pygame
import time

from game_settings.index import game_settings as gs
from graphic_motor.graphic_items import Basic_item

cell_size = gs["battle"].cell_size

cell_switcher = {
    "plain": {},
    "forest": {},
    "mountain": {},
    "water": {},
    "sand": {},
    "fort": {}
}

def cell_to_surface_pos(cell_pos):
    surface_pos_x = (cell_pos[1] + 3.5) * cell_size
    surface_pos_y = (cell_pos[0] + 1.5) * cell_size
    return [surface_pos_x, surface_pos_y]

def cursor_to_map_pos(cursor_pos, map_size):
    map_pos_x = max(min((1 - cursor_pos[1]), 0), 3 - map_size[1]) * cell_size
    map_pos_y = max(min((1 - cursor_pos[0]), 0), 3 - map_size[0]) * cell_size
    return [map_pos_x, map_pos_y]

class Cursor(Basic_item):
    def __init__(self, position):
        self.grid_position = position
        super().__init__(pygame.image.load("Graphics\\cursor.png").convert(),
            cell_to_surface_pos(position),
            [0, 0]
        )
        self.surface.set_colorkey(self.surface.get_at((50, 50)))
        print(self.surface.get_at((50, 50)))
        self.grid_position = position
    
    def pre_update(self):
        self.grid_position[0] = max(0, min(5, self.grid_position[0]))
        self.grid_position[1] = max(0, min(9, self.grid_position[1]))
    
    def update(self):
        self.position = cell_to_surface_pos(self.grid_position)
        

class Cell():
    def __init__(self, type):
        props = cell_switcher[type]

class Map(Basic_item):
    def __init__(self, props):
        self.background = props["background"]
        self.cursor = Cursor(props["init_cursor"])
        self.grid = []
        for row_index in range(len(props["grid"])):
            self.grid.append([])
            for column_index in range(len(props["grid"][row_index])):
                cell_type = props["grid"][row_index][column_index]
                self.grid[-1].append(Cell(cell_type))
        super().__init__(self.background.copy(),
            cursor_to_map_pos(self.cursor.grid_position, (len(self.grid), len(self.grid[0]))),
            [0, 0]
        )
        self.surface.blit(self.cursor.surface, self.cursor.position)
    
    def pre_update(self):
        self.cursor.pre_update()
        target = cursor_to_map_pos(self.cursor.grid_position, (len(self.grid), len(self.grid[0])))
        self.speed[0] = (target[0] - self.position[0]) / 10
        self.speed[1] = (target[1] - self.position[1]) / 10
    
    def update(self):
        self.pre_update()
        self.cursor.update()
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        self.surface = self.background.copy()
        self.surface.blit(self.cursor.surface, self.cursor.position)

    

