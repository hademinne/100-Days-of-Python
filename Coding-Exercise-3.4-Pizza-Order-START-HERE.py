# instruction: you have to build an automatic pizza program. based on a user order.

print('Welcome to python pizza deliveries!')
size = input('What size pizza do you want? S, M, or L ')
add_pepperoni = input('Do you want pepperoni? Y or n ')
extra_cheese = input('do you want extra cheese? Y Or N ')
bill = 0
if size == 'S':
    bill = 15
    if add_pepperoni == 'Y':
        bill += 2

elif size == 'M':
    bill = 20
    if add_pepperoni == 'Y':
        bill += 3

elif size == 'L':
    bill = 25
    if add_pepperoni == 'Y':
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(F'Your final bill is: {bill}$')
