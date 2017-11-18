import pygame


class Bomb:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 50
        self.high = 20
        self.prev_x = x
        self.prev_y = y

    def draw(self, window):
        current_coords = (self.x, self.y)
        prev_coords = (self.prev_x, self.prev_y)
        radius = 5
        red = (240, 15, 20)
        black = (0, 0, 0)
        pygame.draw.circle(window, black, prev_coords, radius)
        pygame.draw.circle(window, red, current_coords, radius)

