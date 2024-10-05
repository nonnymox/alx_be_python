def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator); denominator = float(denominator)
        if denominator == 0:
            raise ZeroDivisionError
        # print(f"{numerator}, {denominator}")
    except ValueError:
        print("Bad input")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        result = denominator/numerator
        print(f"{numerator} divided by {denominator} is equal to {result:.2f}")

