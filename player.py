import pygame
import config

class Player:
    def __init__(self,x_pos,y_pos):
        print("player created")
        self.position = [x_pos,y_pos]

    def update(self):
        print("player updated")

    def update_position(self,x_change,y_change):
        self.position[0] += x_change
        self.position[1] += y_change

    def render(self,screen):
        pygame.draw.rect(screen,config.WHITE, (self.position[0]*config.SCALE,self.position[1]*config.SCALE,config.SCALE,config.SCALE),4)