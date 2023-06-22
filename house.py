import pygame 

class House(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('sprites/house.png'), (200, 200))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
    
    def update_pos(self):
        self.rect.x -= 3
        if self.rect.x < 500:
            return False

        return True

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y