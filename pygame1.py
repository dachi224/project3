import pygame
#მიქსერის შემოტანა
from pygame import mixer

#ფაიგეიმის ინიციაცია
pygame.init()
#მიქსერის ინიციაცია
mixer.init()

#მუსიკის ატვირთვა
#mixer.music.load("christmas.mp3")
#მუსიკის დაკვრა (ლუფით)
#mixer.music.play(-1)
#ხმის დაწევა
#mixer.music.set_volume(0.5)


#ეკრანის ზომები
width = 600
height = 400
#ეკრანის შექმნა
screen = pygame.display.set_mode((width, height))
#ფანჯარაზე წარწერის ცვლილება
pygame.display.set_caption("Merry Christmas")
#სურათის შემოტანა (ნაძვი)
icon = pygame.image.load("new.png")
#ფანჯარაზე სურათის შეცვლა
pygame.display.set_icon(icon)

red = (255, 100, 100)
#background = pygame.image.load("background.jpg")
#ფონის სურათის ზომის შეცვლა
#background = pygame.transform.scale(background, (width, height))

tree = pygame.image.load("new.png")
tree = pygame.transform.scale(tree, (200, 200))

#მთავარი ანიმაციის კლასი
class ChristmasTree:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [width/2, height/2]
    #სურათის დახატვის ფუნქცია
    def draw(self):
        screen.blit(self.image, self.rect)


# ობიექტის შექმნა მთავარი კლასისგან
christmastree = ChristmasTree(tree)



run = True
while run:
    #ფონის ფერის ჩასხმა
    screen.fill(red)
    #ფონის სურათის დადება
    #screen.blit(background, (0, 0))
    #ობიექტის დახატვა
    christmastree.draw()
    #კოდის გათიშვა
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #ეკრანის განახლება
    pygame.display.update()


