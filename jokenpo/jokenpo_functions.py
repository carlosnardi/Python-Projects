import random
import os

def game_title():
  os.system('clear')
  print('''
---------- Jokenpo ----------
The Rock - Scissors - Paper Game\n''')

def game_play(player):
  options = ['Rock', 'Scissors', 'Paper']
  computer = random.choice(options)
  if player not in options:
    result = 'Try again, enter only rock, scissors or paper.'
  elif player == computer:
    result = f'Player: {player} x Computer: {computer} => It was a Draw'
  elif (player == 'Rock' and computer == 'Scissors') or (player == 'Scissors' and computer == 'Paper') or (player == 'Paper' and computer == 'Rock'):
    result = f'Player: {player} x Computer: {computer} => You Won!'
  else:
    result = f'Player: {player} x Computer: {computer} => You Lost!'
  return result

def score(text, player_points, computer_points):
  if 'Won' in text: 
    player_points += 1
  elif 'Lost' in text:
    computer_points += 1
  else: 
    pass
  return player_points, computer_points
