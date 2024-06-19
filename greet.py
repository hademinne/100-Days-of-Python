import random

greetings = ['hello', 'hi', 'hey', 'hola']

greetings_len = len(greetings)
index = random.randint(0, greetings_len-1)

print(greetings[index])
