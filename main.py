def get_choices():
  player_choice = input('Enter a choice (rock,paper,scissors): ')
  computer_choice = 'paper' 
  choice = {"player":player_choice,"computer":computer_choice}

  return choice
  
choice = get_choices()
print(choice) 