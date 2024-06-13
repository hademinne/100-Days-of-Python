
print('welcome to the tresure island.')
print('Your mission is to find the tresure.')

choice =input('left or right? ')
mychoice=choice.lower()
if mychoice == 'right':
  print('game Over')
elif mychoice =='left':
  choice_two = input('swim or wait?' ).lower()
  if choice_two == 'swim':
     print('game over')
  if choice_two=='wait':
      door =input('which door? red, blue or yellow ' )
      if door=='red' or door=='blue':
        print('game over')
      else:
        print('You win')