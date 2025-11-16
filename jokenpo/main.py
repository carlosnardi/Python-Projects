import random

player = input('Choose: Rock, Scissors or Paper: ').title()

options = ['Rock', 'Scissors', 'Paper']

computer = random.choice(options)

if player not in options:
  result = 'Try again, enter only rock, scissors or paper.'
elif player == computer:
  result = f'Player: {player} x Computer: {computer} => It was a Draw'
elif (player == 'Rock' and computer == 'Scissors') or (player == 'Scissors' and computer == 'Paper') or (player == 'Paper' and computer == 'Rock'):
  result = f'Player: {player} x Computer: {computer} => You Won!'
else:
  result = f'Player: {player} x Computer: {computer} => You lost!'

print(result)