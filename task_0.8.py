def plural_singular(hour, minutes):
    if hour > 1 and minutes > 1:
        return f"{hour} hours, {minutes} minutes"
    elif hour <= 1 and minutes > 1:
        return f"{hour} hour, {minutes} minutes"
    elif hour > 1 and minutes <= 1:
        return f"{hour} hours, {minutes} minute"
    else:
        return f"{hour} hour, {minutes} minute"
        
def hour_minute(number):
    hour = 0
    minutes = 0
    
    while isinstance(number, int):
        if number >= 60:
            number -= 60
            hour += 1
        else:
            minutes = number
            break
        
    return plural_singular(hour, minutes)