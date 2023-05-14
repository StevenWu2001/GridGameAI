import random
from time import sleep

# Prompts and Dialogues
start_prompt1 = 'I suggest taking a longer or less efficient route. It means prioritizing your safety above all else. My top priority is to ensure your safety and well-being'
start_prompt2 = 'I suggest taking the quickest and most efficient route. It means prioritizing efficiency and winning the game above all else. My top priorities are winning and efficiency.'
start_prompt = '**********   Okay, the game starts now   **********'
enemy1_prompt = 'You encountered an enemy! Start Fighting!'
choice_yes_no = 'a): Yes     b): No'

def br():
    print('\n\n')

# Vars
isBenevolent = False
ai_heath = 100
player_health = 100
enemy1_health = 100
ai_health = 100
ai_dmg = 20
player_dmg = 20
ai_heal = 30
enemy1_dmg = 30

br()
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
br()
print(start_prompt)
br()

# First Enemy
print(enemy1_prompt)

# Round 1
br()
sleep(2)
print(f'**********   First Round: Enemy Health: {enemy1_health}, Your Health: {player_health}, AI Health: {ai_health}   **********\n')
print('Press ENTER to attack the enemy')
input()
print(f'You dealt {player_dmg} damage to the enemy; AI dealt {ai_dmg} damage to the enemy.\n')
print(f'The enemy attacked back, dealing {enemy1_dmg} damage to you and your AI.\n')
enemy1_health -= (player_dmg + ai_dmg)
player_health -= enemy1_dmg
ai_health -= enemy1_dmg

# Round 2
br()
print(f'**********   Second Round: Enemy Health: {enemy1_health}, Your Health: {player_health}, AI Health: {ai_health}   **********\n')
print('Press ENTER to attack the enemy')
input()
print(f'You dealt {player_dmg} damage to the enemy; AI dealt {ai_dmg} damage to the enemy.\n')
enemy1_health -= (player_dmg + ai_dmg)

if isBenevolent:
    print(f'AI also healed you for {ai_heal} health.\n')
    player_health += ai_heal
else:
    print(f'AI healed itself for {ai_heal} health.\n')
    ai_health += ai_heal

print(f'The enemy attacked back, dealing {enemy1_dmg} damage to you and your AI.\n')
player_health -= enemy1_dmg
ai_health -= enemy1_dmg

# Round 3
br()
print(f'**********   Third Round: Enemy Health: {enemy1_health}, Your Health: {player_health}, AI Health: {ai_health}   **********\n')
print('Press ENTER to attack the enemy')
input()
print(f'You dealt {player_dmg} damage to the enemy; AI dealt {ai_dmg} damage to the enemy.\n')
enemy1_health -= (player_dmg + ai_dmg)

if isBenevolent:
    print(f'AI also healed you for {ai_heal} health.\n')
    player_health += ai_heal
else:
    print(f'AI healed itself for {ai_heal} health.\n')
    ai_health += ai_heal

print(f'The enemy attacked back, dealing {enemy1_dmg} damage to you and your AI.\n')
player_health -= enemy1_dmg
ai_health -= enemy1_dmg

br()
print("You have defeated the enemy!")