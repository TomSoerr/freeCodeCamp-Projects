def add_time(start, duration, optional=None):
    # convert input #
    time, am = start.split()
    start_hours, start_minutes = time.split(":")
    hours, minutes = duration.split(":")

    start_hours, start_minutes, hours, minutes = int(start_hours), int(start_minutes), int(hours), int(minutes)
    if am == "AM":
        am = True
    elif am == "PM":
        am = False


    if optional != None:
        optional = optional.lower()
        day_of_the_week = True

        if optional == "monday":
            day = 0
        elif optional == "tuesday":
            day = 1
        elif optional == "wednesday":
            day = 2
        elif optional == "thursday":
            day = 3
        elif optional == "friday":
            day = 4
        elif optional == "saturday":
            day = 5
        elif optional == "sunday":
            day = 6
    else:
        day_of_the_week = False

    # calculate output #

    new_minutes = start_minutes + minutes

    new_hours = start_hours + hours

    x, new_minutes = divmod(new_minutes, 60)
    new_hours = new_hours + x

    y, new_hours = divmod(new_hours, 12)

    days_passed = 0
    while y > 0:
        if am:
            am = False
        else:
            am = True
            days_passed += 1
        y -= 1

    # convert to string #

    days = [", Monday", ", Tuesday", ", Wednesday", ", Thursday", ", Friday", ", Saturday", ", Sunday"]

    if day_of_the_week:
        non, day = divmod(days_passed + day, 7)
        weekday = days[day]
    else:
        weekday = ""

    if days_passed == 0:
        days_passed = ""
    elif days_passed == 1:
        days_passed = " (next day)"
    elif days_passed > 1:
        days_passed = " (" + str(days_passed) + " days later)"

    if am:
        am = " AM"
    elif not am:
        am = " PM"

    new_hours, new_minutes = str(new_hours), str(new_minutes)
    if new_hours == "0": new_hours = "12"
    zero = ""
    if len(new_minutes) == 1: zero = "0"

    return str(new_hours) + ":" + zero + new_minutes + am + weekday + days_passed