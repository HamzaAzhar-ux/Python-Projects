import time
from calendar import isleap


def is_leap_year(year):
    """Checks if a given year is a leap year.

    Args:
        year (int): Year to be checked.

    Returns:
        bool: True if leap year, False otherwise.
    """
    return isleap(year)


def get_days_in_month(month, leap_year):
    """Returns the number of days in a given month, considering leap year.

    Args:
        month (int): Month number (1-12).
        leap_year (bool): True if leap year, False otherwise.

    Returns:
        int: Number of days in the month.
    """
    days_in_month = {
        1: 31,
        2: 28,  # Base case for non-leap year
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if month == 2 and leap_year:
        days_in_month[2] = 29  # Override for leap year February

    return days_in_month[month]


def calculate_age_in_days(birth_year, current_year):
    """Calculates the total number of days lived based on birth and current year.

    Args:
        birth_year (int): Year of birth.
        current_year (int): Current year.

    Returns:
        int: Total number of days lived.
    """
    total_days = 0
    for year in range(birth_year, current_year):
        total_days += 366 if is_leap_year(year) else 365
    return total_days


def calculate_age(name, birth_year):
    """Calculates age in years, months, and days based on birth year and current date.

    Args:
        name (str): Name of the person.
        birth_year (int): Year of birth.
    """
    try:
        current_time = time.localtime()
        current_year = current_time.tm_year
        current_month = current_time.tm_mon

        total_days = calculate_age_in_days(birth_year, current_year)

        # Calculate months and remaining days
        years = total_days // 365
        remaining_days = total_days % 365

        months = 0
        leap_year = is_leap_year(current_year)
        for month in range(1, current_month):
            months += get_days_in_month(month, leap_year)

        months += remaining_days // get_days_in_month(current_month, leap_year)
        remaining_days %= get_days_in_month(current_month, leap_year)

        print(f"{name}'s age is \n years= {years}.\n months= {months} \ndays= {remaining_days}")

    except ValueError:
        print("Invalid age entered. Please enter a valid integer.")


if __name__ == "__main__":
    name = input("Please enter your name: ")
    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except ValueError:
            print("Invalid age entered. Please enter a valid integer.")

    birth_year = int(time.localtime().tm_year) - age
    calculate_age(name, birth_year)
