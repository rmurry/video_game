import pygame
import config

class Player:
    def __init__(self,x_pos,y_pos):
        print("player created")
        self.position = [x_pos,y_pos]
        self.image = pygame.image.load("imgs/player.png")
        self.image = pygame.transform.scale(self.image,(config.SCALE,config.SCALE))
        self.rect = pygame.Rect(self.position[0]*config.SCALE,self.position[1]*config.SCALE,config.SCALE,config.SCALE)

    def update(self):
        print("player updated")

    def update_position(self,new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]
        

    def render(self,screen,camera):
        self.rect = pygame.Rect(self.position[0]*config.SCALE,self.position[1]*config.SCALE - (camera[1] * config.SCALE),config.SCALE,config.SCALE) 
        screen.blit(self.image,self.rect)
        #pygame.draw.rect(screen,config.WHITE, (self.position[0]*config.SCALE,self.position[1]*config.SCALE,config.SCALE,config.SCALE),4)