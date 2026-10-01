MONTH_CODES = {
    1: 1,  # January
    2: 4,  # February
    3: 4,  # March
    4: 0,  # April
    5: 2,  # May
    6: 5,  # June
    7: 0,  # July
    8: 3,  # August
    9: 6,  # September
    10: 1, # October
    11: 4, # November
    12: 6  # December
}

WEEKDAY_NAMES = {
    0: "Saturday",
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday"
}

DAYS_IN_MONTHS = {
    1: 31, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

def getDayOfTheWeek(year, month, day):
    last_two_digits = year % 100
    twelves_count = last_two_digits // 12
    remainder_of_twelve = last_two_digits % 12
    fours_in_remainder = remainder_of_twelve // 4
    day_of_month = day
    
    month_code = MONTH_CODES[month]
    
    if (month == 1 or month == 2) and isLeapYear(year):
        month_code -= 1
        
    century = (year // 100) * 100
    if century == 1600 or century == 2000:
        month_code += 6
    elif century == 1700 or century == 2100:
        month_code += 4
    elif century == 1800:
        month_code += 2
        
    total_sum = twelves_count + remainder_of_twelve + fours_in_remainder + day_of_month + month_code
    weekday_index = total_sum % 7
    
    return WEEKDAY_NAMES[weekday_index]

def makeCalendar():
    year_target = 2026
    
    for month in range(1, 13):
        if month == 2:
            total_days = 29 if isLeapYear(year_target) else 28
        else:
            total_days = DAYS_IN_MONTHS[month]
            
        for day in range(1, total_days + 1):
            day_name = getDayOfTheWeek(year_target, month, day)
            print(f"{month}-{day}-{year_target} is a {day_name.lower()}.")
