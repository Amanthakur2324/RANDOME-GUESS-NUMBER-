import random
num = random.randint(1,100)

tries = 0
while True:
    guess = int(input("ENTER THE NUMBER "))
    if num==guess:
        tries +=1
        print("you  won YOU are right")
        print(f"YOU GUESS THE NUMBER IN {tries} TRIES")
        break

    elif num<guess:
        print("GO A LIITLE LOWER")
        tries+=1
        
    elif num>guess:
        print("GO A LITTLE HIGHER ")
        tries+=1    
    else:
        tries+=1
        print("you are wrong ")
        
