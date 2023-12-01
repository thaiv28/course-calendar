import datetime
from course import Course
import api

def course_to_event(course, time_zone):
    if(course.time == 'TBA'):
        return None
    
    
    time_split = course.time.split(" ")
    start_time = time_split[0]
    end_time = time_split[2]
    
    class_start_dt = convert_time(course.start, start_time)
    class_end_dt = convert_time(course.start, end_time)
    
    quarter_end_dt = convert_time(course.end, end_time)
    quarter_end_dt = quarter_end_dt + datetime.timedelta(days=1)
    
    days = convert_days(course.days)
    
    # set first class time to actual first date (not just first day of the
    # quarter)
    day_list = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']
    while day_list[class_start_dt.weekday()] not in days:
        class_start_dt += datetime.timedelta(days=1)
        class_end_dt += datetime.timedelta(days=1)
    
    event = {
        'summary': course.code,
        'location': course.location,
        'start': {
            'dateTime': class_start_dt.isoformat(),
            'timeZone': time_zone,
        },
        'end': {
            'dateTime': class_end_dt.isoformat(),
            'timeZone': time_zone,
        },
        'recurrence': [
            'RRULE:FREQ=WEEKLY;BYDAY='+days+';UNTIL='
            +str(quarter_end_dt.isoformat().replace("-","").replace(":","")
                 + "Z")
        ],
    }
    
    print(event)
    
    return event

def convert_days(days):
    abbr = []
    
    if 'Su' in days: abbr.append('SU')
    if 'Mo' in days: abbr.append('MO')
    if 'Tu' in days: abbr.append('TU')
    if 'We' in days: abbr.append('WE')
    if 'Th' in days: abbr.append('TH')
    if 'Fr' in days: abbr.append('FR')
    if 'Sa' in days: abbr.append('SA')
    
    return ','.join(abbr)
        
    
def convert_time(date, time):

    time = time.split(":")
    hr = int(time[0])
    min = int(time[1][0:2])
    if "PM" in time[1]:
        hr += 12
        
    date = date.split("-")
    
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    
    return datetime.datetime(year, month, day, hour=hr, minute=min)
    
        
if __name__ == "__main__":
    pass
    