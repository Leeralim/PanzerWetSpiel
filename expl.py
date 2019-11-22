import pygame

class Expl(pygame.sprite.Sprite):
    timm = 0
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((250,0,150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        print(self.timm)
        self.timm+=1
        if self.timm>4:
            self.kill()
            self.timm = 0
class Expla(pygame.sprite.Sprite):
    tim = 0
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/expl.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.tim+=1
        if self.tim>5:
            self.kill()
            self.tim = 0
class Tp(pygame.sprite.Sprite):
    ti = 0
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/tp.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        print(self.ti)
        self.ti+=1
        if self.ti>3:
            self.kill()
            self.ti = 0
        