import logging

logging.basicConfig(filename='shithaun1.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')




class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        

    def setName(self, name):
        if name.isalpha():
            self.name = name
            logging.info(f'Name set: {name}')
        else:
            logging.warning(f'Invalid name: {name}')

    def getName(self):
        return self.name

    def setAge(self, age):
        try:
            if age > 0:
                self.age = age
                logging.info('Age set successfully.')
        except:
            logging.error('Error while setting age.')
        

    def getAge(self):
        return self.age

    def setGender(self, gender):
        if gender == 'M' or gender == 'F':
            self.gender = gender
            logging.info(f'Gender set: {gender}')
        else:
            logging.warning(f'Invalid gender: {gender}')
       

    def getGender(self):
        return self.gender
    
    def validateName(self,name):

        for i in name:
            if i.isalpha():
                return False
        return True
    
    


    