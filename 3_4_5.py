import pickle
class Student:
    average_marks = 0
    grade = ""
    def __init__(self,name,roll,python_mark,TOC_mark,OS_mark,average_marks,grade):
        self.name = name
        self.roll = roll
        self.python_mark = python_mark
        self.TOC_mark = TOC_mark
        self.OS_mark = OS_mark
        self.average_marks = average_marks
        self.grade = grade


    def moderate_mark(self,grace_mark):
        self.TOC_mark += grace_mark 
        self.OS_mark += grace_mark
        self.python_mark += grace_mark

        if(self.TOC_mark > 100):
            self.TOC_mark = 100
        if(self.OS_mark > 100):
            self.OS_mark = 100 
        if(self.python_mark > 100):
            self.python_mark = 100 

    def average(self):
        self.average_marks = (self.TOC_mark+self.OS_mark+self.python_mark)/3

    def get_grade(self):
        if(self.average_marks<40):
            self.grade = 'D'
        elif(40<=self.average_marks<60):
            self.grade = 'C'
        elif(60<=self.average_marks<80):
            self.grade = 'B'
        elif(80<=self.average_marks):
            self.grade = 'A'

dbfile=open('StudentPickle','rb')#to read file from piclefile
Studentdata=pickle.load(dbfile)
for keys in Studentdata:
    Studentdata
        

