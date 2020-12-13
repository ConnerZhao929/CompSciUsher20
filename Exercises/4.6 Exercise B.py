# Conner Zhao 12/06/20
 
import random
 
def sequence():
  global answer
  answer = []
  for i in range(4):
    answer.append(random.randint(1,9))
 
def check(g0, g1, g2, g3):
  global count
  count = 0
  if g0 == answer[0]:
    count = count + 1
  if g1 == answer[1]:
    count = count + 1
  if g2 == answer[2]:
    count = count + 1
  if g3 == answer[3]:
    count = count + 1
  return count
 
sequence()
print(answer)
print("\n\n")
tries = 0
count = 0
while count != 4:
  tries = tries + 1
  guess1 = int(input("What do you think the first number is? "))
  guess2 = int(input("What do you think the second number is? "))
  guess3 = int(input("What do you think the third number is? "))
  guess4 = int(input("What do you think the fourth number is? "))
  count = check(guess1, guess2, guess3, guess4) 
  print("You guessed " + str(count) + " correctly.")
print("Congratulations, it took you " + str(tries) + " tries.")

