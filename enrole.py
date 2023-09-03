class Enrole:
    def __init__(self, stud, tech,cour, grade=None):
        self.enrole_student = stud
        self.enrole_course = cour
        self.grade = grade
        self.teacher=tech


    def setEnroleStudent(self, stud):
        self.enrole_student = stud

    def getEnroleStudent(self):
        return self.enrole_student

    def setGrade(self, grade):
        self.grade = grade

    def getGrade(self):
        return self.grade

    def computeGPA(self):
        if self.grade=='A':
        
            return self.enrole_course.getCourseWeight() * 4
        elif self.grade=='B':
            return self.enrole_course.getCourseWeight() * 3
        
        elif self.grade=='C':
            return self.enrole_course.getCourseWeight() * 2
        elif self.grade=='D':
            return self.enrole_course.getCourseWeight() * 1