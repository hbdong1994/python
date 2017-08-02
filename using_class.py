import copy


class Person:

    log = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.log += 1   # if use self ,then the obj point to current obj of instantiation
        Person.log += 1  # if use the Class , then same as static param

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return self.name, self.age

obj = Person('dean', 16)

copy_obj = copy.copy(obj)  # copy copy this obj

obj.set_age(18)
obj.set_name('xiaoen')
print obj.get_age(), obj.get_name()

print 'obj : ', obj.__str__()  # orign is
print 'copy :', copy_obj.__str__()  #copy obj is


p1 = Person('dany', 21)
p2 = Person('show', 123)
p3 = Person('ddd', 13)

print Person.log    # if Person.log then 4  if self.log then 1



