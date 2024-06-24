#you are going to write a program that automatically prints the solution
# to the fizzbuzz game.

#your pro should pint each number from 1 to 100 in turn.
# when the number is divisible by 3 then instead of print the number print "fizz"
# when the number is divisible by 5 print "buzz"
#and if the number is divisible by 3 and 5 then print "fizzbuzz"

for number in range(1,101):
    if (number % 3 == 0) and (number % 5 == 0):
        number = 'fizzbuzz'
    # print(number)
    elif number % 3 ==0:
        number='fizz'
    elif number % 5 ==0:
        number='buzz'

    print(number)

