import pygame


class Ship:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 50
        self.high = 20
        self.prev_x = x
        self.prev_y = y
        self.bombs = 10

    def draw(self, window):
        current_coords = (self.x, self.y, self.width, self.high)
        color = (153, 153, 0)
        pygame.draw.rect(window, color, current_coords)

    def draw_prev(self, window):
        prev_coords = (self.prev_x, self.prev_y, self.width, self.high)
        black = (0, 0, 0)
        pygame.draw.rect(window, black, prev_coords)

