import pygame

class Robot(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot1.png'), (80, 80)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot2.png'), (80, 80)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot3.png'), (80, 80)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot4.png'), (80, 80)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot5.png'), (80, 80)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot6.png'), (80, 80)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot7.png'), (80, 80)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

        self.forward = True

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
        if self.rect.x > 670:
            self.forward = False
        
        if self.forward:
            self.rect.x += 5
        else:
            self.rect.x -= 5
        
        if self.rect.x == 100:
            self.forward = True
            return False
    
        return True
    
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))