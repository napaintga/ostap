from pygame import *

# ініціалізація Pygame
mixer.init()
wn = display.set_mode((700, 350))
clock = time.Clock()
game = True
finish = False
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, pl_x, pl_y, size_x, size_y, pl_speed):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
        self.speed = pl_speed
    
    def reset(self):
        wn.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 63:
            self.rect.x -= self.speed+3
        if keys[K_d] and self.rect.x < 1000 :
            self.rect.x += self.speed+3
        if keys[K_w] :
            self.rect. y -= self.speed+3
        if keys[K_s] :
            self.rect. y += self.speed+3

class Area():
    def __init__(self, x=0, y=0, width =10, height =10, color=None):
        self.rect = Rect(x, y, width, height)#прямокутник
        self.fill_color = color


    def color(self, new_color):
        self.fill_color = new_color


    def fill(self):
        draw.rect(wn,self.fill_color,self.rect)


color = (134,132,124)
walls =[Area(288,328,322-288,10, color),
        Area(496,338,532-492,10, color),
        Area(568,318,600-568,10, color),

]

# Завантаження зображень
hero = Player("a-removebg-preview.png", 100, 150, 35, 35, 1)
background = transform.scale(image.load("2838214618_preview_20221127_124242.png"), (700, 500))
background1 = transform.scale(image.load("2838214618_preview_20221127_124242.png"), (700, 500))

tchili = GameSprite("Без_імені-removebg-preview.png",120,177 ,1439, 173,3)


font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
xbg = 0
GAME_SPEED = 3
global grav
grav= 1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        wn.blit(background, (xbg, 0))
        wn.blit(background1, (xbg + 700, 0))
        if xbg < -700:
            xbg = 0

        xbg -= GAME_SPEED
        # tchili.rect.x -= GAME_SPEED
        hero.reset()
        hero.update()
        tchili.reset()  # Додано для відображення платформи
        
        text_score = font.render("hero: " + str(hero.rect.y), 1, (255, 255, 255))
        wn.blit(text_score, (10, 20))
        x = font.render("hero: " + str(hero.rect.x), 1, (255, 255, 255))
        wn.blit(x, (10, 40))
        
        for wall in walls:
            wall.fill()
            # wall.rect.x -= 1
        
        grav = 1
        
        for wall in walls:
            if hero.rect.colliderect(wall.rect):
                grav = 0
                break
        # if grav:
        #     hero.rect.y += hero.speed +1
        
        keys = key.get_pressed()
        if keys[K_w]:
            hero.rect.y -= hero.speed * 4
            grav = 1

    display.update()
    clock.tick(FPS)

