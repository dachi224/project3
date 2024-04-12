import pygame
from settings import player_size, background_size, width
pygame.init()

full_sky = pygame.transform.scale(pygame.image.load("images/BG/BG.png"), (width, 7*50))

santa_movement = []

santa_standing = []
for i in range(1, 17):
    sprite = pygame.image.load(f"images/santa/Idle ({i}).png")
    sprite = pygame.transform.scale(sprite, player_size)
    santa_standing.append(sprite)

santa_movement.append(santa_standing)

santa_walking = []
for i in range(1, 14):
    sprite = pygame.image.load(f"images/santa/Walk ({i}).png")
    sprite = pygame.transform.scale(sprite, player_size)
    santa_walking.append(sprite)

santa_movement.append(santa_walking)

santa_jumping = []
for i in range(1, 17):
    sprite = pygame.image.load(f"images/santa/Jump ({i}).png")
    sprite = pygame.transform.scale(sprite, player_size)
    santa_jumping.append(sprite)

santa_movement.append(santa_jumping)

santa_running = []
for i in range(1, 12):
    sprite = pygame.image.load(f"images/santa/Run ({i}).png")
    sprite = pygame.transform.scale(sprite, player_size)
    santa_running.append(sprite)

santa_movement.append(santa_running)

santa_sliding = []
for i in range(1, 12):
    sprite = pygame.image.load(f"images/santa/Slide ({i}).png")
    sprite = pygame.transform.scale(sprite, player_size)
    santa_sliding.append(sprite)

santa_movement.append(santa_sliding)

santa_death = []

for i in range(1, 18):
    sprite = pygame.image.load(f"images/santa/Dead ({i}).png")
    sprite = pygame.transform.scale(sprite, player_size)
    santa_death.append(sprite)

santa_movement.append(santa_death)


background_sprites = {}
for i in range(1, 19):
    background_sprites[i] = pygame.transform.scale(pygame.image.load(f"images/Tiles/{i}.png"), background_size)



objects = {
    "box": pygame.image.load(f"images/Object/Crate.png"),
    "crystal": pygame.image.load(f"images/Object/Crystal.png"),
    "icebox": pygame.image.load(f"images/Object/IceBox.png"),
    "igloo": pygame.image.load(f"images/Object/Igloo.png"),
    "sign1": pygame.image.load(f"images/Object/Sign_1.png"),
    "sign2": pygame.image.load(f"images/Object/Sign_2.png"),
    "snowman": pygame.image.load(f"images/Object/SnowMan.png"),
    "stone": pygame.image.load(f"images/Object/Stone.png"),
    "tree1": pygame.image.load(f"images/Object/Tree_1.png"),
    "tree2": pygame.image.load(f"images/Object/Tree_2.png"),
}

object_sprites = {}
for key, value in objects.items():
    object_sprites[key] = pygame.transform.scale(value, background_size)
