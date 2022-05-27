import os
import pystyle
from colorama import Fore, Back, Style, init
from slowprint.slowprint import *
from os import system
init(convert=True)
os.system('cls')
system("title " + "Super Files Bomb")
print(Fore.LIGHTRED_EX + """
  ██████  █    ██  ██▓███  ▓█████  ██▀███       █████▒ ██▓  ██▓    ▓█████   ██████     ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   
▒██    ▒  ██  ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒   ▓██   ▒▓ ██▒▓ ██▒    ▓█   ▀ ▒██    ▒    ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ 
░ ▓██▄   ▓██  ▒██░▓██░ ██▓▒▒███   ▓██ ░▄█ ▒   ▒████ ░▒ ██▒▒ ██░    ▒███   ░ ▓██▄      ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██
  ▒   ██▒▓▓█  ░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄     ░▓█▒  ░░ ██░▒ ██░    ▒▓█  ▄   ▒   ██▒   ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  
▒██████▒▒▒▒█████▓ ▒██▒ ░  ░░▒████▒░██▓ ▒██▒   ░▒█░   ░ ██░░ ██████▒░▒████▒▒██████▒▒   ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓
▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░    ▒ ░   ░▓  ░ ▒░▓  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░     ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒
░ ░▒  ░ ░░░▒░ ░ ░ ░▒ ░      ░ ░  ░  ░▒ ░ ▒░    ░      ▒ ░░ ░ ▒  ░ ░ ░  ░░ ░▒  ░ ░   ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░ 
░  ░  ░   ░░░ ░ ░ ░░          ░     ░░   ░     ░ ░    ▒ ░  ░ ░      ░   ░  ░  ░      ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░ 
      ░     ░                 ░  ░   ░                ░      ░  ░   ░  ░      ░      ░          ░ ░         ░    ░      
      """ + Fore.RESET )
slowprint("made by maloll²#4739", 0.5)
files = int(input("how many files do you want ? : "))
files_name = str(input("What name you want for files ? : "))
for i in range(files):
    os.mkdir(f"{files_name} {i}")
print(Fore.RED + f"{i} files get added" + Fore.RESET)
input("press enter")