import calendar

# Calender module use to work with dates and generate calendar data

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
print() # leave a blank line
print("Here is the calendar : ")
print() # leave a blank line
print(calendar.month(year, month))

# Here calendar.month(year, month) returns a string that looks like a real calendar
