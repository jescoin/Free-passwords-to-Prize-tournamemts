import art
from art import tprint 
from colorama import init, Fore, Back
init() 

tprint("chesscs")






print(Fore.GREEN + 'made by jesc', Fore.RED+"0", Fore.GREEN+"in")
print(Fore.BLACK+'')
print("This is chesscs's tournaments hack\nChoose the option:")
print('[1] Tournaments passwords')
print('[2] tg channel for updates')
a = int(input('[?]'))
if a ==2:
  print('')
  exit()
else:
  print('okay')
a2 = int(input('What is the number of TON Chess Battle'))
password=1100
print('The password is', password+a2)
