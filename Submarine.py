import pygame


class Submarine:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 50
        self.high = 30
        self.bombs = 10
        self.submarine_image = pygame.image.load("/home/bmalecki/Downloads/submarine.png")
        self.submarine_image = pygame.transform.scale(self.submarine_image, (self.width, self.high))
        self. right_move = True

    def draw(self, window):
        window.blit(self.submarine_image, (self.x, self.y))
