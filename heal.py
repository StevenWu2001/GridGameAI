import pygame

class Heal(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        self.size = 200
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/heal/heal1.png'), (self.size, self.size)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/heal/heal2.png'), (self.size, self.size)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/heal/heal3.png'), (self.size, self.size)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/heal/heal4.png'), (self.size, self.size)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/heal/heal5.png'), (self.size, self.size)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

        self.forward = True

    def animate(self):
        self.attack_animation = True

    def update(self,speed):
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False

        self.image = self.sprites[int(self.current_sprite)]
        
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))