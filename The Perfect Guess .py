import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a!=n):
  guesses += 1
  a = int(input("guess the number:"))
  if (a>n):
    print("Lower number please")
  else:print("higher number please")

print(F"you guesses correct number {n} in {guesses} attempts")




