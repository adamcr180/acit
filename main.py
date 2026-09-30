import dow

def getDayOfTheWeekForUserDate():
    """Prompts user for specific date parts and prints the calculated weekday."""
    print("--- Day of the Week Finder ---")
    
    user_month = int(input("Enter month (1-12): "))
    user_day = int(input("Enter day (1-31): "))
    user_year = int(input("Enter year (e.g., 2026): "))
    
    weekday_result = dow.getDayOfTheWeek(user_year, user_month, user_day)
    
    print(f"\nThe date {user_month}-{user_day}-{user_year} is a {weekday_result}.\n")

if __name__ == "__main__":
    dow.makeCalendar()
    
    print("\n" + "="*40 + "\n")
    
    getDayOfTheWeekForUserDate()
