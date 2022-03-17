from unicodedata import name


class Person:
    name ="Person"
    age =''
    def __init__(self, name,age):
        self.name = name
        self.age = age
jeffrey = Person("Jeffrey","2")
print('%s name is %s %s tuoi' %(Person.age, jeffrey.name,jeffrey.age))