import pygame
clock = pygame.time.Clock()
fps = 60

pygame.init()

size = 50

width = size * 20
height = size * 10


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Game")

background_sprites = {
    "T": pygame.image.load("lava_top.png"),
    "M": pygame.image.load("lava_middle.png"),
    "B": pygame.image.load("lava_buttom.png"),
    "S": pygame.image.load("sky.png"),
    "G": pygame.image.load("green_whater.png"),
    "R": pygame.image.load("rock.png"),
    "I": pygame.image.load("island.png"),
    "W": pygame.image.load("water.png")
}

level_map = [
    "SSSSSSSSSSSSSSSSSSSS",
    "SSSSSSSSSSSSSSSSSSSS",
    "SSSSSSSSSSSSSSSSSSSS",
    "SSSSSSSSSSIIIISSSSSS",
    "SSSSIISSSSSSSSSSISSS",
    "SSSSSSSSSSSSSSSSSSSS",
    "SSSSSSSSSSSSSSSSSSSS",
    "RRTTTTTTTTTGTTTTTWWW",
    "MMMMMMMMMMMGMMMMMWWW",
    "BBBBBBBBBBBGBBBBBTTT"
]

class Background(pygame.sprite.Sprite):
    def __init__(self, image, size, x, y, name):
        super().__init__()
        self.name = name
        self.image = pygame.transform.scale(image, (size, size))
        self.rect = self.image.get_rect(x=x, y=y)

    def collision(self):
        if self.name in ["T", "M", "B", "I", "R"] and self.rect.colliderect(player.rect):
            player.gravity = False
            player.rect.bottom = self.rect.top

        if self.name in ["S", "G", "W"] and self.rect.colliderect(player.rect):
            player.gravity = True

    def update(self):
        self.collision()

background_group = pygame.sprite.Group()

for y, line in enumerate(level_map):
    for x, symbol in enumerate(line):
        new_block = Background(background_sprites[symbol], size, x * size, y * size, symbol)
        background_group.add(new_block)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = size // 2
        self.rect = pygame.Rect(25, height - 5 * size, self.size, self.size)
        self.speed = 3
        self.speed_x = 0
        self.speed_y = 0
        self.jump = False
        self.gravity = True

    def draw(self):
        pygame.draw.rect(screen, (255, 100, 100), self.rect)

    def movement(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.gravity:
            self.speed_y += 1

        elif not self.jump:
            self.speed_y = 0

        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= width:
            self.rect.right = width

    def update(self):
        self.draw()
        self.movement()


player_group = pygame.sprite.Group()

player = Player()
player_group.add(player)

run = True
while run:
    clock.tick(fps)
    background_group.draw(screen)
    background_group.update()
    player.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -player.speed
            if event.key == pygame.K_RIGHT:
                player.speed_x = player.speed

            # if event.key == pygame.K_SPACE and not player.gravity:
            #     player.speed_y = -7 * player.speed
            #     player.gravity = True

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player.speed_x = 0


    pygame.display.update()
