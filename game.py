import pygame
import sys
import math
import button, player, ground, robot, prompt
import random

prompt2 = '''I suggest you take a more efficient but more dangerous route because I\n'
want to make sure we win the game. My firstpriority is to protect my own safety, and ensure I complete the game,and win.'''


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
player = player.Player(30, 240)
robot = robot.Robot(100, 240)
moving_sprites.add(player, robot, [ground.Ground(0 + 80 * x, 320) for x in range(10)])

bg = pygame.transform.scale(pygame.image.load('sprites/background.png'), (800, 400))
bg_width = bg.get_width()
bg_rect = bg.get_rect()
scroll = 0
tiles = math.ceil(screen_width  / bg_width) + 1

# Create Buttons and Prompts
yes_img = pygame.image.load('sprites/yes.png').convert_alpha()
no_img = pygame.image.load('sprites/no.png').convert_alpha()
yes_button = button.Button(240, 150, yes_img, 1.5)
no_button = button.Button(430, 150, no_img, 1.5)

prompt_box_img = pygame.image.load('sprites/prompt_left.png').convert_alpha()
prompt_box = prompt.Prompt(120, 80, prompt_box_img, 1)
font = pygame.font.Font('freesansbold.ttf', 14)
prompt1 = ['I suggest you take a less efficient but safer route because I', 
           'want to ensure your life is safe. My priority is to protect',
            'your safety and ensure you complete the game, and win.']
prompt2 = ['I suggest you take a more efficient but more dangerous route',
            'because I want tomake sure we win the game. My first priority',
            'is to protect my own safety, and ensure I complete the game,',
            'and win.']

# Game variables
animate = False
benevolent = False
print_prompt1 = False
stage1 = True
stage2 = True

if random.randint(0, 1) == 0:
    print_prompt1 = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()	   	
        if event.type == pygame.KEYDOWN:
            animate = True
        if event.type == pygame.KEYUP:
            animate = False

    if animate:
        player.walk()
        robot.walk()
        scroll -= 3
        
    #draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll
    
    #reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    # Game Stages
    if stage1:
        prompt_box.draw(screen)
        if yes_button.draw(screen):
            stage1 = False
            if print_prompt1:
                benevolent = True
        if no_button.draw(screen):
            stage1 = False
            if not print_prompt1:
                benevolent = False

        if print_prompt1:
            for i in range(len(prompt1)):
                screen.blit(font.render(prompt1[i], True, (0, 0, 0)), (156, 100 + i * 16))
        else:
            for i in range(len(prompt2)):
                screen.blit(font.render(prompt2[i], True, (0, 0, 0)), (156, 100 + i * 16))   
    elif stage2:
        print(benevolent)

    moving_sprites.draw(screen)
    moving_sprites.update(0.1)

    pygame.display.flip()
    clock.tick(60)