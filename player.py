import pygame
import math


class Tower(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("res/tower.png")
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load("res/block.png")
        #self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 570
        
 
    def update(self,y,STM):
        image = pygame.transform.rotate(self.image, 2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if (STM > 0):
                self.rect.x -=3
                lastMove = "left"
        elif keys[pygame.K_RIGHT]:
            if (STM > 0):
                self.rect.x +=3
                lastMove = "right"
        self.rect.y = y - 10
        if self.rect.x > 544:
            self.rect.x = 544
        if self.rect.x < 2:
            self.rect.x = 2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("res/tank.png")
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load("res/block.png")
        #self.rect = self.image.get_rect()
        self.rect.x = 98
        self.rect.y = 570
 
    def update(self,STM):
        image = pygame.transform.rotate(self.image, 2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if (STM > 0):
                self.rect.x -=3
        elif keys[pygame.K_RIGHT]:
            if (STM > 0):
                self.rect.x +=3
        if self.rect.x > 540:
            self.rect.x = 540
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > 600:
            self.rect.y = 600

        
class PlayerR(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("res/tank2.png")
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load("res/block.png")
        #self.rect = self.image.get_rect()
        self.rect.x = 122
        self.rect.y = 570
 
    def update(self,STM):
        image = pygame.transform.rotate(self.image, 2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if (STM > 0):
                self.rect.x -=3
        elif keys[pygame.K_RIGHT]:
            if (STM > 0):
                self.rect.x +=3
        if self.rect.x > 564:
            self.rect.x = 564
        if self.rect.x < 24:
            self.rect.x = 24
        if self.rect.y > 600:
            self.rect.y = 600


        