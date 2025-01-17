def add_time(start, duration, starting_day = None):

    # Days of the week
    days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    # Parse start time
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))
    if period == 'PM':
        start_hours += 12

    # Parse duration
    duration_hours, duration_minutes = map(int, duration.split(':'))
    
    # Add duration to start time
    end_minutes = start_minutes + duration_minutes
    end_hours = start_hours + duration_hours + end_minutes // 60
    end_minutes %= 60
    days_later = end_hours // 24
    end_hours %= 24

    # Determine AM/PM
    if end_hours >= 12:
        period = 'PM'
        end_hours -= 12
    else:
        period = 'AM'
    if end_hours == 0:
        end_hours = 12

    # Construct the new time string
    new_time = f"{end_hours}:{end_minutes:02d} {period}"

    # Add day of the week if provided
    if starting_day:
        day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    # Add day information
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
 
    return new_time