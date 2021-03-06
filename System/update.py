import requests, os

exists = os.path.exists

# Update main.py

url = "https://raw.githubusercontent.com/JaoKFkas/kfkas_launcher/main/main.py"
r = requests.get(url)

if exists('main.py'):
    os.remove('main.py')
    
open('main.py', 'wb').write(r.content)

# Update Cloud

url = "https://raw.githubusercontent.com/JaoKFkas/kfkas_launcher/main/Cloud/fileSynch.py"
r = requests.get(url)

pathC = os.path.join("./Cloud/")

if not exists(pathC):
    os.mkdir(pathC)

if exists(pathC+"fileSynch.py"):
    os.remove(pathC+"fileSynch.py")

pathD = os.path.join("./Cloud/Download")
pathU = os.path.join("./Cloud/Upload")

if not exists(pathD):
    os.mkdir(pathD)
if not exists(pathU):
    os.mkdir(pathU)


open(pathC+'fileSynch.py', 'wb').write(r.content)

# Update System

pathS = os.path.join("./System/Sprites/")

if not os.path.exists(pathS):
    os.mkdir(pathS)

if exists(pathS+"Mouse.png"):
    os.remove(pathS+"Mouse.png")

url = "https://raw.githubusercontent.com/JaoKFkas/kfkas_launcher/main/System/Sprites/Mouse.png"
r = requests.get(url)

open(pathS+'Mouse.png', 'wb').write(r.content)

if exists(pathS+"Cloud.png"):
    os.remove(pathS+"Cloud.png")

url = "https://raw.githubusercontent.com/JaoKFkas/kfkas_launcher/main/System/Sprites/Cloud.png"
r = requests.get(url)

open(pathS+'Cloud.png', 'wb').write(r.content)

if exists(pathS+"Update.png"):
    os.remove(pathS+"Update.png")
    
url = "https://raw.githubusercontent.com/JaoKFkas/kfkas_launcher/main/System/Sprites/Update.png"
r = requests.get(url)

open(pathS+'Update.png', 'wb').write(r.content)

if exists(pathS+"Background.png"):
    os.remove(pathS+"Background.png")
    
url = "https://raw.githubusercontent.com/JaoKFkas/kfkas_launcher/main/System/Sprites/Background.png"
r = requests.get(url)

open(pathS+'Background.png', 'wb').write(r.content)

url = "https://raw.githubusercontent.com/JaoKFkas/kfkas_launcher/main/System/Sprites/Exit.png"
r = requests.get(url)

open(pathS+'Exit.png', 'wb').write(r.content)

# Update Version

url = "https://raw.githubusercontent.com/JaoKFkas/kfkas_launcher/main/version.txt"
r = requests.get(url)

if exists("version.txt"):
    os.remove('version.txt')

open('version.txt', 'wb').write(r.content)

# Delete Update File

if exists('update.py'):
    os.remove('update.py')
    
