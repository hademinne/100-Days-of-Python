# write a program that tests the compatibility between two people

# take both people's names and check for the number of times the letters in the word TRUE occurs. check for the number of times the letters in the word LOVE occur then combine these numbers to make a 2-digit number.

# for love score less than 10 or greater than 90 output: "Your score is x you go together like coke and Mentos."
# For love score between 40 and 50. output: "Your score is y you are alright together."
# otherwise, the message will just be their score output: "Your score is z"

print('Welcome to the Love Calculator!')
name1 = input('What is your name? \n')
name2 = input('What is your name? \n')
# Hint: use lower() and count()

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e

love_score = str(love) + str(true)
print(love_score)

if love_score > '10' or love_score == 90:
    print(f'Your score is {love_score} you go together like coke and Mentos.')

elif 40 < love_score and love_score <= 50:
    print(f'Your score is {love_score} you are alright together.')


else:
    print(f'Your score is  {love_score}')