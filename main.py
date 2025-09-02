import requests, json, os, time
from replit import db

while True:
  time.sleep(1)
  os.system("clear")
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
  
  joke = result.json()
  funny = joke["joke"]
  id = joke["id"]
  print(funny)
  print()
  ans = input("(s)ave this joke, (l)oad saved jokes or (n)ew joke: \n").lower()
  print()
  if ans == "n":
    continue
  elif ans == "s":
    db[id] = funny
    print("Saved")
    continue
  else:
    for key in db.keys():
      print(db[key])
      print("\n")
      
    
    
