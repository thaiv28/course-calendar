class Course():
    
    def __init__(self, code, comp, days, times, loc, start, end):
        self.code = code
        self.comp = comp
        self.days = days
        self.times = times
        self.loc = loc
        self.start = start
        self.end = end
    
    def __str__(self):
   
        string = ''
        string += self.code + " (" + self.comp + ")\n"
        string += self.days + " " + self.times + "\n"
        string += self.loc + "\n"
        string += self.start + " - " + self.end + "\n"
        string += "--------------"
        
        return string
        