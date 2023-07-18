# OOP
''' 
4 pillars 
1) Abstraction => a way to create a class and put order in your code (readable, maintainable)
2) Inheritance => You can maintain attributes/methods from "parent" class
3) Polymorphysm => You can override methods from parent class to do specific things
4) Encapsulation => Public, Protected, Private methods
'''
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    @abstractmethod
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id, studied_subject):
        super().__init__(name, age)
        self.student_id = student_id
        self.studied_subject = studied_subject
    
    def say_hello(self):
        super().say_hello()
        print(f"I am a student with ID {self.student_id}.")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    @staticmethod
    def is_good_picture():
        return print('Hi yes its ok')

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")
    
    def display_balance(self):
        print(f"Account balance: {self.balance}")



# Functions x Methods
'''
def
Methods are in scope of a class => self
# Attributes => "the parameter" in the constructor
## cls x self 
# cls => refering to class itself (@classmethod)
# self => instance of class
# staticmethods => (@classmethod)

## classmethod x staticmethod

'''
if __name__ == '__main__':
    a = BankAccount(1,'me')
    a.deposit(100)
    a.withdraw(20)
    a.display_balance()









