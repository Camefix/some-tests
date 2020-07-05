import pygame
import time

from game_settings.index import game_settings as gs
from graphic_motor.graphic_items import Basic_item

cell_size = gs["battle"].cell_size

cell_switcher = {
    "plain": {"color": gs["color"].plain},
    "forest": {"color": gs["color"].forest},
    "mountain": {"color": gs["color"].mountain},
    "water": {"color": gs["color"].water},
    "sand": {"color": gs["color"].sand},
    "fort": {"color": gs["color"].fort}
}

def cell_to_surface_pos(cell_pos):
    surface_pos_x = (cell_pos[1] + 3.5) * cell_size
    surface_pos_y = (cell_pos[0] + 1.5) * cell_size
    return [surface_pos_x, surface_pos_y]

def cursor_to_map_pos(cursor_pos, map_size):
    map_pos_x = max(min((1 - cursor_pos[1]), 0), 3 - map_size[1]) * cell_size
    map_pos_y = max(min((1 - cursor_pos[0]), 0), 3 - map_size[0]) * cell_size
    print([map_pos_x, map_pos_y])
    return [map_pos_x, map_pos_y]

class Cursor(Basic_item):
    def __init__(self, position):
        super().__init__(pygame.image.load("Graphics\\cursor.png"),
            cell_to_surface_pos(position),
            [0, 0]
        )
        self.grid_position = position

class Cell():
    def __init__(self, type):
        props = cell_switcher[type]
        self.surface = pygame.Surface((cell_size, cell_size))
        self.surface.fill(props["color"])

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
        super().__init__(self.background,
            cursor_to_map_pos(self.cursor.grid_position, (len(self.grid), len(self.grid[0]))),
            [0, 0]
        )
        self.surface.blit(self.cursor.surface, self.cursor.position)
