import random
n=random.randint(1, 100)
guesses=0
while True:
    guesses+=1
    a= int(input("enter a numbere between 1 and 100:"))
    if (a>n):
        print("lower number please!")
    else:
        print("higher number please!")
    if (a==n):
        break
print(f"you guessed the number {n} in {guesses} guesses")
