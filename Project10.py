#Creating a calendar by taking month and year input from user.

#import calendar
import calendar

# Enter the month and year.
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar.
print(calendar.month(yy,mm))