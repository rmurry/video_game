import pygame
import config                   # config.py file in directory/repo
from game import Game           # game.py file in directory/repo

pygame.init()

screen = pygame.display.set_mode((600,400))

pygame.display.set_caption('Top Scroller')

game = Game(screen)
game.set_up()
while True:
    game.update()
    screen.fill(config.BLACK)
    pygame.display.flip