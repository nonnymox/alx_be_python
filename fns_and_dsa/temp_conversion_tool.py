FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# Creating a Function that takes °f and uses the formula to convert °c
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


# Function that take °c and uses the formula to convert to °f
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# Testing the functions
# print(convert_to_celsius(59))
# print(convert_to_fahrenheit(15))


# Prompting user for the temperature to convert and the °c or °f
temp = float(input("Enter the temperature to convert: "))
c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

# Converting based on the user input
if c_or_f == "c":
    print(f"{temp}°C is to {convert_to_fahrenheit(temp):.2f}°F")
elif c_or_f == "f":
    print(f"{temp}°F is {convert_to_celsius(temp):.2f}°C")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")