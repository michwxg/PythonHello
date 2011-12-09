def fibs(num):    
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

class Person:
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm %s\n" % self.name)
        
class Student(Person):
    def greet(self):
        Person.greet(self)
        print("i'm student")

miko = Student()
miko.setName('miko')
miko.greet() 
