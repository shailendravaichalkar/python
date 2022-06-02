while True:
    try:
        age = int(input("Plase enter your age :"))
        10/age
        raise ValueError("Het Cut it out")
        #raise Exception("Finish it")
    except ZeroDivisionError:
        print(" Age > 0")
        break
    else:
        print("Thank you") # Never get executed because of raise 

