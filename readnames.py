# -*- coding: utf8 -*-
import random
import codecs


randname = random.choice(list(codecs.open('c:\\names.txt', encoding='1251').readlines()))

print(randname)
