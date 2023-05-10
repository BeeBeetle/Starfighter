import random
from pygame import *
from variables import *

# all classes for different in game actors (player/enemies/misc items that move)
# make sure the player has a higher layer number than any objects to be displayed BELOW the player
# if you don't then things will be funky, here I have the enemies (space rocks) on a layer above because
# as soon as you collide with one the game is over anyways, plus for a frame or two it looks better to have
# the asteroid clip over the player so it looks more like a crash

# player class


class SHIELD(pygame.sprite.Sprite):

    def __init__(self):
        super(SHIELD, self).__init__()
        self.surf = shield_image
        self.rect = self.surf.get_rect(
            center=(wide-768, tall-319)
        )
        self._layer = 5

    def update(self, pressed_keys):
        if pressed_keys [K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys [K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys [K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys [K_RIGHT]:
            self.rect.move_ip(5,0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > wide:
            self.rect.right = wide
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > tall:
            self.rect.bottom = tall


class PLAYER(pygame.sprite.Sprite):

    def __init__(self):
        super(PLAYER, self).__init__()
        self.surf = player_image
        self.rect = self.surf.get_rect(
            center=(wide-793, tall-319)
        )
        self._layer = 4

    def update(self, pressed_keys):
        if pressed_keys [K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys [K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys [K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys [K_RIGHT]:
            self.rect.move_ip(5,0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > wide:
            self.rect.right = wide
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > tall:
            self.rect.bottom = tall


#class for enemies


class BAD(pygame.sprite.Sprite):
    def __init__(self):
        super(BAD, self).__init__()
        self.surf = enemy_image
        self.rect = self.surf.get_rect(
            center=(
                random.randint(wide+20,wide+100),
                random.randint(0, tall),
            )
        )
        self.speed = random.randint(5,20)
        self._layer = 5

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


#class for moving stars (non-collision)


class STARS(pygame.sprite.Sprite):
    def __init__(self):
        super(STARS, self).__init__()
        self.surf = star_image
        self.rect = self.surf.get_rect(
            center=(
                random.randint(wide+20,wide+50),
                random.randint(0,tall),
            )
        )
        self.speed = random.randint(2,7)
        self._layer = 2

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


#a moving background image (starscape)


class BACKGROUND1(pygame.sprite.Sprite):
    def __init__(self):
        super(BACKGROUND1, self).__init__()
        self.surf = back_image1
        self.rect = self.surf.get_rect()
        self.speed = 1
        self._layer = 1

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def start(self, x):
        self.rect = self.surf.get_rect(
            topleft=(x,0)
        )


class BACKGROUND2(pygame.sprite.Sprite):
    def __init__(self):
        super(BACKGROUND2, self).__init__()
        self.surf = back_image2
        self.rect = self.surf.get_rect()
        self.speed = 1
        self._layer = 1

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def start(self, x):
        self.rect = self.surf.get_rect(
            topleft=(x,0)
        )


class BACKGROUND3(pygame.sprite.Sprite):
    def __init__(self):
        super(BACKGROUND3, self).__init__()
        self.surf = back_image3
        self.rect = self.surf.get_rect()
        self.speed = 1
        self._layer = 1

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def start(self, x):
        self.rect = self.surf.get_rect(
            topleft=(x,0)
        )

