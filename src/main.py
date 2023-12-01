import api
import event
import parse

def main():
    filepath = '../files/schedule.pdf'
    
    service = api.connect()
    courses = parse.parse_pdf(filepath)
    cal_dict = api.get_calendars(service)
    
    cal_id = cal_dict["API test"]
    calendar = service.calendarList().get(calendarId=cal_id).execute()
    time_zone = calendar["timeZone"]

    e_list = []

    for c in courses:
        e_list.append(event.course_to_event(c, time_zone))
  
    for e in e_list:
        if e != None:
            print(e)
            e = service.events().insert(calendarId=cal_id, body=e).execute()
            print('Event created: %s' % (e.get('htmlLink')))
            

if __name__ == "__main__":
    main()

