class Person:
    def __init__(self, name):
        self.name = name


    def say_hello(self):
        print(f"Hello, {self.name}")

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

p1 = Person("Prakhar")
print(p1.name)
p1.set_age(18)
print(p1.get_age())
