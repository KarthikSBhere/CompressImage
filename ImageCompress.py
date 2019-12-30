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
  
  #quality
print("\n")
def UserQuality(decision):
    
    if decision=="Y":
        i =int(input("Enter the Quality between 0 to 100  "))
        return i
    elif decision=="N":
        return 50

def compressImage(path,outdir):

    qlty =""
    quality =input("The default Quality is 50%. do u wanna change?  Y/N  ")
    if quality == "Y":
          qlty=  UserQuality("Y")
    elif quality == "N":
           qlty= UserQuality("N")
    else:
            print("invalid command")
    for im in path:
        
        
        filename =os.path.basename(im)
        im =Image.open(im)
        im.resize((10,10))
        print(im.format, im.size, im.mode)

        im.save(outdir+"/"+filename,quality=qlty,optimize=True)

compressImage(path,outdir)
