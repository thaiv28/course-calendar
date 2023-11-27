from pdfquery import PDFQuery
from pdfquery.cache import FileCache
from src.course import Course

def parse():
    pdf = PDFQuery('../files/schedule.pdf')
    pdf.load()

    pdf.tree.write('../files/test.xml', pretty_print=True)

    enrolled_labels = pdf.pq('LTTextLineHorizontal:contains("Status")')

    classes = []

    for i in enrolled_labels.items():
        left_edge = float(i.attr('x0'))
        right_edge = float(i.attr('x1'))
        bottom_edge = float(i.attr('y0'))
        top_edge = float(i.attr('y1'))
        
        # finds course code and title
        
        code_bbox = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' 
                    % (left_edge - 0.75, bottom_edge + 19.075, 
                        right_edge + 85.092, top_edge + 21.078))
        
        code = code_bbox.text()
        
        # creates list of components (lecture, lab, discussion, etc)
        
        component_bbox = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' 
                    % (left_edge + 76.079, bottom_edge - 101.958, 
                        right_edge + 96.054, top_edge - 68.463))
        
        components = []
        for comp in component_bbox.items():
            components.append(comp.text())
            

            
        # creates list of days and times
        
        days_times_bbox = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' 
                    % (left_edge + 135.75, bottom_edge - 99.213, 
                        right_edge + 160.834, top_edge - 62.208))
    
        days = []
        times = []
        days_times_str = []
        
        items = days_times_bbox.items()
        
        for i in items:
            
            if i.text()[-1] == '-':
                string = i.text() + ' ' + next(items).text()
                days_times_str.append(string)
            else:
                days_times_str.append(i.text())
        
        for text in days_times_str:
            space = text.strip().find(' ')
            if space != -1:
                days.append(text[:space])
                times.append(text[space + 1:])
            else:
                days.append(text)
                times.append(text)
            
        # create list of locations
        
        locations = []
        
        # adds locations for top row of each course (ex: the lecture sections)
        
        loc_bbox_two = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' 
                    % (left_edge + 222.27, bottom_edge - 77.056, 
                        right_edge + 272.086, top_edge - 59.551))
        
        items = loc_bbox_two.items()
        
        loc_string = ""
        for i in items:
            loc_string += i.text()
            loc_string += " "
        
        if loc_string != "":
            locations.append(loc_string.strip())
        
        # adds locations for bottom row of each course (ex: the lab section)

        loc_bbox_one = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' 
                    % (left_edge + 222.27, bottom_edge - 102.556, 
                        right_edge + 272.086, top_edge - 85.051))
        
        items = loc_bbox_one.items()
        
        loc_string = ""
        for i in items:
            loc_string += i.text()
            loc_string += " "
        
        if loc_string != "":
            locations.append(loc_string.strip())
            
        # creates list of start/end dates
        start = []
        end = []
        
        dates_bbox = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' 
                    % (left_edge + 382.02, bottom_edge - 102.556, 
                        right_edge + 428.836, top_edge - 59.551))
        
        items = dates_bbox.items()
        
        is_start = True
        for i in items:
            text = i.text()
            if is_start:
                start.append(text[:len(text) - 2])
            else:
                end.append(i.text())
            
            is_start = not is_start
            
        # add class to classes list 
        
        for i in range(len(components)):
            classes.append(Course(code, components[i], days[i], times[i], locations[i], start[i], end[i]))

    return classes

        
        

