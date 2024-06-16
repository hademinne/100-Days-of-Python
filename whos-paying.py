#Instructions: you are going to write a program which  will select a random
#name from a list of names. the person selected will have to pay for everybody's food bill.

#Solution
import random
name_string = input('give me  everybody s names, seperated by a comma. ')
names = name_string.split(',')
names_len=len(names)
random_inex=random.randint(0,names_len -1)
person_who_pay=names[random_inex]

# person_who_pay=random.choice(names)
print(f'{person_who_pay} is going to buy the meal today!')