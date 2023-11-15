class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}")

    def set_age(self, age):
        self.age = age


p1 = Person("Prakhar")
p1.set_age(18)
p1.say_hello(), print(p1.age)
 