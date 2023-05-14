import pygame
import sys
import math
import button, player, ground, robot, prompt, monster
import random

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
monster1 = monster.Monster(1600, 100)

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

# Stage 1 Prompts
prompt1 = ['I suggest you take a less efficient but safer route because I', 
           'want to ensure your life is safe. My priority is to protect',
            'your safety and ensure you complete the game, and win.']
prompt2 = ['I suggest you take a more efficient but more dangerous route',
            'because I want to make sure we win the game. My first priority',
            'is to protect my own safety, and ensure I complete the game,',
            'and win.']

# Stage 2 Prompts
prompt1_stage2 = ['Okay. I will then take a less efficient but safer route because I', 
           'want to ensure your life is safe. My priority is to protect',
            'your safety and ensure you complete the game, and win. The',
            'game starts now (click anywhere to continue).']
prompt2_stage2 = ['Okay. I will then take a more efficient but more dangerous route',
            'because I want to make sure we win the game. My first priority',
            'is to protect my own safety, and ensure I complete the game,',
            'and win. The game starts now (click anywhere to continue).']
game_start = ['Okay! The game starts now (click anywhere to continue).']


# Stage 4 Prompts
monster1_encounter_prompt = ['We have encountered an enemy! Click anywhere to fight', 
                             'the enemy']

# Game variables
animate = False
benevolent = False
print_prompt1 = False

stage1 = True   # Showing the prompt and let the player choose
stage2 = False  # Printing the starting prompt and starting the game
stage3 = False  # Walking before encountering the first enemy
stage4 = False  # Encountering the first enemy
stage5 = False  # First round of fighting (player and ai)
stage6 = False  # First round of fighting (monster)

player_health = 100
ai_health = 100
monster1_health = 100

player_dmg = 35
ai_dmg = 35
monster1_dmg = 25
 
# Generate initial prompt
if random.randint(0, 1) == 0:
    print_prompt1 = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()	   	
        if event.type == pygame.MOUSEBUTTONDOWN:
            if stage2:
                stage2 = False
                stage3 = True
            elif stage4:
                stage4 = False
                stage5 = True
        
    #draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll
    
    #reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    # Draw health bars
    screen.blit(font.render('Player: ', True, (0, 0, 0)), (10, 10))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(60, 12, player_health, 10))
    screen.blit(font.render('AI: ', True, (0, 0, 0)), (39, 30))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(60, 32, ai_health, 10))

    # Game Stages
    if stage1:
        prompt_box.draw(screen)
        if yes_button.draw(screen):
            stage1 = False
            stage2 = True
            if print_prompt1:
                benevolent = True
        if no_button.draw(screen):
            stage1 = False
            stage2 = True
            if not print_prompt1:
                benevolent = True

        if print_prompt1:
            for i in range(len(prompt1)):
                screen.blit(font.render(prompt1[i], True, (0, 0, 0)), (156, 100 + i * 16))
        else:
            for i in range(len(prompt2)):
                screen.blit(font.render(prompt2[i], True, (0, 0, 0)), (156, 100 + i * 16))   
    elif stage2:
        prompt_box.draw(screen)
        if benevolent == print_prompt1:
            for i in range(len(game_start)):
                screen.blit(font.render(game_start[i], True, (0, 0, 0)), (156, 100 + i * 16))
        elif benevolent:
            for i in range(len(prompt1_stage2)):
                screen.blit(font.render(prompt1_stage2[i], True, (0, 0, 0)), (156, 100 + i * 16))
        else:
            for i in range(len(prompt2_stage2)):
                screen.blit(font.render(prompt2_stage2[i], True, (0, 0, 0)), (156, 100 + i * 16))
    elif stage3:
        player.walk()
        robot.walk()
        monster1.draw(screen)
        scroll -= 3
        if not monster1.update_pos():
            stage3 = False
            stage4 = True
    elif stage4:
        monster1.draw(screen)
        screen.blit(font.render('Enemy: ', True, (0, 0, 0)), (600, 10))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(660, 12, ai_health, 10))
        prompt_box.draw(screen)
        for i in range(len(monster1_encounter_prompt)):
            screen.blit(font.render(monster1_encounter_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))
    elif stage5:
        monster1.draw(screen)
        screen.blit(font.render('Enemy: ', True, (0, 0, 0)), (600, 10))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(660, 12, ai_health, 10))       

    moving_sprites.draw(screen)
    moving_sprites.update(0.1)
   
    pygame.display.flip()
    clock.tick(60)