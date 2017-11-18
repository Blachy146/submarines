import pygame
import pygame.locals
import time
import sys
import Ship
import Bomb
import Configuration


def draw_sea_water(window, configuration, ship):
    coords = (0, configuration.ship_y+ship.high*0.70, configuration.window_width, configuration.window_high)
    color = (0, 0, 110)
    pygame.draw.rect(window, color, coords)


def displayNumberOfAvailableBombs(window, ship):
    font = pygame.font.Font(None, 30)
    text = font.render("Bombs: {0}".format(ship.bombs), True, (255, 255, 0))
    prev_text = font.render("Bombs: {0}".format(ship.bombs+1), True, (0, 0, 0))
    window.blit(prev_text, (10, 10))
    window.blit(text, (10, 10))


def init_and_create_window(configuration):
    pygame.init()
    pygame.display.set_caption("Submarines")
    return pygame.display.set_mode((configuration.window_high, configuration.window_width))


configuration = Configuration.Configuration()
window = init_and_create_window(configuration)
background_image = pygame.image.load('/home/bmalecki/Downloads/clouds2.jpg')

move_left = False
move_right = False
ship = Ship.Ship(configuration.ship_x, configuration.ship_y)
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
                if ship.bombs > 0:
                    bombs.append(Bomb.Bomb(ship.x, ship.y+5))
                    ship.bombs -= 1
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

    bombs = [bomb for bomb in bombs if bomb.y < configuration.window_high+5]

    ship.draw_prev(window)
    window.blit(background_image, (0, 0))
    draw_sea_water(window, configuration, ship)

    for bomb in bombs:
        bomb.prev_y = bomb.y
        bomb.y += configuration.bomb_coord_increase
        bomb.draw(window)

    ship.draw(window)
    displayNumberOfAvailableBombs(window, ship)
    pygame.display.update()

