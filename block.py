import pygame

class Down(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((1280, 100))
            self.image.fill((0,0,0))
            self.rect = self.image.get_rect()
        #self.image = pygame.image.load("res/block.png")
        #self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 620
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2, 2))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load("res/block.png")
        #self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Kak(pygame.sprite.Sprite):
    def __init__(self,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/kaktus.png")
        self.rect = self.image.get_rect()

        self.rect.x = 520
        self.rect.y = 320
