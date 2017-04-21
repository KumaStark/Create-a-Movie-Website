# Set a list includes total days in every month(except leap year).
daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    """Returns True if inputed year is leap year."""
    if year / 100 == year / 100.0:
        if year / 400 == year / 400.0:
            return True
        else:
            return False
    elif year / 4 == year / 4.0:
        return True
    else:
        return False


def convertYMDtoDs(y, m, d):
    """Convert year/month/day to count days passed."""
    # days start from 0
    totaldays = 0
    # Loop to count how many days passed of these years.
    # i_Year start from 0 to inputed Y(means year).
    i_year = 0
    while i_year < y:
        totaldays += 365
        # If the year is leap year, then plus an extra day.
        if isLeapYear(i_year):
            totaldays += 1
        i_year += 1
    # Loop to count how many days passed of these monthes in current year.
    # i_month start from 0 to inputed m(means month).
    i_month = 0
    while i_month < m - 1:
        if isLeapYear(y) and i_month == 2:
            totaldays += daysOfMonths[i_month] + 1
        else:
            totaldays += daysOfMonths[i_month]
        i_month += 1
    # Plus the d(means day) which is the count of days passed in current month.
    totaldays += d
    # Returns the total days
    return totaldays


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    """Return Days between y1/m1/d1 and y2/m2/d2
    # If the function returns a positive number,
    # It means y2/m2/d2 is later then y1/m1/d1, and vise versa.
    # If the function returns 0, it means y1/m1/d1 and y2/m2/d2 is same."""
    days = convertYMDtoDs(y2, m2, d2) - convertYMDtoDs(y1, m1, d1)
    return days
