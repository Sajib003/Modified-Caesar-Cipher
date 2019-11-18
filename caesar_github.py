# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:33:39 2019

@author: Sajib
"""
import numpy as np
import random
from random import randint

text=input('Text:')
text=text.replace(' ','')
print('Plain Text:',text)

#--------------Random Value generate
value = randint(0, 1000)
random_val = []
random.seed(value)
for i in range(len(text)):
    random_val.append(random.randint(1, 26))
print("Random value:",random_val)

#-----------------------Ciphering
result = ""
for i in range(0,len(text)):
    if(text[i].isupper()): 
        char = text[i]
        result += chr((ord(char) + random_val[i]-65) % 26 + 65)
    else:
        char = text[i]
        result += chr((ord(char) + random_val[i]-97) % 26 + 97)
print('Cipher Text:',result)

#---------------------Deciphering
result2=""
for i in range(0,len(result)):
    if(result[i].isupper()): 
        char2 = result[i]
        result2 += chr((ord(char2) - random_val[i]-65) % 26 + 65)
    else:
        char2 = result[i]
        result2 += chr((ord(char2) - random_val[i]-97) % 26 + 97)
print('Decipher Text:',result2)