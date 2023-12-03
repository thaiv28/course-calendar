import event
import parse
import main
import api
import cal

if __name__ == "__main__":
    filepath = '../../files/test/schedule.pdf'
    
    service = api.connect()
    courses = parse.parse_pdf(filepath)
    calendar, cal_id = cal.get_calendar(service)
    
    
    time_zone = calendar["timeZone"]

    event_list = []

    for c in courses:
        event_list.append(event.course_to_event(c, time_zone))
  
    for e in event_list:
        if e != None:
            print(e)
            