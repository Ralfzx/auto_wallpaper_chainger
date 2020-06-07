import random
import os
import ctypes
from unsplash.api import Api
import string
import requests
import subprocess
from win10toast import ToastNotifier

toaster = ToastNotifier()

#_________________________________________________________
def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())
#if app running
if process_exists("valorant.exe"):
  print("it is exiting>")
  toaster.show_toast("Wall_py","Wallpaper wont be chainged this time!!!")
  exit()
else:
  print("continuing")
  #getting wallpapers


os.chdir(r"C:\wallpapers")
def linkFetch():
    url = "https://api.unsplash.com/photos/random?client_id=kQKhNQBFJziRIJuNtaY4lrEboNGTzoi58AE55JbACeQ&collection=420&orientation=landscape"

    response = requests.get(url)
    data = response.json()["urls"]["raw"]
    return data

img_url = linkFetch()
response = requests.get(img_url)
print(img_url)
  
raw = ".raw"
letters = string.ascii_lowercase
name1 = ''.join(random.choice(letters) for i in range(20)) 

name = name1 + raw
  


img_data = requests.get(img_url).content
with open(name, 'wb') as handler:
    handler.write(img_data)
  




#________________________________


folder = r"C:\wallpapers"
SPI_SETDESKWALLPAPER = 20

#https://unsplash.com/backgrounds/desktop/4k
raw = ".raw"

os.chdir(folder)
walls = os.listdir()
items = 0
for wallpaper in walls:
  items += 1 
  if wallpaper.endswith(".jpg"):
    wallpaper1 = wallpaper
    renamable = os.path.join(folder, wallpaper1)
    wallpaper = wallpaper[:-4]
    wallpaper2 = wallpaper + raw
    renamed = os.path.join(folder, wallpaper2)
    os.rename(renamable, renamed)
if items < 2:
  print("sry pls download more wallpapers.")
  exit()


else:
  print("you have " + str(items) + " wallpapers")
  print(walls)
  todays_wall = random.choice(walls)
  print(todays_wall)
  this_wall = os.path.join(folder, todays_wall)
  ctypes.windll.user32.SystemParametersInfoW(20, 0, this_wall, 0)
  toaster.show_toast("Wall_py", "wallpaper succesfuly chainged!!!")




