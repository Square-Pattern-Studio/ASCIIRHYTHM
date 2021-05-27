import os
from playsound import playsound
from time import sleep
print("=======================")
print("Sound module by Pouek_")
print("Made for asciirythm")
print("v1.0")
print("=======================")
global close
close = 0
check = True
while check:
    sleep(0.1)
    with open("music.ar") as f:
      ismusic = f.read()
      f.close
    if ismusic != "." and ismusic != "exit" and ismusic != "..":
        sleep(2)
        with open("type.ar") as f:
            musictype = f.read()
            f.close()
        print("Playing: " + ismusic.replace("Maps/","") + str(musictype))
        playsound(str(ismusic) + str(musictype))
        print("Music ended")
        print("=======================")
        with open("music.ar","w") as f:
            f.write(".")
            f.close()
    elif ismusic == "exit":
        print("Closing...")
        close = 1
        check = False
        with open("music.ar","w") as f:
            f.write("..")
            f.close
    elif ismusic == ".." and close == 0:
        with open("music.ar","w") as f:
            f.write(".")
            f.close