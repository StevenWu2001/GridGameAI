import pygame 

class Ground(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('sprites/ground.png'), (250, 250))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]