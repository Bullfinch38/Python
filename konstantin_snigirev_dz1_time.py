print("Time defining program")
# number = input("Enter duration in seconds: ")
# number = int(number)
# print(f'{number} seconds')
#
# number = input("Enter number in seconds: ")
# number = int(number)
# minutes = number // 60
# seconds = number % 60
# print(f'{minutes} min and {seconds} sec')
#
# number = input("Enter number in minutes: ")
# number = int(number)
# hours = number // 60
# minutes = number % 60
# print(f'{hours} h and {minutes} min')

number = input("Enter duration (in seconds): ")
number = int(number)
seconds_day = 60 * 60 * 24
seconds_hour = 60 * 60
seconds_minute = 60

days = number // seconds_day
# print(days)
hours = (number - seconds_day * days) // seconds_hour
# print(hours)
minutes = (number - (seconds_day * days) - (hours * seconds_hour)) // seconds_minute
# print(minutes)
seconds = number - (seconds_day * days) - (hours * seconds_hour) - (minutes * seconds_minute)
# print(seconds)
print(f'{days} d {hours} h {minutes} m {seconds} s')

