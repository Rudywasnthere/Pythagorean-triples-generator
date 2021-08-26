import math;
import time;

print(" Hello, I will give you a pythagorean triple based on any positive integer you enter (please be sure it's bigger than two)")
again = ""
blank = input()

print("The number you input will be the smallest in the triple for simplicity's sake")

while( again == ""):
  triple = 0
  triple_2 = 0
  num = 0
  correct = False
  while( correct == False):
    num = input(" What's the integer: ")
    try:
      num = int(num)
      print("True")
      if num > 2:
        if num%2 == 0:
          triple = int(((num**2)/4) - 1)
          triple_2 = triple + 2
        else:
          triple = int(((num**2) - 1)/2)
          triple_2 = triple + 1
        correct = True
      else:
        print("you need to enter a number above 2!")
    except ValueError:
      print("it needs to be an integer silly")

  if num > triple:
    ordered_pair = f"{triple}, {num}, {triple_2}"
  else:
    ordered_pair = f"{num}, {triple}, {triple_2}"

  print(f"You're triple is {ordered_pair}")