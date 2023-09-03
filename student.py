from person import Person
class Student(Person):
    def __init__(self,name,age,gender,id):
        super().__init__(name,age,gender)
        self.id=id

        
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id