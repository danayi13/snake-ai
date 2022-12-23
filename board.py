import pygame

import food
import snake

# TODO get better colors
BACKGROUND_COLOR = (0, 0, 0)
GRID_LINE_COLOR = (255, 255, 255)

class Board:

    height = None
    width = None

    def __init__(self, height: int=20, width: int=20):
        self.height = height
        self.width = width

    def draw_board(self, screen: pygame.Surface) -> None:
        # Board Outline - Scale to Grid Size
        window_height = screen.get_height()
        window_width = screen.get_width()

        square_side = min((window_height * 0.8 / self.height) * 0.95, (window_width * 0.8 / self.width))
        top_padding = (window_height * 0.8 - square_side * self.height) / 2.0 + window_height * 0.2
        side_padding = (window_width - square_side * self.width) / 2.0
        board_height = square_side * self.height
        board_width = square_side * self.width

        pygame.draw.rect(screen, BACKGROUND_COLOR, [side_padding, top_padding, board_width, board_height])

        # Gridlines
        line_top = side_padding + square_side
        for _ in range(self.width - 1):
            pygame.draw.line(screen, GRID_LINE_COLOR, (line_top, top_padding), (line_top, top_padding + board_height))
            line_top += square_side
        line_left = top_padding + square_side
        for _ in range(self.height - 1):
            pygame.draw.line(screen, GRID_LINE_COLOR, (side_padding, line_left), (side_padding + board_width, line_left))
            line_left += square_side
