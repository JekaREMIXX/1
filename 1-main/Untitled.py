from pygame import *
import random
from time import time as t
font.init()

font=font.SysFont('Arial', 40)
window = display.set_mode((700,500))
display.set_caption("pygame window")
background =transform.scale(image.load("fon.png"), (700,500))
player1 =transform.scale(image.load("rocket1.png"), (10,90))
player2 =transform.scale(image.load("rocket2.png"), (10,90))
ball =transform.scale(image.load("ball2.png"), (50,110))

x1=40
y1=random.randint(10,350)
x2=650
y2=random.randint(10,350)
x3=1
y3=1
speed=1
speed_player=1
class GameSprite(sprite.Sprite):
    def __init__(self,player1,x1,y1,speed):
        super().__init__()
        self.image = player1
        self.speed = 1
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >5:
            self.rect.y -=5
        if keys_pressed[K_DOWN] and self.rect.y <405:
            self.rect.y +=5
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >5:
            self.rect.y -=5
        if keys_pressed[K_s] and self.rect.y <405:
            self.rect.y +=5

direction="right"
lost=0
class Ball(GameSprite):
    def update(self):
        global direction
        speed=2
        if direction=="right":
            self.rect.x +=random.randint(1,5)
        if self.rect.x>700:
            lost=lost+1
            self.rect.x =0
            self.rect.x = random.randint(10,600)
clock = time.Clock()
FPS = 60
finishlose=font.render("YOU LOSE", 1, (255, 0, 0))
gamesprite1 = Player1(player1,x1,y1,speed)
gamesprite2 = Player2(player2,x2,y2,speed)
gamesprite3 = Ball(ball,x2,y2,speed)
game=True
finish=False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    gamesprite1.reset()
    gamesprite1.update()
    gamesprite2.reset()
    gamesprite2.update()
    gamesprite3.reset()
    gamesprite3.update()
    if lost>1 or sprite.collide_rect(gamesprite1, gamesprite3):
            window.blit(finishlose,(300, 300))
            finish = True
    display.update()
