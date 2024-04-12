import pygame
from maps import level_map, object_map
from sprites import santa_movement, background_sprites, full_sky, object_sprites
from settings import width, height, size
from pygame import mixer
mixer.init()
jumping_sound = mixer.Sound("jump.mp3")

clock = pygame.time.Clock()
pygame.init()


pygame.display.set_caption("Christmas")
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load("images/Object/Tree_2.png"))



class Background(pygame.sprite.Sprite):
    def __init__(self, image, size, x, y, name, border=False):
        super().__init__()
        self.size = size
        self.name = name
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self.rect = self.image.get_rect(x=x, y=y)
        self.border = border



background_group = pygame.sprite.Group()
border_group = pygame.sprite.Group()

for y, line in enumerate(level_map):
    for x, symbol in enumerate(line):
        if symbol != "":
            if symbol in [2, 14, 15, 16]:
                new_block = Background(background_sprites[symbol].convert_alpha(), size, x * size, y * size, symbol, True)
                border_group.add(new_block)
            else:
                new_block = Background(background_sprites[symbol].convert_alpha(), size, x * size, y * size, symbol)

            background_group.add(new_block)

for y, line in enumerate(object_map):
    for x, symbol in enumerate(line):
        if symbol != "":
            new_block = Background(object_sprites[symbol].convert_alpha(), size, x * size, y * size, symbol)
            background_group.add(new_block)


#background movement
def background_movement(speed):
    for tile in background_group:
        tile.rect.x -= speed


class Player(pygame.sprite.Sprite):
    def __init__(self, movement):
        super().__init__()
        self.movement = movement
        self.standing = movement[0]
        self.walking = movement[1]
        self.jumping = movement[2]
        self.i = 0
        self.image = self.standing[self.i].convert_alpha()
        self.size = size // 2
        self.rect = self.image.get_rect(x=size // 2, y=height - 6 * size)
        self.speed = 3
        self.dx = 0
        self.dy = 0
        self.speed_x = 0
        self.speed_y = 0
        self.timer = 0
        self.right = True

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def draw(self):
        screen.blit(self.image, self.rect)




        self.timer += 1
        if self.timer == 3:
            self.timer = 0
            if self.i < len(self.walking)-1:
                self.i += 1
            else:
                self.i = 0




    def movements(self):

        dx = 0
        dy = 0
        walk_cooldown = 5

        # get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            jumping_sound.play()
            self.vel_y = -20
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0

        if dx > 0:
            self.right = True
        elif dx < 0:
            self.right = False

        #Animations
        if self.vel_y != 0:
            self.image = self.jumping[self.i].convert_alpha()
            if not self.right:
                self.image = pygame.transform.flip(self.image, True, False)

        elif dx != 0 and dy == 0:
            # global scroll
            self.image = self.walking[self.i].convert_alpha()
            if not self.right:
                self.image = pygame.transform.flip(self.image, True, False)

            #ფლეიერის ერთ ადგილას სირბილი
            if dx > 0 and self.rect.right >= width-100:
                self.rect.right = width-100
                background_movement(dx)

            if dx < 0 and self.rect.left <= 100:
                self.rect.left = 100
                background_movement(dx)



        else:
            self.image = self.standing[self.i]
            if not self.right:
                self.image = pygame.transform.flip(self.image, True, False)




        # add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # check for collision
        for tile in border_group:
            # check for collision in x direction
            if tile.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            # check for collision in y direction
            if tile.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground i.e. jumping
                if self.vel_y < 0:
                    dy = tile.rect.bottom - self.rect.top
                    self.vel_y = 0
                # check if above the ground i.e. falling
                elif self.vel_y >= 0:
                    dy = tile.rect.top - self.rect.bottom
                    self.vel_y = 0

        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > height:
            self.rect.bottom = height
            dy = 0




    def update(self):
        self.draw()
        self.movements()

player = Player(santa_movement)
player_group = pygame.sprite.Group()
player_group.add(player)

bx = 0
by = 0

run = True
while run:
    screen.fill((0,0,0))


    for i in range(-3, 3):
        screen.blit(full_sky, (bx + i * width, by))

    background_group.draw(screen)
    background_group.update()
    player_group.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    pygame.display.update()
    clock.tick(60)
