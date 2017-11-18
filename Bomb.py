import pygame


class Bomb:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 25
        self.high = 25
        self.barrel_image = pygame.image.load("/home/bmalecki/Downloads/barrel.png")
        self.barrel_image = pygame.transform.rotate(self.barrel_image, 35)
        self.barrel_image = pygame.transform.scale(self.barrel_image, (self.width, self.high))

    def draw(self, window):
        window.blit(self.barrel_image, (self.x, self.y))

