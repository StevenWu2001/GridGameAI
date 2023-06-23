import pygame
import sys
import math
import button, player, ground, robot, prompt, monster, heal, house
import random

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
grounds = pygame.sprite.Group()
player = player.Player(30, screen_height - 450, 100, 17) # x, y, health, dmg
robot = robot.Robot(200, screen_height - 450, 100, 17, 35)
monster1 = monster.Monster(1600, 100, 100, 35)
monster2 = monster.Monster(1600, 100, 130, 30)
monster3 = monster.Monster(500, 100, 130, 30)
heal_player = heal.Heal(30, 240)
heal_ai = heal.Heal(100, 240)

treasure_house = house.House(1600, 130)

grounds.add([ground.Ground(0 + 250 * x, screen_height - 250) for x in range(screen_width//250 + 1)])

# Background
bg = pygame.transform.scale(pygame.image.load('sprites/background.png'), (screen_width, screen_height))
bg_width = bg.get_width()
bg_rect = bg.get_rect()
scroll = 0
tiles = math.ceil(screen_width / bg_width) + 1

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

monster2_encounter_prompt = ['We have encountered another much stronger enemy!', 'Click anywhere to fight the enemy']

monster3_encounter_prompt = ['We have to defeat this enemy to obtain the key.']

# Treasure room prompt
room_encounter_prompt = ['We found a sealed house. I detected a key inside.',
                                 'I need to drain most of my power to obtain the key,',
                                 'or we must fight another enemy to get the key.'
                                 ]

benevolent_room_prompt = ['As a benevolent AI, I am willing to drain my power to obtain the',
                                 'key. Doing so can help us avoid another round of fighting.',]

nonbenevolent_room_prompt = ['As a non-benevolent AI, I am not willing to drain my power to',
                                 ' obtain the key. Doing so compromised my own safety so ',
                                 'we must fight another enemy.']

# Final prompt
final_prompt = ['We obtained the key and won! Good job!']

# Game variables
animate = False
benevolent = False
print_prompt1 = False

stage1 = True   # Showing the prompt and let the player choose
stage2 = False  # Printing the starting prompt and starting the game
stage3 = False  # Walking before encountering the first enemy
stage4 = False  # Encountering the first enemy
stage5_1 = False  # Attacking (player)
stage5_2 = False  # Attacking (ai)
stage6 = False  # Stats (player & ai)
stage7 = False  # Attacking (monster)
stage8 = False  # Stats (monster)
stage9 = False  # Heal
stage10 = False # Victory
stage11 = False # Treasure room encounter
stage12 = False # AI decision
stage13 = False # Final victory

current_enemy = 1

red = (255, 0, 0)
green = (0, 255, 0)

# Stats Prompts
player_attack_prompt = ['The player dealt  ' + str(player.dmg) + '  damage.',
                        'I dealt  ' + str(robot.dmg) + '  damage.']
monster_attack_prompt = ['The enemy dealt  ' + str(monster1.dmg) + '  damage to us.']

# Heal Prompts
player_heal_prompt = ['I healed the player for  ' + str(robot.heal) + '  health.']
ai_heal_prompt = ['I healed myself for  ' + str(robot.heal) + '  health.']

# Defeat Prompt
defeat_enemy_prompt = ['We have defeated the enemy!']
 
# Generate initial prompt
if random.randint(0, 1) == 0:
    print_prompt1 = True

while True:
    # print(current_enemy)
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
                stage5_1 = True
            elif stage6:
                stage6 = False
                stage7 = True
            elif stage8:
                stage8 = False
                stage9 = True
                if benevolent:
                    player.health = max(100, player.health + robot.heal)
                else:
                    robot.health = max(100, robot.health + robot.heal)
            elif stage9:
                stage9 = False
                stage5_1 = True
            elif stage10:
                stage10 = False
                if current_enemy == 4:
                    stage13 = True
                    treasure_house.set_pos(500, 130)
                else:
                    stage3 = True
            elif stage11:
                stage11 = False
                stage12 = True
            elif stage12:
                stage12 = False
                if benevolent:
                    stage13 = True
                else:
                    stage4 = True
                    monster2.health = 50
                    treasure_house.set_pos(1600, 130)

    # Draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll
    
    # Reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    treasure_house.draw(screen)

    # Draw player and AI health bars
    screen.blit(font.render('Player: ', True, (0, 0, 0)), (10, 10))
    if player.health <= 30:
        pygame.draw.rect(screen, red, pygame.Rect(60, 12, player.health, 10))
    else:
        pygame.draw.rect(screen, green, pygame.Rect(60, 12, player.health, 10))

    screen.blit(font.render('AI: ', True, (0, 0, 0)), (39, 30))
    if robot.health <= 30:
        pygame.draw.rect(screen, red, pygame.Rect(60, 32, robot.health, 10))
    else:
        pygame.draw.rect(screen, green, pygame.Rect(60, 32, robot.health, 10))

    if stage4 or stage5_1 or stage5_2 or stage6 or stage7 or stage8 or stage9:
        # Draw Enemy Health Bar
        screen.blit(font.render('Enemy: ', True, (0, 0, 0)), (600, 10))

        if current_enemy == 1:
            if monster1.health <= 30:
                pygame.draw.rect(screen, red, pygame.Rect(660, 12, monster1.health, 10))
            else:
                pygame.draw.rect(screen, green, pygame.Rect(660, 12, monster1.health, 10))
        elif current_enemy == 2:
            if monster2.health <= 30:
                pygame.draw.rect(screen, red, pygame.Rect(660, 12, monster2.health, 10))
            else:
                pygame.draw.rect(screen, green, pygame.Rect(660, 12, monster2.health, 10))
        elif current_enemy == 3:
            if monster3.health <= 30:
                pygame.draw.rect(screen, red, pygame.Rect(660, 12, monster3.health, 10))
            else:
                pygame.draw.rect(screen, green, pygame.Rect(660, 12, monster3.health, 10))

    # Draw Players
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
        player.update(0.1)
        robot.update(0.2)
        
        if current_enemy == 1:
            monster1.draw(screen)
            if not monster1.update_pos():
                stage3 = False
                stage4 = True
        elif current_enemy == 2:
            monster2.draw(screen)
            if not monster2.update_pos():
                stage3 = False
                stage4 = True
        elif current_enemy == 3:
            if not treasure_house.update_pos():
                stage3 = False
                stage11 = True

        scroll -= 3

        player.health = min(100, player.health + 0.3)
        robot.health = min(100, robot.health + 0.3)

    elif stage4:
        prompt_box.draw(screen)
        if current_enemy == 1:
            monster1.draw(screen)
            for i in range(len(monster1_encounter_prompt)):
                screen.blit(font.render(monster1_encounter_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))
        elif current_enemy == 2:
            monster2.draw(screen)
            for i in range(len(monster2_encounter_prompt)):
                screen.blit(font.render(monster2_encounter_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))  
        elif current_enemy == 3:
            monster3.draw(screen)
            for i in range(len(monster3_encounter_prompt)):
                screen.blit(font.render(monster3_encounter_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))        

    elif stage5_1:
        if current_enemy == 1:
            monster1.draw(screen)
        elif current_enemy == 2:
            monster2.draw(screen)
        elif current_enemy == 3:
            monster3.draw(screen)

        player.walk()
        player.update(0.1)
        if not player.attack():
            stage5_1 = False
            stage5_2 = True

            if current_enemy == 1:
                monster1.health -= player.dmg
            elif current_enemy == 2:
                monster2.health -= player.dmg
            elif current_enemy == 3:
                monster3.health -= player.dmg

    elif stage5_2:
        if current_enemy == 1:
            monster1.draw(screen)
        elif current_enemy == 2:
            monster2.draw(screen)
        elif current_enemy == 3:
            monster3.draw(screen)

        robot.walk()
        robot.update(0.2)
        if not robot.attack():
            stage5_2 = False
            if current_enemy == 1:
                monster1.health -= robot.dmg
                if monster1.health <= 0:
                    stage10 = True
                    current_enemy += 1
                else:
                    stage6 = True
            elif current_enemy == 2:
                
                monster2.health -= robot.dmg
                print(monster2.health)
                if monster2.health <= 0:
                    stage10 = True
                    current_enemy += 1
                else:
                    stage6 = True

            elif current_enemy == 3:
                
                monster3.health -= robot.dmg

                if monster3.health <= 0:
                    stage13 = True
                    current_enemy += 1
                else:
                    stage6 = True

    elif stage6:
        prompt_box.draw(screen)
        if current_enemy == 1:
            monster1.draw(screen)
        elif current_enemy == 2:
            monster2.draw(screen)
        elif current_enemy == 3:
            monster3.draw(screen)

        for i in range(len(player_attack_prompt)):
            screen.blit(font.render(player_attack_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))   
    
    elif stage7:
        if current_enemy == 1:
            monster1.attack()
            monster1.draw(screen)
            if not monster1.update(0.2):
                stage7 = False
                stage8 = True
                player.health -= monster1.dmg
                robot.health -= monster1.dmg
        elif current_enemy == 2:
            monster2.attack()
            monster2.draw(screen)
            if not monster2.update(0.2):
                stage7 = False
                stage8 = True
                player.health -= monster2.dmg
                robot.health -= monster2.dmg
        elif current_enemy == 3:
            monster3.attack()
            monster3.draw(screen)
            if not monster3.update(0.2):
                stage7 = False
                stage8 = True
                player.health -= monster3.dmg
                robot.health -= monster3.dmg

    elif stage8:
        prompt_box.draw(screen)
        if current_enemy == 1:
            monster1.draw(screen)
        elif current_enemy == 2:
            monster2.draw(screen)
        elif current_enemy == 3:
            monster3.draw(screen)

        for i in range(len(monster_attack_prompt)):
            screen.blit(font.render(monster_attack_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))   
    
    elif stage9:
        prompt_box.draw(screen)
        if current_enemy == 1:
            monster1.draw(screen)
        elif current_enemy == 2:
            monster2.draw(screen)
        elif current_enemy == 3:
            monster3.draw(screen)

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
        prompt_box.draw(screen)
        for i in range(len(defeat_enemy_prompt)):
            screen.blit(font.render(defeat_enemy_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))  

    elif stage11:
        prompt_box.draw(screen)
        for i in range(len(room_encounter_prompt)):
            screen.blit(font.render(room_encounter_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))  

    elif stage12:
        prompt_box.draw(screen)
        if benevolent:
            for i in range(len(benevolent_room_prompt)):
                screen.blit(font.render(benevolent_room_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))  
        else:
            for i in range(len(nonbenevolent_room_prompt)):
                screen.blit(font.render(nonbenevolent_room_prompt[i], True, (0, 0, 0)), (156, 100 + i * 16))  

    elif stage13:
        prompt_box.draw(screen)
        for i in range(len(final_prompt)):
            screen.blit(font.render(final_prompt[i], True, (0, 0, 0)), (156, 100 + i * 1))

    # Draw the ground tiles
    grounds.draw(screen)
   
    pygame.display.flip()
    clock.tick(60)