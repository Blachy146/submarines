import pygame


class Ship:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 50
        self.high = 50
        self.bombs = 10
        self.ship_image = pygame.image.load("/home/bmalecki/Downloads/ship.png")
        self.ship_image = pygame.transform.scale(self.ship_image, (self.width, self.high))

    def draw(self, window):
        window.blit(self.ship_image, (self.x, self.y))

