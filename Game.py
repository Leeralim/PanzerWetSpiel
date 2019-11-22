import pygame
import sys
import os
import tkinter
import time
import random
import math

from pygame.locals import *

from block import *
from player import *
from expl import *
from bullet import *
from bars import *
from enemy import *

pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (5,5) 
bg = pygame.image.load("res/bg.png")
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('PanzerShot')
pygame.mouse.set_visible(0)
background = pygame.Surface(screen.get_size())

allsprites = pygame.sprite.Group()

remov = Remov(-20, -20)
remov2 = Remov2(-22, -22)
remov3 = Remov3(-22, -22)

kak = Kak()
allsprites.add(kak)
blocks = pygame.sprite.Group()
booms = pygame.sprite.Group()
boom = Expl(-20,-20)
tp = Tp(-200,-200)
boomm = Expla(-200,-200)

player = Player()
allsprites.add(player)
playerr = PlayerR()
allsprites.add(playerr)
tower = Tower()
allsprites.add(tower)

enemy = Enemy()
allsprites.add(enemy)
enemyr = EnemyR()
allsprites.add(enemyr)
towe = Towe()
allsprites.add(towe)

mec = Mec(999,999)
stmbar = Stmbar()
allsprites.add(stmbar)
stmps = pygame.sprite.Group()
hpbar = Hpbar()
allsprites.add(hpbar)
hpps = pygame.sprite.Group()
mpbar = Mpbar()
allsprites.add(mpbar)
mpps = pygame.sprite.Group()




down = Down()
allsprites.add(down)

bullets = pygame.sprite.Group()
bullet = Bullet(-200,-200, 10)

shoot2 = False
shoot = False
moveenemy = False
beginturn = False
endturn = False
HPEN = 1
HP = 100
MP = 100
STM = 100
u = 600
uu = 0
timer = 0
timerout = random.choice([40,35,30,25,20,15,10,5])
xyenemy = random.choice([2,2,0,-2,-2])
tomer = 0
powepower = 10


for i in range(1280):
    if (u <=590):
        u = 592
    if (u == 600):
        u = random.choice([u-2,u])
    if (u < 600):
        u = random.choice([u-2,u,u+2])
    uu = u
    while (uu<620):
        uu+=2
        block=Block(i,uu)
        blocks.add(block)
pointy = 22
for i in range(9):
    stmp = Stmp(83,pointy)
    stmps.add(stmp)
    allsprites.add(stmp)
    pointy+=10
pointy = 22
for i in range(9):
    mpp = Mpp(53,pointy)
    mpps.add(mpp)
    allsprites.add(mpp)
    pointy+=10
pointy = 22
for i in range(9):
    hpp = Hpp(23,pointy)
    hpps.add(hpp)
    allsprites.add(hpp)
    pointy+=10


clock = pygame.time.Clock()
exit_program = False

def drawScreen():
    pygame.display.update()
    screen.blit(bg, (0, 0))
    
