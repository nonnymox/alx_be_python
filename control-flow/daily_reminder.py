task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no)")


match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is still a high priority task that requires some attention soon!")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is still a medium priority task that requires some attention. Consider completing it "
                  f"when you have free time.!")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is still a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Unknown priority level for '{task}'. Please enter 'low', 'medium', or 'high'.")




