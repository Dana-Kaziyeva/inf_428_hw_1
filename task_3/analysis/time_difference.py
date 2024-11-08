# task3/analysis/time_difference.py

def time_to_minutes(hours, minutes, am_pm):
    """
    Convert time in hours and minutes (AM/PM) to minutes since midnight.

    :param hours: Hours in 12-hour format (1-12).
    :param minutes: Minutes of the hour.
    :param am_pm: 'AM' or 'PM'.
    :return: Total minutes since midnight.
    """
    if am_pm.lower() == 'pm' and hours != 12:
        hours += 12
    elif am_pm.lower() == 'am' and hours == 12:
        hours = 0
    return hours * 60 + minutes


def convert_to_am_pm(time):
    """
    Convert 24-hour time to 12-hour AM/PM format.

    :param time: Time in 24-hour format (0-23 hours).
    :return: A tuple of (hours, minutes, AM/PM).
    """
    hours, minutes = divmod(time, 60)
    am_pm = 'AM' if hours < 12 else 'PM'
    if hours > 12:
        hours -= 12
    elif hours == 0:
        hours = 12
    return hours, minutes, am_pm


def time_difference_in_hours(time1, time2):
    """
    Calculate the time difference between two times in hours,
    considering time wrapping at midnight (cyclic).

    :param time1: Time in 24-hour format (0-23 hours).
    :param time2: Time in 24-hour format (0-23 hours).
    :return: Time difference in hours.
    """
    diff = abs(time2 - time1)
    return min(diff, 24 - diff)
