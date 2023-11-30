import datetime
from course import Course

def course_to_event(course):
    if(course.time == 'TBA'):
        return None
    
    
    time_split = course.time.split(" ")
    start_time = time_split[0]
    end_time = time_split[2]
    
    start_dt = convert_time(course.start, start_time)
    end_dt = convert_time(course.start, end_time)
    
    event = {
        'summary': course.code,
        'location': course.loc,
        'start': {
            'dateTime': start_dt.isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end_dt.isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
    }
    
    print(event)
    
    return event
    
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
    convert_time(Course())
    