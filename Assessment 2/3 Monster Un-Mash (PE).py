# a python mini-game about unmashing the monsters from the previous trinket program
# the only objective left is to create a user-defined function
import random
# arrays of ASCII art monster parts, same as previous script
heads = [
r"""   .-----.   
  /  o o  \  
 (    ~    ) """, # octopus head
r"""   _______   
  / x   x \  
  | ,===, |  """, # zombie head
r""" @ .-----. @ 
  ( o   o )  
   \  U  /   """, # monkey head
r"""   .-----.   
  | O   O |  
   \ ||| /   """, # skeleton head
]

bodies = [
r"""  \_______/  
   | ~ ~ |   
   |_~_~_|   """, # octopus body
r"""--|       |--
  |  ___  |  
  |__|_|__|  """, # zombie body
r"""  /|     |\  
 / |  _  | \ 
   |_____|   """, # monkey body
r"""  --|=|=|--  
    |=|=|    
    |=|=|    """, # skeleton body
]

legs = [
r"""  / /| |\ \  
  ~ ~ ~ ~ ~  """, # octopus legs
r"""    |   |    
   _|   |_   """, # zombie legs
r"""   /     \   
  d       b  """, # monkey legs
r"""   ||   ||   
  _||   ||_  """, # skeleton legs
]
monsters = ["octopus", "zombie", "monkey", "skeleton"]
# list of monster names in string that can be compared to typed input later

# my user defined function that sets both the body part ASCII art and the body part answer string at the same time
def SetRandomPart(parts):
  number = random.randint(0, len(parts) - 1)
  return parts[number], monsters[number]

# this is where my user defined function is used
# python lets you return multiple values very easily so the art and answer string can be set on the same line
head, jumbledHead = SetRandomPart(heads)
body, jumbledBody = SetRandomPart(bodies)
leg, jumbledLegs = SetRandomPart(legs)

# the rest is printing logic for prompting the player
print(head)
print(body)
print(leg)
print("Some horrible, horrible person has ran a program that mashed together some poor monsters!")
print("Identify which pieces from the above creature belong to which monster below so they can be put back together again!")
print("\033[90m"+r"""
   Octopus        Zombie         Monkey        Skeleton
   .-----.        _______      @ .-----. @      .-----.
  /  o o  \      / x   x \      ( o   o )      | O   O |
 (    ~    )     | ,===, |       \  U  /        \ ||| /
  \_______/    --|       |--    /|     |\      --|=|=|--
   | ~ ~ |       |  ___  |     / |  _  | \       |=|=|
   |_~_~_|       |__|_|__|       |_____|         |=|=|
  / /| |\ \        |   |         /     \        ||   ||
  ~ ~ ~ ~ ~       _|   |_       d       b      _||   ||_
"""  + "\033[0m")

# this part takes in the answers and just compares them to the strings received from the user-defined function
userinput = input("Whose head is that? ").lower() # it uses /lower() so that the input works regardless of capitalisation
if userinput == jumbledHead: #check against earlier received string
  print("\033[32m"+"Phew, the " + jumbledHead + " got his head back.") # the numbers on these lines are just for colouration
else:
    print("\033[31m" + "Not quite, looks like that monster is stuck without his head...")
userinput = input("\033[0m"+"Which body is that? ").lower()
if userinput == jumbledBody:
  print("\033[32m"+"Phew, the " + jumbledBody + " got his body back.")
else:
    print("\033[31m" + "Not quite, looks like that monster is stuck without his body...")
userinput = input("\033[0m"+"Whose legs are those? ").lower()
if userinput == jumbledLegs:
  print("\033[32m"+"Phew, the " + jumbledLegs + " got his legs back.")
else:
    print("\033[31m" + "Not quite, looks like that monster is stuck without his legs...")