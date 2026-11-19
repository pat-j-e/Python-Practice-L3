# a monster mash mini-script that shows use of ASCII art, module from a python library, and a while loop
import random # necessary to create random numbers later
import time # used to repeat the mash at certain intervals

# arrays of ASCII art monster parts
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


i = 0
# use of while loop. terminates after 5 monsters
while i < 5:
  # use of Python random library. random.choice chooses a random value held inside a data structure, in this case my array of strings
  head = random.choice(heads)
  body = random.choice(bodies)
  leg = random.choice(legs)
  i+=1 # iterator to control loop
  print(head)
  # use of Python time library to give a little animation to the construction by pausing each segment
  time.sleep(0.1)
  print(body)
  time.sleep(0.1)
  print(leg)
  time.sleep(0.1)
  time.sleep(2)
print("5 monsters have been mashed, how horrible!")