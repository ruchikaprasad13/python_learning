#Ruchika's Tresure Hunt
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# first choice
fork = input("You're hiking on a wooded trail and come to a fork in the road. Do you go 'left' or 'right'? \n").lower()
if fork == "left":
  lake = input("You reach the shore of a large lake with an island in the center.\n  Do you wait for the ferryman or just swim across? (Choose 'wait' or 'swim') \n").lower()

  # second choice
  if lake == "wait":
    cave = input("The ferryman gladly takes you across the lake and you walk into the jungle.\n After a short while you come upon a large cave.\n Curiously you enter.  Oddly enough, inside the cave are three doors: A Red, Blue, and Yellow door.  Which do you choose, 'red', 'blue', or 'yellow'? \n").lower()

    #final choice
    if cave == "red":
      print("As the door closes and locks behind you, a giant scorpion surprises you...\n it stings and eats you. Game Over.")  
    elif cave == "blue":
      print("As the door opens, a giant troll grabs you by the neck...he kills and eats you.  Game Over.")
    elif cave == "yellow":
      print("The door slowly swings open to reveal...The lost treasure of Jack Sparrow!!!  Congratulations Mate You WIN!")
    else:
      print("You turn to leave and are suddenly attacked by a large mountain lion...and Die.  Game Over.")
  
  else: 
    print("After a few minutes in the water, you are pulled under and drown by a large crocodile.  Game Over.")  
    
else:
  print("About 50 yards in you are attacked & mauled to death by a giant momma grizzly bear.  Game Over.")
  
