# a python mini-game that asks you to type a random string of numbers and letters to beat an enemy before the time runs out
#tried to do a live timer that locks you out of inputting if youre too slow
# but it seems like you cant do this on trinket since you cant interrupt after requesting input
import random
import time
characters = "abcdefghijklmnopqrstuvwxyz" # the selection of characters that are selected from at random later on
health = 3 # how many words need to be typed to beat the monster
timeLimit = 12 # total time allowed for all words to be spelled out
start = time.time() #  gets the starting point of when the program started
print("A monster has appeared!")
# main game loop that runs so long as the monster is alive
while health > 0:
# use of built-in function 1 (print())
  print(
    """  .-------.   
 /  `o o'  \  |
 \    ^    /  |
--|       |---+¬
  |       |   T
  |_______|   
   ||   ||   
  _||   ||_  """)
  #creates the word to be typed
  word = ""
  i = 0
  # while loop with delimiter of 5 decides length of word
  while i < 5:
    if i == 0:
          word = word + random.choice(characters).upper() # capitalises first letter
    else:
          word = word + random.choice(characters) # adds the rest on
    i += 1
  #collect user input
  inputWord = input("Quick! Type the magic word '" + "\033[34m" + word + "\033[0m" + "' to fight back! ")
  # the strings before and after word here change the colour to blue then back to normal
  # check if word typed in time limit, if not then fail out
  elapsed = time.time() - start 
  # you need to minus the starting time to get elapsed time. time.time() returns a huge number that is reduced down to a usable one by this
  if elapsed > timeLimit:
    print("\033[31m" + "Too slow! The monster reached you!")
    print(r"""     GAME OVER
     .--------.
    /  ()  ()  \
    \    <>    /
     '-.WWWW.-'
       |_||_|
""")
    break
  # check if input word is correct
  if inputWord == word:
    health-=1
    print("A direct hit!")
    if health == 1:
      print("\033[31m" + "He's almost down!" + "\033[0m")
    if health > 0:
      print("Here he comes again! Get ready!")
      # use of built-in function 2 (round())
      print(round(timeLimit - elapsed), "seconds left!")
  #if word is wrong then fail out
  else:
    print("\033[31m" + "You messed up the spell and the monster reached you!")
    print(r"""     GAME OVER
     .--------.
    /  ()  ()  \
    \    <>    /
     '-.WWWW.-'
       |_||_|
""")
    break
# if the loop has ended then checks if health is 0 aka a win state
if health == 0:
  print("You won, while the monster was " + str(round(timeLimit - elapsed, 1)) + " seconds from reaching you!")
  print(
    """  .-------.   
 /  `X X'  \  |
 \    ^    /  |
--|       |---+¬
  |       |   T
  |_______|   
   ||   ||   
  _||   ||_  """)

