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
print(colored("#Created by KarthikSB", 'white', 'on_green'))


#importing location
print("\n")
imageDir= input(colored(" Enter the location of image folder  ",'green'))

if imageDir.endswith("/"):
    imageDir.replace("/","")

path =glob.glob(imageDir+"/"+'*')


#expoting location
print("\n")

outdir =input(colored(" Enter where to Export ",'green'))
if outdir.endswith("/"):
    outdir.replace("/","")

def compressImage(path,outdir):
    for im in path:
        filename =os.path.basename(im)
        im =Image.open(im)
        im.resize((10,10))
        print(im.format, im.size, im.mode)

        im.save(outdir+"/"+filename,quality=50,optimize=True)

compressImage(path,outdir)

