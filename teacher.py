from person import Person
class Teacher(Person):
    def __init__(self,name,age,gender,type):
        super().__init__(name,age,gender)
        self.type=type