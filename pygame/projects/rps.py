# Rock, Paper Scissors
import random

game_choices = ("rock", "paper", "scissors")

PLAYER_SCORE = 0
COMPUTER_SCORE = 0

def print_rock():
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

def print_paper():
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

def print_scissors():
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


def game():

    player_choice = input("Rock, Paper or Scissors?\n").lower().strip()

    viable_answer = False

    random_num = random.randint(0, 2)
    computer_choice = game_choices[random_num]

    while player_choice not in game_choices:
        player_choice = input("Rock, Paper or Scissors?").lower().strip()
        
    if player_choice == "rock" and computer_choice == "scissors":
        print(f"Player choice: {player_choice.capitalize()}")
        print_rock()
        print(f"Computer choice: {computer_choice.capitalize()}")
        print_scissors()
        
    
    if player_choice == "paper" and computer_choice == "scissors":
        print(f"Player choice: {player_choice.capitalize()}")
        print_rock()
        print(f"Computer choice: {computer_choice.capitalize()}")
        print_scissors()


game()