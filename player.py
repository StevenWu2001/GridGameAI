import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/player/player1.png'), (80, 80)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/player/player2.png'), (80, 80)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/player/player3.png'), (80, 80)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/player/player4.png'), (80, 80)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

        self.forward = True
        self.flipped = False

    def walk(self):
        self.attack_animation = True

    def update(self,speed):
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False

        self.image = self.sprites[int(self.current_sprite)]
    
    def attack(self):
        if self.rect.x > 600:
            self.forward = False
            self.flipped = True
        
        if self.forward:
            self.rect.x += 5
        else:
            self.rect.x -= 5
        
        if self.rect.x == 30:
            self.forward = True
            self.flipped = False
            return False
    
        return True
        
    def draw(self, surface):
        surface.blit(pygame.transform.flip(self.image, self.flipped, False), (self.rect.x, self.rect.y))