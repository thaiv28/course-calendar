import datetime

class Course():
    
    def __init__(self, code, comp, days, times, loc, start, end):
        self.title = self.create_title(code, comp)
        self.code = code
        self.comp = comp
        self.days = days
        self.time = times
        self.location = loc
        self.start = self.convert_date_format(start)
        self.end = self.convert_date_format(end)
        
    def convert_date_format(self, date):
        month = date[:2]
        day = date[3:5]
        year = date[6:]
        
        return year + "-" + month + "-" + day

    def create_title(self, code, comp):
        title = code + " (" + comp + ")"
        return title
        
    def __str__(self):
   
        string = ''
        string += self.code + " (" + self.comp + ")\n"
        string += self.days + " " + self.time + "\n"
        string += self.loc + "\n"
        string += self.start + " to " + self.end + "\n"
        string += "--------------"
        
        return string
        