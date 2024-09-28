def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num1 != 0:
            return num2 / num1
        else:
            return "Cannot divide by zero."
    else:
        return "That is not valid!"
