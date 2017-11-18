import pygame
import pygame.locals
import time
import sys
import os
import Ship
import Bomb


def init_and_create_window():
    pygame.init()
    return pygame.display.set_mode((640, 640))


def draw_circle(window, x, y, radius):
    pygame.draw.circle(window, (255, 255, 255), (x, y), radius, 2)


window = init_and_create_window()

ship = Ship.Ship(300, 300)

move_left = False
move_right = False

bombs = []

while True:
    time.sleep(0.03)
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            sys.exit(0)
        if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_LEFT:
                move_left = True
            elif event.key == pygame.locals.K_RIGHT:
                move_right = True
            elif event.key == pygame.locals.K_SPACE:
                bombs.append(Bomb.Bomb(ship.x, ship.y+5))
        if event.type == pygame.locals.KEYUP:
            if event.key == pygame.locals.K_LEFT:
                move_left = False
            elif event.key == pygame.locals.K_RIGHT:
                move_right = False
    if move_left:
        ship.prev_x = ship.x
        ship.x -= 10
    elif move_right:
        ship.prev_x = ship.x
        ship.x += 10

    bombs = [bomb for bomb in bombs if bomb.y < 641]

    for bomb in bombs:
        bomb.prev_y = bomb.y
        bomb.y += 1
        bomb.draw(window)

    ship.draw(window)
    pygame.display.update()

