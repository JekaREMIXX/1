from pygame import *
import random
from time import time as t
font.init()

font=font.SysFont('Arial', 40)
window = display.set_mode((700,500))
display.set_caption("pygame window")
background =transform.scale(image.load("fon.png"), (700,500))
class GameSprite(sprite.Sprite):
    def __init__(self,rocket,x1,y1,speed):
        super().__init__()
        self.image = 1
        self.speed = 1
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x >5:
            self.rect.x -=10
        if keys_pressed[K_RIGHT] and self.rect.x <600:
            self.rect.x +=10
    def fire(self):
        bullet1= Bullet(bullet, self.rect.centerx,self.rect.top,-15)
        bullets.add(bullet1)
game=True
finish=False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    display.update()
