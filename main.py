from student import Student
from course import Course
from enrole import Enrole
from teacher import Teacher
from person import Person

studentobj = Student(name='Abebe', age=16, gender='M', id='ID01')
courseobj1 = Course('Introduction to python', 'cs01', 6)
courseobj2 = Course('Introduction to java', 'cs02', 6)

teacher1=Teacher(name='kebede', age=35, gender='M', type='lecture')
enroleobj1 = Enrole(stud=studentobj, cour=courseobj1,tech=teacher1)
enroleobj2 = Enrole(stud=studentobj, cour=courseobj2,tech=teacher1)
personObj = Person (name="abebe", age=12, gender ="M")

#print("Name:", studentobj.getName())
print("Age:", personObj.getAge())
personObj.setAge("s")
personObj.setName('ZERUBABEL122')
personObj.setGender('P')

#print(enroleobj1.setGrade('C'))

#print(studentobj.getName())
#print(courseobj1.getCourseName())
#studentobj.setName('zerubabel')
#print(studentobj.getName())

#print('{} {} {}'.format(studentobj.name,studentobj.age,studentobj.gender))

