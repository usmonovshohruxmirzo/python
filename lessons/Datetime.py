from datetime import datetime, date, time, timedelta, timezone

# Current Date and Time
now = datetime.now()
print(now)

today = date.today()
print(today)

# utc_now = datetime.utcnow() # The method "utcnow" in class "datetime" is deprecated
utc_now = datetime.now(timezone.utc)
print(utc_now)


# Creating Specific Dates and Times
my_date = date(2024, 11, 26)
print(my_date)

my_time = time(14, 30, 45)  
print(my_time) 

my_datetime = datetime(2024, 11, 26, 14, 30, 45)
print(my_datetime)  

# Formatting and Parsing Dates and Times
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

date_str = "2024-11-26 14:30:45"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed_date)  

# Date and Time Arithmetic
now = datetime.now()
future = now + timedelta(days=7)  # Add 7 days
past = now - timedelta(hours=2)  # Subtract 2 hours
print(future)  # Example: 2024-12-03 12:30:45
print(past)    # Example: 2024-11-26 10:30:45

start = datetime(2006, 9, 16)
end = datetime(2024, 11, 26)
difference = end - start
print(difference)


#  Comparing Dates and Times
date1 = datetime(2024, 11, 25)
date2 = datetime(2024, 11, 26)

print(date1 < date2)
print(date1 == date2)

# Working with Timezones

# Create a timezone with UTC+5
tz = timezone(timedelta(hours=5))
now = datetime.now(tz)
print(now)  # Example: 2024-11-26 17:30:45+05:00

# from pytz import timezone
# utc_now = datetime.now(timezone("UTC"))
# ist = utc_now.astimezone(timezone("Asia/Kolkata"))
# print(ist)


# Practical Examples
# Countdown Timer

future_date = datetime(2024, 12, 31)
now = datetime.now()
countdown = future_date - now
print(f"Days until new year: {countdown.days}")