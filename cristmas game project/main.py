import pygame
from maps import level_map, object_map
from sprites import santa_movement, background_sprites, full_sky, object_sprites
from settings import width, height, size

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Christmas")
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load("images/Object/Tree_2.png"))

class Background(pygame.sprite.Sprite):
    def __init__(self, image, size, x, y, name):
        super().__init__()
        self.size = size
        self.name = name
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self.rect = self.image.get_rect(x=x, y=y)




background_group = pygame.sprite.Group()

for y, line in enumerate(level_map):
    for x, symbol in enumerate(line):
        if symbol != "":
            new_block = Background(background_sprites[symbol], size, x * size, y * size, symbol)
            background_group.add(new_block)

for y, line in enumerate(object_map):
    for x, symbol in enumerate(line):
        if symbol != "":
            new_block = Background(object_sprites[symbol], size, x * size, y * size, symbol)
            background_group.add(new_block)


class Player(pygame.sprite.Sprite):
    def __init__(self, movement):
        super().__init__()
        self.movement = movement
        self.standing = movement[0]
        self.walking = movement[1]
        self.jumping = movement[2]
        self.i = 0
        self.image = self.standing[self.i]
        self.size = size // 2
        self.rect = self.image.get_rect(x=size // 2, y=height - 4 * size)
        self.speed = 3
        self.speed_x = 0
        self.speed_y = 0
        self.timer = 0
        self.right = True

        self.jump = False
        self.y_gravity = 1
        self.jump_height = 20
        self.y_velocity = self.jump_height

    def draw(self):
        screen.blit(self.image, self.rect)
        if self.jump:
            self.image = self.jumping[self.i]
            if not self.right:
                self.image = pygame.transform.flip(self.image, True, False)

        elif self.speed_x != 0 and self.speed_y == 0:
                self.image = self.walking[self.i]
                if not self.right:
                    self.image = pygame.transform.flip(self.image, True, False)

        else:
            self.image = self.standing[self.i]
            if not self.right:
                self.image = pygame.transform.flip(self.image, True, False)



        self.timer += 1
        if self.timer == 3:
            self.timer = 0
            if self.i < len(self.walking)-1:
                self.i += 1
            else:
                self.i = 0




    def movements(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.speed_x > 0:
            self.right = True
        elif self.speed_x < 0:
            self.right = False

        if self.rect.left < -45:
            self.rect.left = -45
        if self.rect.right > width+45:
            self.rect.right = width+45

        if self.jump:
            self.rect.y -= self.y_velocity
            self.y_velocity -= self.y_gravity
            if self.y_velocity < -self.jump_height:
                self.jump = False
                self.y_velocity = self.jump_height



    def update(self):
        self.draw()
        self.movements()

player = Player(santa_movement)
player_group = pygame.sprite.Group()
player_group.add(player)



run = True
while run:
    screen.blit(full_sky, (0, 0))
    background_group.draw(screen)
    background_group.update()
    player_group.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -player.speed
            if event.key == pygame.K_RIGHT:
                player.speed_x = player.speed


            if event.key == pygame.K_SPACE:
                player.jump = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0

    pygame.display.update()
    clock.tick(60)