while not exit_program:
    clock.tick(60)
    bullets.draw(screen)  
    drawScreen()
    #tomer+=1
    #if tomer>100:
        #tomer = 0
    #if tomer>5:
        #allsprites.remove(boomm)
        #boomm.kill
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYUP:
            if i.key == K_f:
                if MP>0:
                    MP-=10
                    tp = Tp(tower.rect.x, tower.rect.y)
                    tp.ti = 0
                    allsprites.add(tp)
                    player.rect.x +=40
                    playerr.rect.x +=40
                    tower.rect.x +=40
            if i.key == K_r:
                if MP>0:
                    MP-=10
                    mec = Mec(towe.rect.x+10,towe.rect.y-50)
                    allsprites.add(mec)
            if i.key == K_SPACE:
                if endturn == False:
                    bullet = Bullet(tower.rect.x + 40, tower.rect.y,powepower)
                    bullets.add(bullet)
                    endturn = True
                    powepower = 10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        #print(bullet.power)
        if powepower <60:
            powepower +=2

    
    if keys[pygame.K_g]:
        endturn = True
    if keys[pygame.K_LEFT]:
        STM -=2.5
    elif keys[pygame.K_RIGHT]:
        STM -=2.5
    if endturn == True:
        timer+=1
        if timer <40:
            moveenemy = True
            enemy.rect.x += xyenemy
            enemyr.rect.x += xyenemy
            towe.rect.x +=xyenemy
        elif timer>40:
            bullet = Bullet(towe.rect.x, towe.rect.y,(random.choice([-30,-30,-40,-40,-50,-50,-60,-70])))
            bullets.add(bullet)
            endturn = False
            beginturn = True
            moveenemy = False
            timer = 0
                      
    if beginturn == True:
        remov = Remov(-20, -20)
        pointy = 22
        for i in range(9):
            stmp = Stmp(83,pointy)
            stmps.add(stmp)
            allsprites.add(stmp)
            pointy+=10
        STM = 100
        xyenemy = random.choice([2,2,2,0,-2,-2,-2])
        beginturn = False
        shoot=False
        shoot2=False
        
    if (bullet.rect.y>640):
        bullet.rect.y = 600
    if ((bullet.yy < 0)and(bullet.rect.y>450)):
        bullet.yy = bullet.yy/8
        bullet.xx = bullet.xx/4
        
    if pygame.sprite.groupcollide(bullets, blocks, True, False):
        xxb = bullet.rect.x
        yyb = bullet.rect.y
        boomm.tim = 0
        boomm = Expla(xxb-20,yyb-20)
        allsprites.add(boomm)
        
        boom = Expl(xxb,yyb)
        booms.add(boom)
        allsprites.add(boom)
        allsprites.remove(boom)
        boom = Expl(xxb+5,yyb)
        booms.add(boom)
        allsprites.add(boom)
        allsprites.remove(boom)
        boom = Expl(xxb-5,yyb)
        booms.add(boom)
        allsprites.add(boom)
        allsprites.remove(boom)
        boom = Expl(xxb,yyb+5)
        booms.add(boom)
        allsprites.add(boom)
        allsprites.remove(boom)
        boom = Expl(xxb,yyb-5)
        booms.add(boom)
        allsprites.add(boom)
        allsprites.remove(boom)
        boom = Expl(xxb,yyb-10)
        booms.add(boom)
        allsprites.add(boom)
        allsprites.remove(boom)
        boom = Expl(xxb,yyb+10)
        booms.add(boom)
        allsprites.add(boom)
        allsprites.remove(boom)
        boom = Expl(xxb+10,yyb)
        booms.add(boom)
        allsprites.add(boom)
        allsprites.remove(boom)
        boom = Expl(xxb-10,yyb)
        booms.add(boom)
        allsprites.add(boom)
        allsprites.remove(boom)
        boom = Expl(xxb+5,yyb+5)
        booms.add(boom)
        allsprites.add(boom)
        allsprites.remove(boom)
        boom = Expl(xxb+5,yyb-5)
        booms.add(boom)
        allsprites.add(boom)
        allsprites.remove(boom)
        boom = Expl(xxb-5,yyb+5)
        booms.add(boom)
        allsprites.add(boom)
        allsprites.remove(boom)
        boom = Expl(xxb-5,yyb-5)
        booms.add(boom)
        allsprites.add(boom)
        allsprites.remove(boom)
        

    if HPEN <1:
        enemy.kill()
        enemyr.kill()
        towe.kill()
    if endturn == False:
        player.update(STM)
        playerr.update(STM)
        tower.update(player.rect.y,STM)
    tp.update()
    mec.update()
    boomm.update()
    boom.update()
    enemy.update(STM)
    enemyr.update(STM)
    towe.update(enemy.rect.y,STM)
    bullets.update()
    
    if STM == 90:
        remov = Remov(90,25)
    if STM == 80:
        remov = Remov(90,35)
    if STM == 70:
        remov = Remov(90,45)
    if STM == 60:
        remov = Remov(90,55)
    if STM == 50:
        remov = Remov(90,65)
    if STM == 40:
        remov = Remov(90,75)
    if STM == 30:
        remov = Remov(90,85)
    if STM == 20:
        remov = Remov(90,95)
    if STM == 10:
        remov = Remov(90,105)
    if STM == 0:
        remov = Remov(90,115)
        
    if MP == 90:
        remov3 = Remov3(60,25)
    if MP == 80:
        remov3 = Remov3(60,35)
    if MP == 70:
        remov3 = Remov3(60,45)
    if MP == 60:
        remov3 = Remov3(60,55)
    if MP == 50:
        remov3 = Remov3(60,65)
    if MP == 40:
        remov3 = Remov3(60,75)
    if MP == 30:
        remov3 = Remov3(60,85)
    if MP == 20:
        remov3 = Remov3(60,95)
    if MP == 10:
        remov3 = Remov3(60,105)
    if MP == 0:
        remov3 = Remov3(60,115)
        
    if HP == 90:
        remov2 = Remov2(30,25)
    if HP == 80:
        remov2 = Remov2(30,35)
    if HP == 70:
        remov2 = Remov2(30,45)
    if HP == 60:
        remov2 = Remov2(30,55)
    if HP == 50:
        remov2 = Remov2(30,65)
    if HP == 40:
        remov2 = Remov2(30,75)
    if HP == 30:
        remov2 = Remov2(30,85)
    if HP == 20:
        remov2 = Remov2(30,95)
    if HP == 10:
        remov2 = Remov2(30,105)
    if HP == 0:
        remov2 = Remov2(30,115)

