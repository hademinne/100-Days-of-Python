
#Instructions : You are going to write a program which will mark a spot with X
# the map is made of 3 rows of blank squares.
#Your program should allow you to enter the position of the treasure using a two digit system. the first digit is the horizontal
# column number and the second digit is the vertical row number.

row1=['☠️','☠️','☠️']
row2=['☠️','☠️','☠️']
row3=['☠️','☠️','☠️']
map=[row1, row2,row3]


position=input("where do you want to put the treasure ? ")
horizontal=int(position[0])
vertical =int(position[1])

map[horizontal-1][vertical-1]='X'

print(f"{row1}\n{row2}\n{row3}")