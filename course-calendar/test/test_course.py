import sys
sys.path.append("../")

from course import Course


# {'summary': 'CSE 16 - Appl Discrete Math', 'location': 'Earth&Marine B214', 'start': {'dateTime': '2024-01-11T17:20:00', 'timeZone': 'America/Los_Angeles'}, 'end': {'dateTime': '2024-01-11T18:25:00', 'timeZone': 'America/Los_Angeles'}, 'recurrence': ['RRULE:FREQ=WEEKLY;BYDAY=TH;UNTIL=20240316T182500Z']}
# CSE 16 - Appl Discrete Math (Discussion)
# Th 5:20PM - 6:25PM
# Earth&Marine B214
# 2024-01-08 to 2024-03-15

#self, code, comp, days, times, loc, start, end):
def test():
    course = Course("CSE 16 - Appl Discrete Math", "Discussion", "Th", "5:20PM - 6:25PM",
                    "Earth&Marine B214", "01/08/2024", "03/15/2024")
    
    assert course.title == "CSE 16 - Appl Discrete Math (Discussion)"
    assert course.code == "CSE 16 - Appl Discrete Math"
    assert course.days == "Th"
    assert course.time == "5:20PM - 6:25PM"
    assert course.location == "Earth&Marine B214"
    assert course.start == "2024-01-08"
    assert course.end == "2024-03-15"
    
    return course
    
if __name__ == "__main__":
    test()