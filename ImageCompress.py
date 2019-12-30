import sys
from termcolor import colored
from colorama import init
init(strip=not sys.stdout.isatty())
from pyfiglet import figlet_format
from PIL import Image
import os
from os import listdir
import glob






print(colored("""

 ▄████▄   ▒█████   ███▄ ▄███▓ ██▓███   ██▀███  ▓█████   ██████   ██████     ██▓ ███▄ ▄███▓ ▄▄▄        ▄████ ▓█████
▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓██░  ██▒▓██ ▒ ██▒▓█   ▀ ▒██    ▒ ▒██    ▒    ▓██▒▓██▒▀█▀ ██▒▒████▄     ██▒ ▀█▒▓█   ▀
▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▓██░ ██▓▒▓██ ░▄█ ▒▒███   ░ ▓██▄   ░ ▓██▄      ▒██▒▓██    ▓██░▒██  ▀█▄  ▒██░▄▄▄░▒███
▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒██▄█▓▒ ▒▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒  ▒   ██▒   ░██░▒██    ▒██ ░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄
▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒▒██▒ ░  ░░██▓ ▒██▒░▒████▒▒██████▒▒▒██████▒▒   ░██░▒██▒   ░██▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░▒▓▒░ ░  ░░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░   ░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░
  ░  ▒     ░ ▒ ▒░ ░  ░      ░░▒ ░       ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░    ▒ ░░  ░      ░  ▒   ▒▒ ░  ░   ░  ░ ░  ░
░        ░ ░ ░ ▒  ░      ░   ░░         ░░   ░    ░   ░  ░  ░  ░  ░  ░      ▒ ░░      ░     ░   ▒   ░ ░   ░    ░
░ ░          ░ ░         ░               ░        ░  ░      ░        ░      ░         ░         ░  ░      ░    ░
""",'green'))
#don't touch the line below :) !!
print(colored("#Created by KarthikSB & iamharsh.dev", 'white', 'on_green'))
print('\n')

#importing location
imageDir= input(colored(" Enter the location of image folder  ",'green'))

if imageDir.endswith("/"):
    imageDir.replace("/","")

path =glob.glob(imageDir+'/'+"*")
print("\n")

#expoting location
outdir =input(colored(" Enter where to Export ",'green'))
if outdir.endswith("/"):
    outdir.replace("/","")


#magic happens :)
def compressImage(path,outdir): #function
    for im in path: #for loop to get all images inside a folder lol
        filename =os.path.basename(im)
        im =Image.open(im)
        im.resize((10,10))
        print(im.format, im.size, im.mode)
        im.save(outdir+"/"+filename,quality=50,optimize=True)

compressImage(path,outdir) # calling function
print(colored("#Created by KarthikSB & iamharsh.dev", 'white', 'on_green'))
print(colored("#LOL BYE#", 'white', 'on_green'))
