import pygame

# TODO get better color
FOOD_COLOR = (200, 200, 200)

class Food:

    height_coor = None
    length_coor = None

    def __init__(self, height_coor: int, length_coor: int):
        self.height_coor = height_coor
        self.length_coor = length_coor

    def draw_food(self, screen: pygame.Surface) -> None:
        pass
