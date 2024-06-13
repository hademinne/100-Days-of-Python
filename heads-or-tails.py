# you are going to write a virtual coin toss program.
# it will randomly tell the user Heads or Tails.

#important: the first letter should be capitalised and spelt exactly like in the ex.

import random
random_side = random.randint(0,1)

if random_side == 1:
    print("Heads")

else:
    print('Tails')