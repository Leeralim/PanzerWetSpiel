import pygame
class Remov(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Remov2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Remov3(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Hpbar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("res/hpbar.png")
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load("res/block.png")
        #self.rect = self.image.get_rect()
        self.rect.x = 21
        self.rect.y = 20
class Hpp(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("res/hpp.png")
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load("res/block.png")
        #self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Mpbar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("res/mpbar.png")
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load("res/block.png")
        #self.rect = self.image.get_rect()
        self.rect.x = 51
        self.rect.y = 20
class Mpp(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("res/mpp.png")
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load("res/block.png")
        #self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Stmbar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("res/stmbar.png")
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load("res/block.png")
        #self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 20
class Stmp(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("res/stmp.png")
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load("res/block.png")
        #self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y