import sys
import random

gameNumber = random.randint(1,10)

def check_match():
    try:
        userNumber = int(input("Inter a Number to guess : "))
        if gameNumber ==  userNumber:
            #print(f"User Number is :{userNumber} and Game guessed it :{gameNumber}")
            return True
        return False
    except (ValueError, TypeError, IndexError):
        print('Please enter a valid Number')
        return False

if __name__ == "__main__":
    while True:
        if (check_match()):
            print("Number matched")
            break
        else:
            print(f"Oops! no match!! Try Again : Hint Try {gameNumber}")
