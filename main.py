import pygame
import pygame.locals
import time
import sys
import Ship
import Bomb
import Configuration
import Submarine


def draw_sea_water(window, configuration, ship):
    coords = (0, configuration.ship_y+ship.high*0.80, configuration.window_width, configuration.window_high)
    color = (20, 40, 250)
    pygame.draw.rect(window, color, coords)


def displayNumberOfAvailableBombs(window, ship):
    font = pygame.font.Font(None, 30)
    text = font.render("Bombs: {0}".format(ship.bombs), True, (255, 255, 0))
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
ship_image_left = False
ship = Ship.Ship(configuration.ship_x, configuration.ship_y)
bombs = []
submarines = []

submarines.append(Submarine.Submarine(200, 500))

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
                    bombs.append(Bomb.Bomb(ship.x+int(ship.width/2), ship.y+45))
                    ship.bombs -= 1
        if event.type == pygame.locals.KEYUP:
            if event.key == pygame.locals.K_LEFT:
                move_left = False
            elif event.key == pygame.locals.K_RIGHT:
                move_right = False
    if move_left:
        if ship.x >= 0:
            if not ship_image_left:
                ship.ship_image = pygame.transform.flip(ship.ship_image, True, False)
                ship_image_left = True
            ship.x -= configuration.ship_coord_increase
    elif move_right:
        if ship.x + ship.width <= configuration.window_width:
            if ship_image_left:
                ship.ship_image = pygame.transform.flip(ship.ship_image, True, False)
                ship_image_left = False
            ship.x += configuration.ship_coord_increase

    bombs = [bomb for bomb in bombs if bomb.y < configuration.window_high+5]

    window.blit(background_image, (0, 0))
    draw_sea_water(window, configuration, ship)

    for bomb in bombs:
        bomb.y += configuration.bomb_coord_increase
        bomb.draw(window)

    for submarine in submarines:
        if submarine.x < 0:
            submarine.right_move = True
            submarine.submarine_image = pygame.transform.flip(submarine.submarine_image, True, False)
        elif submarine.x+submarine.width > configuration.window_width:
            submarine.right_move = False
            submarine.submarine_image = pygame.transform.flip(submarine.submarine_image, True, False)
        if submarine.right_move:
            submarine.x += configuration.submarine_increase
            submarine.draw(window)
        elif not submarine.right_move:
            submarine.x -= configuration.submarine_increase
            submarine.draw(window)


    ship.draw(window)
    displayNumberOfAvailableBombs(window, ship)
    pygame.display.update()

