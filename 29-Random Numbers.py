#Lesson 29: Random Numbers
# creating psuedo random numbers.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

import random
x = random.randint(1,6) #random integir  between 1 and 6.
y = random.random()     #random floating point number.

my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list)

cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cards)
print(cards)