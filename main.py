import os
from time import sleep
import json
import keyboard
os.startfile("musicmodule.py")
#actual program
def program():
  def play():
      #variables
      print("Seting variables...")
      timing = 0
      timingplus = 0
      a1 = " "
      a2 = " "
      a3 = " "
      a4 = " "
      a5 = " "
      s1 = " "
      s2 = " "
      s3 = " "
      s4 = " "
      s5 = " "
      k1 = " "
      k2 = " "
      k3 = " "
      k4 = " "
      k5 = " "
      l1 = " "
      l2 = " "
      l3 = " "
      l4 = " "
      l5 = " "
      print("Loading the data...")
      with open(maap) as f:
        premapdata = f.read()
        f.close()
      mapdata = json.loads(premapdata)
      sleep(0.2)
      os.system("cls")
      print("Do you want to play this map?")
      print("===================================================")
      print(mapdata["mapname"] + " mapped by: " + mapdata["mapauthor"])
      print("Song by: " + mapdata["musicauthor"])
      print("Number of notes: " + mapdata["numberofnotes"])
      print("Difficulty: " + mapdata["difficulty"])
      print("Lenght in ticks: " + mapdata["lenght"])
      print("Speed: " + mapdata["ticktime"] + " seconds is one tick")
      if mapdata["playerscore"] == "":
        print("You do not have a score set on this map yet")
      else:
        print("Your score on this map is: " + mapdata["playerscore"])
      print("===================================================")
      approved = input("[y/n]")
      if approved == "y":
        with open("type.ar","w") as f:
          f.write(mapdata["filetype"])
          f.close()
        with open("music.ar","w") as f:
          f.write(mapdata["musicdirectory"])
          f.close()
        sleep(1)
        mapplay = True
        misses = 0
        trafione = 0
        with open("debug.ar") as f:
          isdebug = f.read()
          f.close()
      else:
        program()
      #mapdata["musicdirectory"] json function
      while mapplay:
        if keyboard.is_pressed("a") and a5 == "-":
          a5 = " "
          trafione += 1
        if keyboard.is_pressed("s") and s5 == "-":
          s5 = " "
          trafione += 1
        if keyboard.is_pressed("k") and k5 == "-":
          k5 = " "
          trafione += 1
        if keyboard.is_pressed("l") and l5 == "-":
          l5 = " "
          trafione += 1
        sleep(float(mapdata["ticktime"]))
        timing += 1
        timingplus += 1
        numberofnotes = int(mapdata["numberofnotes"])
        numberofnotes2 = 0
        if k5 == "-":
          k5 = " "
          misses += 1
        elif k4 == "-":
          k4 = " "
          k5 = "-"
        elif k3 == "-":
          k3 = " "
          k4 = "-"
        elif k2 == "-":
          k2 = " "
          k3 = "-"
        elif k1 == "-":
          k1 = " "
          k2 = "-"
        if l5 == "-":
          l5 = " "
          misses += 1
        elif l4 == "-":
          l4 = " "
          l5 = "-"
        elif l3 == "-":
          l3 = " "
          l4 = "-"
        elif l2 == "-":
          l2 = " "
          l3 = "-"
        elif l1 == "-":
          l1 = " "
          l2 = "-"
        if a5 == "-":
          a5 = " "
          misses += 1
        elif a4 == "-":
          a4 = " "
          a5 = "-"
        elif a3 == "-":
          a3 = " "
          a4 = "-"
        elif a2 == "-":
          a2 = " "
          a3 = "-"
        elif a1 == "-":
          a1 = " "
          a2 = "-"
        if s5 == "-":
          s5 = " "
          misses += 1
        elif s4 == "-":
          s4 = " "
          s5 = "-"
        elif s3 == "-":
          s3 = " "
          s4 = "-"
        elif s2 == "-":
          s2 = " "
          s3 = "-"
        elif s1 == "-":
          s1 = " "
          s2 = "-"
        while numberofnotes != numberofnotes2:
          numberofnotes2 += 1
          notee = str(numberofnotes2) + "note"
          if int(mapdata[notee]) == timing:
            noteee = str(numberofnotes2) + "noteK"
            if mapdata[noteee] == "K":
              k1 = "-"
            elif mapdata[noteee] == "L":
              l1 = "-"
            elif mapdata[noteee] == "A":
              a1 = "-"
            elif mapdata[noteee] == "S":
              s1 = "-"
        os.system("cls")
        print("|"+ str(a1) +"|   |"+ str(s1) +"|   |"+ str(k1) +"|   |"+ str(l1) +"|")
        print("|"+ str(a2) +"|   |"+ str(s2) +"|   |"+ str(k2) +"|   |"+ str(l2) +"|")
        print("|"+ str(a3) +"|   |"+ str(s3) +"|   |"+ str(k3) +"|   |"+ str(l3) +"|")
        print("|"+ str(a4) +"|   |"+ str(s4) +"|   |"+ str(k4) +"|   |"+ str(l4) +"|")
        print("|"+ str(a5) +"|   |"+ str(s5) +"|   |"+ str(k5) +"|   |"+ str(l5) +"|")
        print("|=|   |=|   |=|   |=|")
        print("|A|   |S|   |K|   |L|")
        if isdebug == "YES":
          print(str(timing) + " ticks")
        if timing >= int(mapdata["lenght"]):
          mapplay = False
          #misses -= int(mapdata["numberofnotes"])
          print("End of map")
          print("You missed " + str(misses) + " of " + mapdata["numberofnotes"] + " notes")
          print("Map passed with score of " + str((trafione/int(mapdata["numberofnotes"]))*100) + "%")
          print("Save the score?")
          savescore = input("[y/n]")
          if savescore == "y":
            mapdata["playerscore"] = str((trafione/int(mapdata["numberofnotes"]))*100) + "%"
            with open(mapdata["mapname"] + ".json", 'w') as outfile:
              json.dump("Maps/" + mapdata, outfile)
          sleep(2)
          program()
  os.system("cls")
  print("   __    ___   ___  ____  ____    ____  _   _  _  _  ____  _   _  __  __ ")
  sleep(0.1)
  print("  /__\  / __) / __)(_  _)(_  _)  (  _ \( )_( )( \/ )(_  _)( )_( )(  \/  )")
  sleep(0.1)
  print(" /(__)\ \__ \( (__  _)(_  _)(_    )   / ) _ (  \  /   )(   ) _ (  )    ( ")
  sleep(0.1)
  print("(__)(__)(___/ \___)(____)(____)  (_)\_)(_) (_) (__)  (__) (_) (_)(_/\/\_)")
  sleep(0.1)
  print("Made by Pouek_")
  print("v.0.1")
  print("-------------------------------------------------------------------------")
  print("l - load map from file")
  print("m - search for maps")
  print("q - quit")
  choose = input("")
  if choose == "l":
      print("Type the directory of map or just slide it here")
      premap = input("")
      maap = premap.replace('"','')
      os.system("cls")
  elif choose == "rr":
    os.system("main.py")
  elif choose == "q":
    with open("music.ar","w") as f:
        f.write("exit")
        f.close()
  elif choose == "m":
    print("Searching for maps...")
    print("This can take some time")
    sleep(0.1)
    os.system("cls")
    loadedmaps = []
    loadedmaps = [pos_json for pos_json in os.listdir("Maps") if pos_json.endswith('.json')]
    countmaps = str(loadedmaps).count(".json")
    print("Found " + str(countmaps) + " maps")
    print("=================================")
    print(str(loadedmaps).replace("]","").replace("[","").replace("Maps","").replace("'","").replace("/","").replace(".json",""))
    print("=================================")
    print("Type the map name to choose")
    mapname = input("")
    maap = "Maps/" + mapname + ".json"
    play()
  elif choose == "don":
    with open("debug.ar","w") as f:
        f.write("YES")
        f.close()
    program()
  elif choose == "dno":
    with open("debug.ar","w") as f:
        f.write("to jest dramat kurwa")
        f.close()
    program()
program()