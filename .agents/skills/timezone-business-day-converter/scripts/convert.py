from datetime import datetime, timedelta
import pytz

def is_business_day(date):
    return date.weekday() < 5

def next_business_day(date):
    next_day = date + timedelta(days=1)
    while not is_business_day(next_day):
        next_day += timedelta(days=1)
    return next_day

def convert_time(input_time_str, input_tz_str):
    input_tz = pytz.timezone(input_tz_str)
    dt = datetime.strptime(input_time_str, "%Y-%m-%d %H:%M")
    dt = input_tz.localize(dt)

    timezones = ["UTC", "US/Pacific", "Europe/London"]

    for tz in timezones:
        converted = dt.astimezone(pytz.timezone(tz))
        print(tz, converted.strftime("%Y-%m-%d %H:%M"))

    print("Is business day:", is_business_day(dt))
    print("Next business day:", next_business_day(dt).strftime("%Y-%m-%d"))

if __name__ == "__main__":
    convert_time("2026-04-26 15:00", "US/Eastern")