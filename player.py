import pygame
import config

class Player:
    def __init__(self):
        print("player created")

    def update(self):
        print("player updated")

    def render(self,screen):
        pygame.draw.rect(screen,config.WHITE, (10,10,10,10),4)
