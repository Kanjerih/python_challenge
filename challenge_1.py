print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play :)")
score = 0

answer = input("what does gpu stand for? ")

if answer.lower() == "graphic processing unit":

    print('correct!')
    score += 1
else:
    print("Incorrect")

answer = input("what does ram stand for? ")

if answer.lower() == "random access memory":

    print('correct!')
    score += 1
else:
    print("Incorrect")


    answer= input("what does psu stand for? ")

if answer.lower() == "power supply":

    print('correct!')
    score += 1
else:
    print("Incorrect")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/4)*100) +  "%.")
