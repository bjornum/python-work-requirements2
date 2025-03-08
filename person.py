# Part of Task 3: Simple Class and Inheritance

## Person Class, who accept a name and age attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    ## Greeting displaying the name and age of the student
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
## Student Class, who Inherit the Person Class.
class Student(Person):
    def __init__(self, name, age, student_id):
        Person.__init__(self, name, age)
        self.student_id = student_id