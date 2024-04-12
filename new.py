import pygame
from random import randint
#მიქსერის შემოტანა
from pygame import mixer

#ფაიგეიმის ინიციაცია
pygame.init()
#მიქსერის ინიციაცია
mixer.init()
clock = pygame.time.Clock()
fps = 30
#მუსიკის ატვირთვა
mixer.music.load("Bobby Helms - Jingle Bell Rock (Lyrics) (1).mp3")
#მუსიკის დაკვრა (ლუფით)
mixer.music.play(-1)
#ხმის დაწევა
mixer.music.set_volume(0.5)


#ეკრანის ზომები
width = 1000
height = 668
#ეკრანის შექმნა
screen = pygame.display.set_mode((width, height))
#ფანჯარაზე წარწერის ცვლილება
pygame.display.set_caption("Merry Christmas")
#სურათის შემოტანა (ნაძვი)
icon = pygame.image.load("tree1.png")
#ფანჯარაზე სურათის შეცვლა
pygame.display.set_icon(icon)

red = (255, 100, 100)
background = pygame.image.load("moonbackground.png")
#ფონის სურათის ზომის შეცვლა
background = pygame.transform.scale(background, (width, height))

tree1 = pygame.image.load("tree1.png")
tree1 = pygame.transform.scale(tree1, (500, 500))
tree2 = pygame.image.load("tree2.png")
tree2 = pygame.transform.scale(tree2, (500, 500))

class SnowFlake(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = [randint(-1000, width), randint(-500, -25)]


    def update(self):
        self.rect.y += 30
        self.rect.x += 15
        if self.rect.y > height:
            self.kill()



#მთავარი ანიმაციის კლასი
class ChristmasTree:
    def __init__(self, images):
        self.images = images
        self.image = images[0]
        self.rect = self.image.get_rect()
        self.rect.center = [width/2, height/1.6]
    #სურათის დახატვის ფუნქცია
    def draw(self):
        global counter
        screen.blit(self.image, self.rect)
        if counter == 0:
            if self.image == self.images[0]:
                self.image = self.images[1]
            else:
                self.image = self.images[0]



# ობიექტის შექმნა მთავარი კლასისგან
christmastree = ChristmasTree([tree1, tree2])

snow_group = pygame.sprite.Group()
snow_image = pygame.image.load("snowflake (2).png")
counter = 0
def create_snow():
    if counter == 0:
        for _ in range(randint(10, 30)):
            flake = SnowFlake(snow_image)
            snow_group.add(flake)

    snow_group.draw(screen)
    snow_group.update()


red = (255, 50, 50)
yellow = (255, 255, 50)
color = yellow

font = pygame.font.Font("font.ttf", 120)

def message(color, font):
    rendered_text = font.render("Happy New Year!", False, color)
    text_rect = rendered_text.get_rect()
    text_rect.center = [width/2, 150]
    screen.blit(rendered_text, text_rect)


run = True
while run:
    clock.tick(fps)
    counter += 1
    if counter > 15:
        counter = 0
        if color == red:
            color = yellow
        else:
            color = red


    #ფონის ფერის ჩასხმა
    # screen.fill(red)
    #ფონის სურათის დადება
    screen.blit(background, ( 0, 0))
    #message(color, font)
    #ობიექტის დახატვა
    christmastree.draw()
    create_snow()
    #კოდის გათიშვა
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #ეკრანის განახლება
    pygame.display.update()
