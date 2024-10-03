class ValueTooHighError(Exception):
    "Raised when the input value is less than 18"
    pass


num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
try:
    if num1 > 100:
        raise ValueTooHighError
    num3 = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueTooHighError:
    print("The firstpip value is higher than 100")
except ValueError:
    print("Please enter a number.")
else:
    print(f"{num1} divided by {num2} is equal to {num3}.")
finally:
    pass
