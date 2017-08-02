from using_class import Person


class Student(Person):

    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary

    def show(self):
        print self.__str__(), 'salary:', self.salary


stu1 = Student('dean', 18, 20000)

stu1.show()
