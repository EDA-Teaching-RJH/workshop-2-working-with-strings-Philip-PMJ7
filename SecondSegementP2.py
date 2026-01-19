import random
secret_number = random.randint(1, 10)
bln = False

while bln == False:
    your_number = int(input("Guess a number from 1 to 10: "))
    if your_number == secret_number:
        print("That's right! The correct answer is " + str(secret_number))
        bln = True
    elif your_number > secret_number:
        print("Too High!")
    else:
        print("Too Low!")