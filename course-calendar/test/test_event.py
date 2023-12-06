import test_course

import sys
sys.path.append("../")

import event

def test():
    course = test_course.test()
    
    # {
        # 'summary': 'CSE 16 - Appl Discrete Math', 'location': 'Earth&Marine B214', 
        # 'start': {'dateTime': '2024-01-09T17:20:00', 'timeZone': 'America/Los_Angeles'}, 
        # 'end': {'dateTime': '2024-01-09T18:25:00', 'timeZone': 'America/Los_Angeles'}, 
        # 'recurrence': ['RRULE:FREQ=WEEKLY;BYDAY=TU,TH;UNTIL=20240316T182500Z']
    # }
    
    e = event.course_to_event(course, "America/Los_Angeles")
    # print(e)
    assert event.convert_days(course.days) == "TU,TH"
    assert str(event.convert_time(course.start, course.time)) == "2024-01-08 17:20:00"
    assert e['summary'] == 'CSE 16 - Appl Discrete Math (Discussion)'
    assert e['start']['dateTime'] == '2024-01-09T17:20:00'
    assert e['end']['dateTime'] == '2024-01-09T18:25:00'
    assert e['recurrence'] == ['RRULE:FREQ=WEEKLY;BYDAY=TU,TH;UNTIL=20240316T182500Z']
    

if __name__ == "__main__":
    test()