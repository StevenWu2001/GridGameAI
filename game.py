import pygame, sys, math

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

    def walk(self):
        self.attack_animation = True

    def update(self,speed):
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False

        self.image = self.sprites[int(self.current_sprite)]

class Ground(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('sprites/ground.png'), (80, 80))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(30, 240)
moving_sprites.add(player, [Ground(0 + 80 * x, 320) for x in range(10)])

bg = pygame.transform.scale(pygame.image.load('sprites/background.png'), (800, 400))
bg_width = bg.get_width()
bg_rect = bg.get_rect()
scroll = 0
tiles = math.ceil(screen_width  / bg_width) + 1

animate = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()	   	
        if event.type == pygame.KEYDOWN:
            animate = True
        if event.type == pygame.KEYUP:
            animate = False
    
    screen.fill((0,0,0))

    if animate:
        player.walk()
        scroll -= 3
        
    #draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll
    #scroll background
    
    #reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    moving_sprites.draw(screen)
    moving_sprites.update(0.1)
    pygame.display.flip()
    clock.tick(60)