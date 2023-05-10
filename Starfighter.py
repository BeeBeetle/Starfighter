from actors import *
from variables import *
from pygame.locals import *
from events import *

pygame.init() # literally just runs the program

player = PLAYER()
all_sprites.add(player)
shield = SHIELD()

new_back1=BACKGROUND1()
new_back2=BACKGROUND2()
new_back3=BACKGROUND3()

while running:
    clock.tick_busy_loop(30)
    keystroke = pygame.key.get_pressed()
    player.update(keystroke)
    shield.update(keystroke)
    enemies.update()
    stars.update()
    space.update()
    screen.fill((0,0,0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        print("Sorry man, you dead.")
        running = False
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                pygame.quit()
        elif event.type == addback:
            if r == -1:
                space.add(new_back1)
                all_sprites.add(new_back1)
                r = -1
            elif r == 0:
                new_back2.start(wide)
                space.add(new_back2)
                all_sprites.add(new_back2)
            elif r == 299:
                new_back3.start(wide)
                space.add(new_back3)
                all_sprites.add(new_back3)
            elif r == 598:
                new_back2.start(wide)
                space.add(new_back2)
                all_sprites.add(new_back2)
                r = 0
            r += 1
        elif event.type == addbad:
            new_bad = BAD()
            enemies.add(new_bad)
            all_sprites.add(new_bad)
        if timer == 450:
            shields.add(shield)
            all_sprites.add(shield)
            if printed == False:
                print("Shields restored!")
                printed = True
            if pygame.sprite.spritecollide(shield, enemies, dokill=True):
                shield.kill()
                shields.update()
                print("Shields down!")
                timer = 0
                printed = False
        elif timer <= 450:
            if len(shields.sprites()) == 0:
                timer += 1
        elif event.type == addstar:
            new_star = STARS()
            stars.add(new_star)
            all_sprites.add(new_star)
pygame.quit()
