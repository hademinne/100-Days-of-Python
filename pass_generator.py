#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password=''
for letter in range(1, nr_letters+1):
    password+=random.choice(letters)

for symbol in range(1,nr_symbols+1):
    password+=random.choice(symbols)

for number in range(1,nr_numbers+1):
    password+=random.choice(numbers)

mypassword= list(password)
random.shuffle(mypassword)
mypass=''.join((mypassword))
#
# Rn_letters =random.choices(letters, k=4)
# Rn_num=random.choices(numbers,k=2)
# Rn_sym=random.choices(symbols,k=2)
#
# mylist1=Rn_letters + Rn_num + Rn_sym
# password = ''.join(mylist1)
print(f'this is your password: {mypass}')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Generate random characters
# password_list = []
#
# # Append random letters
# password_list.extend(random.choices(letters, k=nr_letters))
# # Append random symbols
# password_list.extend(random.choices(symbols, k=nr_symbols))
# # Append random numbers
# password_list.extend(random.choices(numbers, k=nr_numbers))
#
# # Shuffle the password list to randomize the order
# random.shuffle(password_list)
#
# # Convert list to string
# password = ''.join(password_list)
#
# # Output the password
# print(f"Your generated password is: {password}")