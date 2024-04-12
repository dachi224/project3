import random
import sys
import pygame
from pygame import mixer
import math

mixer.init()

#მუსიკების შემოტანა
# mixer.music.load("images/jungles.ogg")
# mixer.music.play(-1)

pygame.init()
clock = pygame.time.Clock()

width = 1000
height = 700

size = (50, 50)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hunting")

text = 'Game Over!'
color = (255, 40, 40)

class BaloonClass(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image = pygame.transform.scale(pygame.image.load(img), (150, 150))
        self.speed = random.choice([-1, 1])
        self.counter = 0

    def draw(self):
        pygame.draw.rect(screen, (100, 100, 100), self.rect)

    def update(self):
        self.counter += 1
        if self.counter > 25:
            self.counter = 0
            self.speed = random.choice([-1, 1])

        self.rect.y += self.speed

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= 400:
            self.rect.bottom = 400

class TargetClass:
    def __init__(self, image):
        self.image = pygame.transform.scale(pygame.image.load(image), (50, 50))
        self.rect = self.image.get_rect(centerx=width/2, centery=height/2)

    def draw(self):
        screen.blit(self.image, self.rect)

    def movement(self):
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.movement()
        self.draw()


class BulletClass(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.rect = pygame.Rect(width/2, height, 50, 50)
        self.rect.center = [width / 2, height]
        self.image = pygame.transform.scale(pygame.image.load(image), (30, 30))
        self.speed = 5
        self.dx = 0
        self.dy = 0

    def movement(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def update(self):
        self.movement()



baloon_group = pygame.sprite.Group()
images = ["red.png", "yellow.png", "green.png"]
for i, img in enumerate(images):
    target = BaloonClass(i*420, 100, img)
    baloon_group.add(target)

font = pygame.font.Font(None, 120)

def game_over(text, color):
    rendered_text = font.render(text, True, color)
    rect = rendered_text.get_rect(centerx=width/2, centery=height/2)
    screen.blit(rendered_text, rect)

target = TargetClass("target.png")
bullet_group = pygame.sprite.Group()
# gun = GunClass("gun.png")

pygame.mouse.set_visible(False)

run = True
while run:
    clock.tick(60)

    screen.fill((255, 255, 255))

    baloon_group.update()
    baloon_group.draw(screen)

    # gun.update()

    target.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = BulletClass("bullet.png")
            bullet_group.add(bullet)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance_x = mouse_x - bullet.rect.centerx
            distance_y = mouse_y - bullet.rect.centery

            angle = math.atan2(distance_y, distance_x)

            bullet.dx = bullet.speed * math.cos(angle)
            bullet.dy = bullet.speed * math.sin(angle)


    bullet_group.update()
    bullet_group.draw(screen)

    pygame.display.update()


game_over(text, color)
pygame.display.update()
pygame.time.wait(3000)

pygame.quit()
sys.exit()