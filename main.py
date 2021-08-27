import math;
import time;

def is_int(x):
  try:
    x = int(x)
    return True
  except ValueError:
    return False

def triple_maker(num, triple, triple_2):
  if num > triple:
    ordered_pair = f"{triple}, {num}, {triple_2}"
  else:
    ordered_pair = f"{num}, {triple}, {triple_2}"
  return ordered_pair


print(" Hello, I will give you a pythagorean triple based on any positive integer you enter (please be sure it's bigger than two)")
again = ""
blank = input()

print("The number you input will be the smallest in the triple for simplicity's sake")

while( again == ""):
  triple = 0
  triple_2 = 0
  num = 0
  numsq = 0
  dis = 1
  triples_list = [""]
  correct = False
  while( correct == False):
    num = input(" What's the integer: ")
    if is_int(num) == True:
      num = int(num)
      numsq = num**2
      n_max = num
      if num > 2:
        if num%2 == 0:
          dis = 2
          while dis < num:
            triple = math.round((num**2 - dis**2 + 2*dis)/(2*dis) + 1, 6)
            triple_2 = triple + dis
            dis += 2
            if is_int(triple) == True:
              triples = triple_maker(num, triple, triple_2)
              triples_list.append(triples)
        else:
          while( dis < num):
            triple = math.round((num**2 - dis**2 + 2*dis)/(2*dis) + 1, 6)
            triple_2 = triple + dis
            dis += 2
            if is_int(triple) == True:
              triples = triple_maker(num, triple, triple_2)
              triples_list.append(triples)

        correct = True 
      else:
        print("you need to enter a number above 2!")
    else:
      print("it needs to be an integer silly")


