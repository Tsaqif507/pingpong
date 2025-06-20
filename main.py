from pygame import *

back = (200, 255, 255) #background color (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

p1 = Player('racket.png', 10, 250, 12, 50, 50)
p2 = Player('racket.png', 540, 250, 12, 50, 50)
ball = GameSprite('ball.png', 250, 300, 20, 30, 30)

game = True
finish = False
clock = time.Clock()
FPS = 40

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(back)
    p1.reset()
    p1.update_l()
    p2.reset()
    p2.update_r()
    ball.reset()
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y < 30 or ball.rect.y > win_height - 40:
        speed_y *= -1

    if sprite.collide_rect(p1, ball) or sprite.collide_rect(p2, ball):
        speed_x *= -1

    display.update()
    clock.tick(FPS)