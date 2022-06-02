while True:
    try:
        age = int(input("Plase enter your age :"))
        10/age
    except (ValueError, ZeroDivisionError) as err:
        print(f"Please enter Valid Age. Error is :{err}")
        continue
    else:
        print(age)
        print('Thank You')
        break
    finally:
        print("This will always run even after 'break' and 'continue'")