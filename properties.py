# class Person:
#     def __init__(self, name):
#         self.name = name
#         self._salary = 0
#
#     def set_salary(self, salary):
#         if salary < 0:
#             raise ValueError("Invalid Salary.")
#         self._salary = salary  # Not totally private cause it can still be accesed but then we consider it to be private
#
#     def get_salary(self):
#         return round(self._salary)
#
#     salary = property(get_salary,
#                       set_salary)  # Combines the set_salary and get_salary, and now we don't have to cal both the
#     # properties separately
#
#
# p1 = Person("Prakhar")
# p1.salary = 2090
# print(p1.name + ",", p1.salary)

# class Time:
#     def __init__(self, second):
#         self._second = second
#
#     def set_second(self, second):
#         if second > 60 or second < 0:
#             raise ValueError("Invalid second!")
#         self._second = second
#
#     def get_second(self):
#         return self._second
#
#     second = property(ge1t_second, set_second)


# t = Time(54)
# t.second = 59
# print(t.second)

# class BankAccount:
#     def __init__(self, account_holder_name):
#         self.account_holder_name = account_holder_name
#         self._balance = 0
#
#     def set_balance(self, balance):
#         if balance > 10000 or balance < 0:
#             raise ValueError("Balance out of limits!")
#         self._balance = round(balance)
#
#     def get_balance(self):
#         return self._balance
#
#     balance = property(get_balance, set_balance)
#
