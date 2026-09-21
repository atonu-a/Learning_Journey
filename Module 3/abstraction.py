from abc import ABC, abstractmethod

class BankAccount:
    @abstractmethod #Now this method is mandatory to create in every class
    def withdraw(self):
        print("Money withdrawn from normal account!")
class SavingsAccount(BankAccount):
    def withdraw(self): 
        print("Money withdrawn from normal account!")
class CurrentAccount(BankAccount):
    def withdraw(self):
        print("Money withdrawn from normal account!")
        
        
class StudentAccount(BankAccount):
    def withdraw(self): 
        print("Money withdrawn from normal account!")