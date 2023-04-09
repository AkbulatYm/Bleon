from pygame import *
display.set_caption('Блеон VS Скала')
window = display.set_mode((700, 500))
win_width = 700

back = transform.scale(image.load('A4.png'),(700,500))
finish = transform.scale(image.load('win.png'),(700,500))
lose = transform.scale(image.load('lose.png'),(700,500))

print(type(finish))
class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self,picture,w,h,x,y, x_speed,y_speed):
        super().__init__(picture,w,h,x,y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed

        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)

        self.rect.y += self.y_speed

        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)

    def fire(self):
        bullet = Bullet('pulka.png', 25, 8, self.rect.right, self.rect.centery, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def __init__(self,picture,w,h,x,y,speed):
        super().__init__(picture,w,h,x,y,)
        self.speed = speed
        self.direction = "left"
    def update(self):
        if self.rect.x <= 500:
            self.direction = "right"
        if self.rect.x >= 620:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemyy(GameSprite):
    def __init__(self,picture,w,h,x,y,speed):
        super().__init__(picture,w,h,x,y,)
        self.speed = speed
        self.direction = "down"
    def update(self):
        if self.rect.y <= 0:
            self.direction = "up"
        if self.rect.y >= 150:
            self.direction = "down"

        if self.direction == "down":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width + 10:   
            self.kill()

player = Player('legon.png',60,60,355,400,0,0)
monster2 = Enemy('hero.png',60,60,620,130,5)
final = GameSprite('banka.png',100,80,600,400)
monster3 = Enemyy('hero.png',60,60,370,130,5)
monster4 = Enemyy('hero.png',60,60,150,10,5)
wall1 = GameSprite('stenavverh.png',50,150,270,370)
wall2 = GameSprite('stenavverh.png',50,170,120,213)
wall3 = GameSprite('stenavverh.png',50,400,450,115)
wall4 = GameSprite('stenavniz.png',320,50,140,210)
wall5 = GameSprite('stenavverh.png',5,500,700,5)
wall6 = GameSprite('stenavverh.png',1,500,-2,5)
wall7 = GameSprite('stenavniz.png',700,10,0,500)
wall8 = GameSprite('stenavniz.png',700,10,0,-10)
monster1 = Enemy('hero.png',60,60,500,300,5)

bullets = sprite.Group()
barriers = sprite.Group()

barriers.add(wall1)
barriers.add(wall2)
barriers.add(wall3)
barriers.add(wall4)
barriers.add(wall5)
barriers.add(wall6)
barriers.add(wall7)
barriers.add(wall8)

Enemmy = sprite.Group()

Enemmy.add(monster1)
Enemmy.add(monster2)
Enemmy.add(monster3)
Enemmy.add(monster4)

win = False
run = True

while run:
    time.delay(50)

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                player.y_speed = -7
            if e.key == K_s:
                player.y_speed = 7
            if e.key == K_a:
                player.x_speed = -7
            if e.key == K_d:
                player.x_speed = 7
        elif e.type == KEYUP:
            if e.key == K_w:
                player.y_speed = 0
            if e.key == K_s:
                player.y_speed = 0
            if e.key == K_a:
                player.x_speed = 0
            if e.key == K_d:
                player.x_speed = 0
            if e.key == K_SPACE:
                player.fire()

    if win != True:
        window.blit(back, (0,0))

        player.update()
        final.reset()
        player.reset()
        barriers.draw(window)
        bullets.update()
        bullets.draw(window)
        Enemmy.update()
        Enemmy.draw(window)

        sprite.groupcollide(bullets, barriers, True, False)
        sprite.groupcollide(Enemmy, bullets, True, True)

    if sprite.spritecollide(player, Enemmy, False):
        win = True
        window.blit(lose,(0,0))
        

    if sprite.collide_rect(player, final):
        win = True
        window.blit(finish ,(0,0))

    display.update()

