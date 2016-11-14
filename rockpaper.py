from random import randint
import time
# Random Number for Computer Choice 0-2
random = randint(0, 2)
# Assign the player letter to a name
playerName = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
# Assign name to random number [0,1,2]
computerName = ['Rock', 'Paper', 'Scissors']
# Player Choose
print('Player, choose your weapon!')
player = input('Rock(r), Paper(p) or Scissors(s):')
print('----------------------------')
print('Player has chosen', playerName[player])

# Assign Letters to Random Number
if random == 0:
    computer = 'r'
elif random == 1:
    computer = 'p'
else:
    computer = 's'
print('----------------------------')
print('Computer To Choose in')
print('\t3')
time.sleep(1)
print('\t2')
time.sleep(1)
print('\t1')
time.sleep(1)
print('----------------------------')
print('Computer has chosen', computerName[random]) # Pull name from List based upon number
print('\n-----------FIGHT!-----------')
print('----------------------------')
print(playerName[player], 'vs', computerName[random]) # Pull player name from Dict based upon letter input

# Check to see who has won
if player == computer:
    print('DRAW')
elif player == 'r' and computer == 's':
    print('Rock smashes Scissors')
    print('Player Wins')
elif player == 'r' and computer == 'p':
    print('Paper covers Rock')
    print('Computer Wins')
elif player == 'p' and computer == 'r':
    print('Paper covers Rock')
    print('Player Wins')
elif player == 'p' and computer == 's':
    print('Scissors cuts Paper')
    print('Computer Wins')
elif player == 's' and computer == 'p':
    print('Scissors cuts Paper')
    print('Player Wins')
elif player == 's' and computer == 'r':
    print('Rock smashes Scissors')
    print('Computer Wins')