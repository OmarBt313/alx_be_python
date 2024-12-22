task = input("Enter your task:")

priority = input("Priority (high/medium/low):")

time_bound = input("is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}'is a high priority task that requires immediate attention today!")

        else:
            print(f"'{task}' is high priopity but not time_bound ")

    case "medium":
        if time_bound == "yes":
            print(f"'{task}'is a medium priority task that shoud be schedualed for this week!")

        else:
            print(f"'{task}' is medium priopity and not time_bound ")

    case "low":
        if time_bound == "yes":
            print(f"'{task}'is a low priority task. Consider completing it when you have free time.")

        else:
            print(f"'{task}' is low priopity and not time_bound ")