#EmpathyTest.py

import random
import sys

emoticons = [
    ("happy", "(^_^)"),
    ("sad", "(T_T)"),
    ("laughing", "(^o^)"),
    ("winking", "(^_~)"),
    ("surprised", "(O_O)"),
    ("embarrassed", "(^_^;)"),
    ("annoyed", "(-_-)"),
    ("cheering", r"\(^o^)/"),
    ("sleepy", "(-_-)zzz"),
    ("shrugging", r"\_('_')_/"),
]
i = 0
s = 0
r = int(sys.argv[1])
while i < r:
  randomEmoticons = random.sample(emoticons, 3)
  correct = random.randrange(3)
  emotion = randomEmoticons[correct]
  print("Which of these emoticons best matches '" + emotion[0] + "'?" )
  userInput = input("1. " + randomEmoticons[0][1] + ", 2." + randomEmoticons[1][1] + ", or 3. " + randomEmoticons[2][1] + "? ")
  
  if int(userInput)-1 == correct:
    s = s + 1
    print("Correct!")
    
  else:
    print("Nope :-(")
  i = i + 1
print("You scored " + str(s) + "!")