from datetime import datetime, timedelta


def display_current_datetime():
    current_datetime = datetime.now()
    current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return f"Current date and time: {current_datetime}"


# print(display_current_datetime())

num_days = int(input("Enter the number of days to add to the current date: "))


def calculate_future_date():
    future_date = datetime.now() + timedelta(days=num_days)
    return f"Future date: {future_date}"

# print(calculate_future_date())
