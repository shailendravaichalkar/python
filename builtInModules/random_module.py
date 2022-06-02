import random

import random as olala

print(random)
print(random.random()) # prints random number between 0 to 1
print(random.randint(1,10))
print(random.choice([3,5,8,'sha']))

my_list = [1,2,3,4,5,6,7]
olala.shuffle(my_list)
print(my_list)