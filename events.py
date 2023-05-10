import pygame
pygame.init()

#in game events, necessary to spawn new sprites/surfaces
addbad = pygame.USEREVENT + 1
pygame.time.set_timer(addbad, 350)

addstar = pygame.USEREVENT +2
pygame.time.set_timer(addstar, 400)

addback = pygame.USEREVENT +3
pygame.time.set_timer(addback, 100)

raiseshield = pygame.USEREVENT +4
pygame.time.set_timer(raiseshield, 3000)

firstshield = pygame.USEREVENT +5
pygame.time.set_timer(firstshield, 1)
