import pygame
import math
import tkinter


class Bullet(pygame.sprite.Sprite):
    power = 10
    temer = 3
    xx = 1
    yy = (-1)*(temer*temer)+14*temer
    def __init__(self, x, y,power):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((250,0,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.power = power
        

    def update(self):
        #print(self.rect.x,self.rect.y)
        self.temer +=1
        self.rect.x += self.xx
        self.rect.y -= self.yy
        self.xx = self.power
        self.yy = (-1)*(self.temer*self.temer)+14*self.temer
class Mec(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/mech.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

    def update(self):

        self.rect.x += 0
        self.rect.y += 1

