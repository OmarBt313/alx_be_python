from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date)
current_date = datetime.now()


# current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
print(current_date.strftime("%Y-%m-%d %H:%M:%S"))

user_input = int(input("Enter the number of days to add to the current date:"))


def calculate_future_date():
    delta = timedelta(days =user_input)
    future_date = current_date + delta
    return future_date.strftime("%Y-%m-%d %H:%M:%S")
    
#     
print(calculate_future_date())