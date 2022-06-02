while True:
    try:
        age = int(input("Plase enter your age :"))
        10/age
    except ValueError:
        print("Please enter  number")
    except ZeroDivisionError:
        print("Please enter  number greater than 0")
    else:
        print(age)
        print('Thank You')
        break
