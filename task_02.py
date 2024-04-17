import math


def run_1(num):
    def factorial(num):
        if num < 0:
            raise Exception
        return math.factorial(num)

    try:
        print(factorial(num))
    except Exception:
        print("Enter a positive num")


def run_2(num):
    def factorial(num):
        try:
            if num < 0:
                raise Exception
            return math.factorial(num)
        except Exception:
            return "Enter a positive num"

    try:
        print(factorial(num))
    except Exception:
        print("Enter a positive num")


user_num = int(input("Enter a number: "))
run_1(user_num)
run_2(user_num)