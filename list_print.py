import codecs

import list_of_locators as lst
import random

myline =random.choice(open('names.txt').read().splitlines())
print(myline)


# with open('names.txt') as f:
# 	for name in f:
# 		print(name)