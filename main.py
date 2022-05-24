from pygame import *
from random import randint



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))





class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(0, 700-80)
            lost += 1





class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.right<win_width:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, 5)
        bullets.add(bullet)   



#сцена
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")
background = (200, 200, 255)
window.fill(background)

#игровые переменные
game = True
finish = False
clock = time.Clock()
FPS = 120
lost = 0
shot_down = 0





#игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

            

    if not finish:
        window.fill(background)

    

    display.update()
    clock.tick(FPS)
