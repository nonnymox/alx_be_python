def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator); denominator = float(denominator)
        if denominator == 0:
            raise ZeroDivisionError
        # print(f"{numerator}, {denominator}")
        res = numerator / denominator
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        return f"The result of the division is {res}"

