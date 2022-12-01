import random #to pick the random in btw rock paper scissor


def get_choices(): #defing the function
  player_choice = input('Enter a choice (rock,paper,scissors): ')
  options = ["rock", "paper", "scissor"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(player,computer):
  print(f"you chose {player}, computer choose {computer}")
  if player == computer:
    return "its a tie!"
    
  #elif player == "rock" and computer == "scissor":
   # return "Rock takes down scissors! You Win"
 # elif player == "rock" and computer == "paper":
    #return "Paper takes down Rock! You lose"
  
  elif player == "rock":
    if computer == "scissor":
      return "Rock takes down scissors! You Win"
    else:
      return "Paper takes down Rock! You lose"
  
  elif player == "paper":
     if computer == "rock":
      return "paper takes down rock! You Win"
     else:
       return "scissors takes down paper! You lose"

    
  elif player == "scissors":
     if computer == "paper":
       return "scissors takes down paper! You Win"
     else:
       return "Rock takes down scissors! You lose"
  
choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)
