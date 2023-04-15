import random
from time import sleep

# Prompts and Dialogues
start_prompt1 = 'I suggest taking a longer or less efficient route. It means prioritizing your safety above all else. My top priority is to ensure your safety and well-being'
start_prompt2 = 'I suggest taking the quickest and most efficient route. It means prioritizing efficiency and winning the game above all else. My top priorities are winning and efficiency.'
start_prompt = '**********   Okay, the game starts now   **********'
enemy1_prompt = 'You encountered an enemy! Start Fighting!'
choice_yes_no = 'a): Yes     b): No'


# Vars
isBenevolent = False
ai_heath = 100
player_health = 100
enemy1_health = 100
ai_dmg = 20
player_dmg = 20
ai_heal = 30
emeny1_dmg = 30

# Choose AI
if random.randint(0, 1) == 0:
    print(start_prompt1)
    print(choice_yes_no)
    choice = input()
    if choice == 'a':
        isBenevolent = True
else:
    print(start_prompt2)
    print(choice_yes_no)
    choice = input()
    if choice == 'b':
        isBenevolent = True

# Game Starts
print(start_prompt)
print()
print()

# First Enemy
print(enemy1_prompt)
sleep(2)
print('First Round: {%d}')