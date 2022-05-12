import pygame
import config                       # config.py file in directory/repo
from game import Game               # game.py file in directory/repo
from game_state import GameState    # game_state.py file in directory/repo

pygame.init()

screen = pygame.display.set_mode((600,400))

pygame.display.set_caption('Top Scroller')


clock = pygame.time.Clock()         #adds framerate to the game
game = Game(screen)
game.set_up()

while game.game_state == GameState.RUNNING:
    clock.tick(60)
    game.update()
    screen.fill(config.BLACK)
    pygame.display.flip()