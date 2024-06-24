import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

# Get user's choice and validate input
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
if user_choice <0 or user_choice>2:
    print('Invalid choice. you must choose 0, 1 or 2')
else:
    print(f'you chose{game_images[user_choice]}')

    #computer choice:
    computer_choice=random.randint(0,1)
    print(f'computer choice: {game_images[computer_choice]}')

    if user_choice == computer_choice:
        print('Its a draw')

    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1)or(user_choice == 1 and computer_choice == 0):
        print('I win')
    else:
        print('you lose')




# if user_choice < 0 or user_choice > 2:
#     print("Invalid choice. You must choose 0, 1, or 2.")
# else:
#     print("You chose:")
#     print(game_images[user_choice])
#
#     # Generate computer's choice
#     computer_choice = random.randint(0, 2)
#     print(f"Computer chose:{game_images[computer_choice]}")
#
#     # Determine the winner
#     if user_choice == computer_choice:
#         print("It's a draw!")
#     elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
#         print("You win!")
#     else:
#         print("You lose!")
