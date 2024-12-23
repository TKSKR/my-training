while True:
    try:
        num1 = int(input("Enter first number: "))
    except ValueError:
        continue
    else:
        break