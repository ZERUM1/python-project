class Course:
    def __init__(self, course_name, course_code, course_weight):
        self.course_name = course_name
        self.course_code = course_code
        self.course_weight = course_weight

    def setCourseName(self, course_name):
        self.course_name = course_name

    def getCourseName(self):
        return self.course_name

    def setCourseCode(self, course_code):
        self.course_code = course_code

    def getCourseCode(self):
        return self.course_code

    def setCourseWeight(self, course_weight):
        self.course_weight = course_weight

    def getCourseWeight(self):
        return self.course_weight