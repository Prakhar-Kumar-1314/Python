class Car:
    number_of_car = 0
    wheels = 4

    def __init__(self, company, model):
        self.company = company
        self.model = model
        Car.number_of_car += 1


c1 = Car("Ford", "Mustang")
c2 = Car("Porshe", 911)

print(c1.model, c1.number_of_car)

class Circle:
    pi = round(3.14)

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * (radius)

    property(ge)


c1 = Circle

print(c1.perimeter(12))
#
# class Employee:
#     number_of_employes = 0
#     Salary = 0
#     Age = 0
#
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         Employee.number_of_employes += 1
#         Employee.Salary += Employee.Salary
#         Employee.Age += Employee.Age
#
#     def average_age(self):
#         return Employee.Age / (Employee.number_of_employes)
#
#
# em = Employee("Prakhar", 36, 200)
#
# print(em.average_age)
