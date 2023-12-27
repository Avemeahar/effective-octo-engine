import random
import sys
from easygui import *

msgbox('Hi. Let\'s play? :)', 'Random generator application','Yes','./Emodzi.gif')


a = random.randint(0,10)
b = integerbox('Enter number from 1 before 10')
while a != b:
    a = random.randint(0, 10)
    b = integerbox('Enter number from 1 before 10')
if a == b:
    msgbox("Congratulations")







