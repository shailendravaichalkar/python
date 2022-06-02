while True:
    try:
        age = int(input("Plase enter your age :"))
    except:
        print("Please enter  number")
    else:
        print(age)
        print('Thank You')
        break
