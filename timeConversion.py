'''
Question:
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
'''

def timeConversion(time):
    time_sign = time[8:]
    time = time[:8]
    if time_sign == "AM":
        if time.startswith("12"):
            return "00" + time[2:]
        else:
            return time
    elif time_sign == "PM":
        if time.startswith("12"):
            return time
        else:
            hour = str(int(time[:2]) + 12)
            return hour + time[2:]
