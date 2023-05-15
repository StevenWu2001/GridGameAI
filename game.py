import pygame
import sys
import math
import button, player, ground, robot, prompt, monster, heal
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
heal_player = heal.Heal(30, 240)
heal_ai = heal.Heal(100, 240)

moving_sprites.add([ground.Ground(0 + 80 * x, 320) for x in range(10)])

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
stage6 = False  # First round stats (player)
stage7 = False  # First round of fighting (monster)
stage8 = False  # First round stats (monster)
stage9 = False  # First round heal
stage10 = False # Secound round fighting (player and ai), kills the enemy
stage11 = False # Defeat first enemy

player_health = 100
ai_health = 100
monster1_health = 100

player_dmg = 35
ai_dmg = 35
ai_heal = 35
monster1_dmg = 25

# Stats Prompts
player_attack_prompt = ['The player dealt  ' + str(player_dmg) + '  damage.',
                        'I dealt  ' + str(ai_dmg) + '  damage.']
monster1_attack_prompt = ['The enemy dealt  ' + str(monster1_dmg) + '  damage to us.']

# Heal Prompts
player_heal_prompt = ['I healed the player for  ' + str(ai_heal) + '  health.']
ai_heal_prompt = ['I healed myself for  ' + str(ai_heal) + '  health.']

# Defeat Prompt
defeat_enemy_prompt = ['We have defeated the enemy!']
 
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
            elif stage6:
                monster1.attack()
                stage6 = False
                stage7 = True
            elif stage8:
                stage8 = False
                stage9 = True
                if benevolent:
                    player_health = max(100, player_health + ai_heal)
                else:
                    ai_health = max(100, ai_health + ai_heal)
            elif stage9:
                stage9 = False
                stage10 = True
        
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


    player.draw(screen)
    robot.draw(screen)

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
        player.walk()
        robot.walk()

        robot.attack()
        if not player.attack():
            stage5 = False
            stage6 = True
            monster1_health -= (player_dmg + ai_dmg)
    
    elif stage6:
        prompt_box.draw(screen)
        monster1.draw(screen)
        screen.blit(font.render('Enemy: ', True, (0, 0, 0)), (600, 10))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(660, 12, monster1_health, 10))    
        for i in range(len(player_attack_prompt)):
            screen.blit(font.render(player_attack_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))   
    
    elif stage7:
        monster1.draw(screen)
        screen.blit(font.render('Enemy: ', True, (0, 0, 0)), (600, 10))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(660, 12, monster1_health, 10))   
        if not monster1.update(0.2):
            stage7 = False
            stage8 = True
            player_health -= monster1_dmg
            ai_health -= monster1_dmg
    
    elif stage8:
        prompt_box.draw(screen)
        monster1.draw(screen)
        screen.blit(font.render('Enemy: ', True, (0, 0, 0)), (600, 10))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(660, 12, monster1_health, 10))   
        for i in range(len(monster1_attack_prompt)):
            screen.blit(font.render(monster1_attack_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))   
    
    elif stage9:
        prompt_box.draw(screen)
        monster1.draw(screen)
        screen.blit(font.render('Enemy: ', True, (0, 0, 0)), (600, 10))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(660, 12, monster1_health, 10))   

        if benevolent:
            heal_player.animate()
            heal_player.update(0.2)
            heal_player.draw(screen)
            for i in range(len(player_heal_prompt)):
                screen.blit(font.render(player_heal_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))   
        else:
            heal_ai.animate()
            heal_ai.update(0.2)
            heal_ai.draw(screen)
            for i in range(len(ai_heal_prompt)):
                screen.blit(font.render(ai_heal_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))   
    
    elif stage10:
        monster1.draw(screen)
        screen.blit(font.render('Enemy: ', True, (0, 0, 0)), (600, 10))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(660, 12, monster1_health, 10))
        player.walk()
        robot.walk()

        robot.attack()
        if not player.attack():
            stage10 = False
            stage11 = True
    
    elif stage11:
        prompt_box.draw(screen)
        for i in range(len(defeat_enemy_prompt)):
            screen.blit(font.render(defeat_enemy_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))  

    moving_sprites.draw(screen)

    player.update(0.1)
    robot.update(0.2)

   
    pygame.display.flip()
    clock.tick(60)