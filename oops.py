# Day 4 - Classes and Objects


# Class and Object

class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)


student1 = Student("Vanshika", 101)

student1.display()

print()


# Single Inheritance

class Person:

    def speak(self):
        print("Person can speak.")


class Teacher(Person):

    def teach(self):
        print("Teacher teaches students.")


t1 = Teacher()

t1.speak()
t1.teach()

print()


# Multilevel Inheritance

class Animal:

    def eat(self):
        print("Animal eats food.")


class Dog(Animal):

    def bark(self):
        print("Dog barks.")


class Puppy(Dog):

    def play(self):
        print("Puppy plays.")


p = Puppy()

p.eat()
p.bark()
p.play()

print()


# Using super()

class Employee:

    def __init__(self, name):
        self.name = name


class Manager(Employee):

    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Department:", self.department)


m = Manager("Vanshika", "IT")

m.display()