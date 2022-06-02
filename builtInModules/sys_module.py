import sys
import random

userNumber = int(sys.argv[1])

while True:
    
    gameNumber = random.randint(1,10)

    if gameNumber ==  userNumber:
        print("Number matched")
        print(f"User Number is :{userNumber} and Game guessed it :{gameNumber}")
        break
    else:
        print(f"Oops! no match!! User Number is :{userNumber} and Game guessed it :{gameNumber}")
