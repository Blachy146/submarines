import pygame
import pygame.locals
import time
import sys
import Ship
import Bomb
import Configuration


def init_and_create_window(configuration):
    pygame.init()
    return pygame.display.set_mode((configuration.window_high, configuration.window_width))


configuration = Configuration.Configuration()
window = init_and_create_window(configuration)

move_left = False
move_right = False
ship = Ship.Ship(300, 300)
bombs = []

while True:
    time.sleep(configuration.sleep_time)
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
        ship.x -= configuration.ship_coord_increase
    elif move_right:
        ship.prev_x = ship.x
        ship.x += configuration.ship_coord_increase

    bombs = [bomb for bomb in bombs if bomb.y < configuration.window_high+1]

    for bomb in bombs:
        bomb.prev_y = bomb.y
        bomb.y += configuration.bomb_coord_increase
        bomb.draw(window)

    ship.draw(window)
    pygame.display.update()

