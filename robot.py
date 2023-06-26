import pygame

class Robot(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, health, dmg, heal, screen_width):
        super().__init__()
        self.screen_width = screen_width
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot1.png'), (200, 200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot2.png'), (200, 200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot3.png'), (200, 200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot4.png'), (200, 200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot5.png'), (200, 200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot6.png'), (200, 200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/robot/robot7.png'), (200, 200)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

        self.forward = True
        self.flipped = False

        self.health = health
        self.dmg = dmg
        self.heal = heal

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
        if self.rect.x > int(self.screen_width * 0.75):
            self.forward = False
            self.flipped = True
        
        if self.forward:
            self.rect.x += int(self.screen_width / 100)
        else:
            self.rect.x -= int(self.screen_width / 100)
        
        if self.rect.x <= 200:
            self.forward = True
            self.flipped = False
            return False
    
        return True
    
    def draw(self, surface):
        surface.blit(pygame.transform.flip(self.image, self.flipped, False), (self.rect.x, self.rect.y))