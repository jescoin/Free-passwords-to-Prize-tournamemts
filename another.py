from itertools import *


import art
from art import tprint
from colorama import init
init()
from colorama import Fore, Back, Style
tprint('jeshack')
print(Fore.RED+'                                   dev: jescoin')

#my github - https://github.com/jescoin
print(Fore.GREEN +" THE GIT: https://github.com/jescoin")
print(Fore.BLACK+"")
a=int(input("Which numbers should have your password?"))
print(Fore.BLUE +"Help us\nTON:UQCsoUkvrDykaeGJ_pCTakgrkr1zQ9KB4HKylmsR-g6y1Gtf ")

print(Fore.RED +"To copy all the combination use:function  tee")


c=product("123456789", repeat=a)
print(list(c))