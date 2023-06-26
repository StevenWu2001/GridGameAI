import pygame 

class House(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, screen_width):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('sprites/house.png'), (400, 400))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
        self.screen_width = screen_width

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
    
    def update_pos(self):
        self.rect.x -= int(self.screen_width / 300)
        if self.rect.x < int(self.screen_width * 0.7):
            return False

        return True

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y