#        
#    if ((bullet.rect.y > 580) and (bullet.rect.y < 600)):
#        bullet.rect.y = 600
#    if bullet.rect.y >599:
#        boom = Expl(bullet.rect.x,bullet.rect.y)
#        allsprites.add(boom)
#    if pygame.sprite.groupcollide(bullets, blocks, True, False):
#        print('fsdfsdfsdf')
#        boom = Expl(bullet.rect.x,bullet.rect.y)
#        allsprites.add(boom)
    
    if (not(pygame.sprite.spritecollide(player, blocks, False))):
        player.rect.y +=2
    if (not(pygame.sprite.spritecollide(playerr, blocks, False))):
        playerr.rect.y +=2
    if (keys[pygame.K_LEFT] and pygame.sprite.spritecollide(player, blocks, False)):
        player.rect.y -=2
        if pygame.sprite.spritecollide(playerr, blocks, False):
            playerr.rect.y -=2
    elif (keys[pygame.K_RIGHT] and pygame.sprite.spritecollide(playerr, blocks, False)):
        playerr.rect.y -=2
        if pygame.sprite.spritecollide(player, blocks, False):
            player.rect.y -=2
            
    if pygame.sprite.spritecollide(kak, bullets, True):
        print('hhehe')
    if (not(pygame.sprite.spritecollide(enemy, blocks, False))):
        enemy.rect.y +=2
    if (not(pygame.sprite.spritecollide(enemyr, blocks, False))):
        enemyr.rect.y +=2
    if (moveenemy == True and pygame.sprite.spritecollide(enemy, blocks, False)):
        enemy.rect.y -=2
        if pygame.sprite.spritecollide(enemyr, blocks, False):
            enemyr.rect.y -=2
    elif (moveenemy == True and pygame.sprite.spritecollide(enemyr, blocks, False)):
        enemyr.rect.y -=2
        if pygame.sprite.spritecollide(enemy, blocks, False):
            enemy.rect.y -=2
            
    if ((pygame.sprite.collide_rect(player, boomm)) or(pygame.sprite.collide_rect(playerr, boomm))or(pygame.sprite.collide_rect(tower, boomm))):
        if shoot==False:
            HP-=10
            shoot = True
    if ((pygame.sprite.collide_rect(enemy, boomm)) or(pygame.sprite.collide_rect(enemyr, boomm))or(pygame.sprite.collide_rect(towe, boomm))):
        if shoot2==False:
            HPEN-=1
            shoot2 = True
    hitbe = pygame.sprite.groupcollide(booms, blocks,True, True)
    if pygame.sprite.collide_rect(mec, towe):
        mec.kill()
        HPEN-=1
    
    if pygame.sprite.spritecollide(remov, stmps, True):
        remov.kill()
    if pygame.sprite.spritecollide(remov3, mpps, True):
        remov3.kill()
    if pygame.sprite.spritecollide(remov2, hpps, True):
        remov2.kill()
        
    for block in hitbe:
        block.kill()
        blocks.remove(block)
        
        
    
    
    allsprites.draw(screen)
    blocks.draw(screen)
    pygame.display.flip()
    

pygame.quit()