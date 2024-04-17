import math

while True:
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise Exception
        print(math.factorial(num))
        break
    except Exception:
        print("Enter a positive num")
