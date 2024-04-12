import pygame
clock = pygame.time.Clock()
fps = 60

pygame.init()

size = 50

width = size * 20
height = size * 10
screen = pygame.display.set_mode((width, height))


walking = [pygame.image.load("w1.jpg"), pygame.image.load("w2.jpg"), pygame.image.load("w3.jpg"), pygame.image.load("w4.jpg")]

walking_left = []
for image in walking:
    image = pygame.transform.flip(image, True, False)
    walking_left.append(image)

punch = [pygame.image.load("p1.jpg"), pygame.image.load("p2.jpg"), pygame.image.load("p3.jpg"), pygame.image.load("p4.jpg"), pygame.image.load("p1.jpg")]

background_sprites = {
    "T": pygame.image.load("lava_top.png"),
    "M": pygame.image.load("lava_middle.png"),
    "B": pygame.image.load("lava_buttom.png"),
    "S": pygame.image.load("sky.png"),
    "W": pygame.image.load("water.png"),
    "G": pygame.image.load("green_whater.png"),
    "R": pygame.image.load("rock.png"),
    "I": pygame.image.load("island.png")
}

#present_image = pygame.image.load("giftbox.png")

map = [
"SSSSSSSSSSSSSSSSSSSS",
"SSSSSSSSSSSSSSSSSSSS",
"SSSSSSSSSIIIIISSSSSS",
"SSSIIISSSSSSSSSIIISS",
"SSSSSSSSSSSSSSSSSSSS",
"SSSSSSSSSSSSSSSSSSSS",
"SSSSSSSSSSSSSSSSSSSS",
"RRTTTTTTTTTTGTTTTWWW",
"MMMMMMMMMMMMGMMMMWWW",
"BBBBBBBBBBBBGBBBBTTT"
]

class Background(pygame.sprite.Sprite):
    def __init__(self, image, size, x, y, name):
        super().__init__()
        self.size = size
        self.name = name
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self.rect = self.image.get_rect(x=x, y=y)

    def collision(self):
        if self.name in ["T", "M", "B", "I", "R"] and self.rect.colliderect(player.rect):
            player.gravity = False
            player.rect.bottom = self.rect.top

        if self.name in ["S", "G"] and self.rect.colliderect(player.rect):
            player.gravity = True


    def update(self):
        self.collision()

class Item(pygame.sprite.Sprite):
    def __init__(self, image, size, x, y):
        super().__init__()
        self.size = size
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self.rect = self.image.get_rect(x=x, y=y)
        self.taken = False

    def collision(self):
        if self.rect.colliderect(player.rect):
            self.taken = True

    def update(self):
        self.collision()
        if not self.taken:
            screen.blit(self.image, self.rect)

#present = Item(present_image, 30, 300, 300)

pygame.display.set_caption("GGame")

background_group = pygame.sprite.Group()

for y, line in enumerate(map):
    for x, symbol in enumerate(line):
        new_block = Background(background_sprites[symbol], size, x * size, y * size, symbol)
        background_group.add(new_block)



class Player(pygame.sprite.Sprite):
    def __init__(self, walking, walking_left, punch_right):
        super().__init__()
        self.walking = walking
        self.punch_right = punch_right
        self.walking_left = walking_left
        self.i = 0
        self.punching = False
        self.image = walking[self.i]
        self.size = size // 2
        self.rect = self.image.get_rect(x=size // 2, y=height - 10 * size)
        self.jump = False
        self.gravity = True
        self.speed = 3
        self.speed_x = 0
        self.speed_y = 0
        self.timer = 0
        self.right = True

    def draw(self):
        screen.blit(self.image, self.rect)


        if self.speed_x != 0:
            if self.speed_x > 0:
                self.right = True
                self.image = self.walking[self.i]
            else:
                self.right = False
                self.image = self.walking_left[self.i]

            self.timer += 1
            if self.timer == 10:
                self.timer = 0
                if self.i < len(self.walking)-1:
                    self.i += 1
                else:
                    self.i = 0


        if self.punching:
            if self.right:
                self.image = self.punch_right[self.i]
            else:
                self.image = pygame.transform.flip((self.punch_right[self.i]), True, False)
            self.timer += 1
            if self.timer == 3:
                self.timer = 0
                if self.i < len(self.walking):
                    self.i += 1
                else:
                    self.punching = False
                    self.i = 0


    def movement(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width


        if self.gravity:
            self.speed_y += 1

        elif not self.jump:
            self.speed_y = 0



    def update(self):
        self.draw()
        self.movement()

player = Player(walking, walking_left, punch)
player_group = pygame.sprite.Group()
player_group.add(player)

run = True
while run:
    clock.tick(fps)
    background_group.draw(screen)
    background_group.update()
    player_group.update()
    #present.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -player.speed
            if event.key == pygame.K_RIGHT:
                player.speed_x = player.speed

            if event.key == pygame.K_p:
                player.speed_x = 0
                player.punching = True
                player.i = 0
                player.timer = 0
            # if event.key == pygame.K_SPACE and not player.jump:
            #     player.jump = True
            #     player.speed_y = -7 * player.speed
            #     player.gravity = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0

    pygame.display.update()
