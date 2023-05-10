import pygame

#screen display start
wide = 900
tall = 700
screen = pygame.display.set_mode((wide, tall))
#screen display end

#sprite images start
player_image = pygame.image.load("images/spaceboat.png")
enemy_image = pygame.image.load("images/rock.png")
star_image = pygame.image.load("images/star.png")
back_image1 = pygame.image.load("images/bg1.png")
back_image2 = pygame.image.load("images/bg2.png")
back_image3 = pygame.image.load("images/bg1.png")
shield_image = pygame.image.load("images/shield3.png")
#sprite images end

#sprite groups start
all_sprites = pygame.sprite.LayeredUpdates()
shields = pygame.sprite.Group()
enemies = pygame.sprite.Group()
stars = pygame.sprite.Group()
space = pygame.sprite.Group()
#sprite groups end

#misc. variables
r = -1
timer = 450
clock = pygame.time.Clock()
running = True
printed = False
shieldup = 1
