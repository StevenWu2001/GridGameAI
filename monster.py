import pygame

class Monster(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.size = 300
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/1.png'), (self.size, self.size)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/2.png'), (self.size, self.size)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/3.png'), (self.size, self.size)))        
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/4.png'), (self.size, self.size)))        
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/5.png'), (self.size, self.size)))        
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/6.png'), (self.size, self.size)))        
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/7.png'), (self.size, self.size)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/8.png'), (self.size, self.size)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/9.png'), (self.size, self.size)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/10.png'), (self.size, self.size)))        
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/11.png'), (self.size, self.size)))        
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/12.png'), (self.size, self.size)))        
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/13.png'), (self.size, self.size)))        
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/14.png'), (self.size, self.size)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/15.png'), (self.size, self.size)))        
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/16.png'), (self.size, self.size)))        
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/17.png'), (self.size, self.size)))        
        self.sprites.append(pygame.transform.scale(pygame.image.load('sprites/monster1/18.png'), (self.size, self.size)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def attack(self):
        self.attack_animation = True

    def update(self,speed):
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False
                return False

        self.image = self.sprites[int(self.current_sprite)]
        return True
    
    def update_pos(self):
        self.rect.x -= 3
        if self.rect.x < 500:
            return False

        return True

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))