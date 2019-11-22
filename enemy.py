import pygame
import math


class Towe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("res/towe.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = 570
        
 
    def update(self,y,STM):
        image = pygame.transform.rotate(self.image, 2)
        keys = pygame.key.get_pressed()
        self.rect.y = y - 10
        if self.rect.x > 1234:
            self.rect.x = 1234
        if self.rect.x < 624:
            self.rect.x = 624

class EnemyR(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("res/tan.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1098
        self.rect.y = 570
 
    def update(self,STM):
        image = pygame.transform.rotate(self.image, 2)
        keys = pygame.key.get_pressed()
        if self.rect.x > 1232:
            self.rect.x = 1232
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > 652:
            self.rect.y = 652

        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("res/tan2.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1122
        self.rect.y = 570
 
    def update(self,STM):
        image = pygame.transform.rotate(self.image, 2)
        keys = pygame.key.get_pressed()
        if self.rect.x > 1256:
            self.rect.x = 1256
        if self.rect.x < 24:
            self.rect.x = 24
        if self.rect.y > 628:
            self.rect.y = 628
