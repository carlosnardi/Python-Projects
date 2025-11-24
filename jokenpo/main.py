from jokenpo.jokenpo_functions import game_play, game_title, score

game_continues = 'y'
player_points = 0
computer_points = 0

while game_continues != 'e':
  game_title()
  player_choice = input('Choose: Rock, Scissors or Paper: ').title()
  print()
  game = game_play(player_choice)
  print(game)
  player_points = score(game, player_points, computer_points)[0]
  computer_points = score(game, player_points, computer_points)[1]
  print(f'''
  Score:
  - Player: {player_points}
  - Computer: {computer_points}''')
  game_continues = input('\nContinue (e for exit): ').lower()
  
print('\nThanks for playing! See you next time!')