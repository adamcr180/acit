import dow

def getDayOfTheWeekForUserDate():
    print("--- Day of the Week Finder ---")
    
    user_month = int(input("Enter month (1-12): "))
    user_day = int(input("Enter day (1-31): "))
    user_year = int(input("Enter year (e.g., 2026): "))
    
    weekday_result = dow.getDayOfTheWeek(user_year, user_month, user_day)
    
    print(f"The date {user_month}-{user_day}-{user_year} is a {weekday_result}.")

if __name__ == "__main__":
    dow.makeCalendar()
    
    print("" + "="*40 + "")
    
    getDayOfTheWeekForUserDate()
