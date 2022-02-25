from datetime import datetime
# importing method to get the day of the week
# reference: https://www.delftstack.com/howto/python/python-datetime-day-of-week/#:~:text=of%20the%20day.-,Use%20the%20weekday()%20Method%20to%20Get%20the%20Name%20of,0%20and%20Sunday%20is%206.

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
# creating an array which defines all the days of the week

weekdays = days[:5]
# defining weekdays using the array

today = (datetime.today().strftime('%A'))
# defining the day of the week as 'today' to use in subsequent if statement.

if (today in weekdays):
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
# if, else statement to execute the print command
