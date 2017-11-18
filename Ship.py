import pygame


class Ship:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 50
        self.high = 20
        self.prev_x = x
        self.prev_y = x

    def draw(self, window):
        current_coords = (self.x, self.y, self.width, self.high)
        prev_coords = (self.prev_x, self.prev_y, self.width, self.high)
        grey = (100, 100, 100)
        black = (0, 0, 0)
        pygame.draw.rect(window, black, prev_coords)
        pygame.draw.rect(window, grey, current_coords)

