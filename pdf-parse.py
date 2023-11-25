from pdfquery import PDFQuery
from pdfquery.cache import FileCache
import course

pdf = PDFQuery('./schedule.pdf')
pdf.load()

pdf.tree.write('test.xml', pretty_print=True)

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
        components.append(comp)
        
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
        space = text.find(' ')
        days.append(text[:space])
        times.append(text[space + 1:])
        
    print(days)
    print(times)

