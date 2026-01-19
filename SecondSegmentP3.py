grade = int(input("Plrase enter your score out of 100: "))

if grade > 100:
    print("How? I mean, well done and all, excellent work, but how?")
elif 100 >= grade >= 90:
    print("Well done! You got an A!")
elif grade > 80:
    print("Very nice! You got a B!")
elif grade > 70:
    print("Nice! You got a C!")
elif grade > 60:
    print ("You got a D, at least it isn't an F.")
elif grade >= 1:
    print("You got below 60. You got an F.")
else:
    print("I- how??? F. Get out.")