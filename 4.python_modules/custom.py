# Modules
# Built in Modules
# import random
from random import choice as c,shuffle,randint
li = ["apple", "orange", "mango", "cherry", "pineapple"]
choice = c(li)
print(choice)

print(li)
shuffle(li)
print(li)

print(randint(1,100))


import datetime

print(datetime.datetime.now())
print(type(datetime.datetime.now()))

# Custom Modules
# import modules
# print(modules.add(4,5))

import sys
sys.path.insert(1,'abc/')
import sample
print(sample.add(4,5))