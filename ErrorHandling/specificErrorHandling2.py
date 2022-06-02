while True:
    try:
        age = int(input("Plase enter your age :"))
        10/age
    except (ValueError, ZeroDivisionError) as err:
        print(f"Please enter Valid Age. Error is :{err}")
    else:
        print(age)
        print('Thank You')
        break