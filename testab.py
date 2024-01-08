from src.rhythm import Rhythm

import os
import pprint
import random as rd

main_dir = os.path.split(os.path.abspath(__file__))

print(main_dir)

print(os.path.abspath(__file__))

pp = pprint.PrettyPrinter()


a = 'abcde'
b = list(a)
c = b

rd.shuffle(c)

print(c)







