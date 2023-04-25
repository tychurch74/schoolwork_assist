
"""
OOP or Object Oriented Programming is a programming paradigm that uses objects and classes to organize code.
Classes are like blueprints for objects. They define the structure and behavior of an object.

A good anology is that of a car factory. The factory is like a class, and the cars are like objects.
The factory is responsible for creating the cars, and the cars are all built the same way.

Classes have attributes and methods. Attributes are like variables, and methods are like functions.
Attributes are defined in the constructor method, which is called when an object is created.
The self keyword is used to refer to the current object. It is used to access attributes and methods of the object.

Continuing with the car anoalogy, the attributes of a car would be things like the color, make, model, and year.
The methods of a car would be things like starting the engine, turning the wheel, and pressing the gas pedal.
"""

# Create a simple bank account management system with classes for Account, Customer, and Bank. 
# Implement methods for depositing, withdrawing, and checking balances.


# Define the Account class, which represents a bank account
class Account:
    # The docstring below (between the triple quotes) is used to document the class. It's a good practice to document classes and methods.
    # Hovering over the class or method name anywhere in the code will display the docstring.
    """
    Attributes:
        balance (float): The current balance of the account
        
    Methods:
        deposit(amount): Deposits the specified amount into the account
        withdraw(amount): Withdraws the specified amount from the account if sufficient funds are available
        check_balance(): Returns the current balance of the account
        
    """
    # Constructor method for initializing an account with a given balance
    def __init__(self, balance):
        self.balance = balance

    # Method to deposit a specified amount into the account
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # Method to withdraw a specified amount from the account if sufficient funds are available
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

    # Method to check the current balance of the account
    def check_balance(self):
        return self.balance


# Define the Customer class, which represents a customer with a bank account
class Customer:
    """
    Attributes:
        name (str): The name of the customer
        account (Account): The customer's bank account
        
    Methods:
        deposit(amount): Deposits the specified amount into the customer's account
        withdraw(amount): Withdraws the specified amount from the customer's account if sufficient funds are available
        check_balance(): Returns the current balance of the customer's account
        
    """
    
    # Constructor method for initializing a customer with a given name and account
    def __init__(self, name, account):
        self.name = name
        self.account = account

    # Method to deposit a specified amount into the customer's account
    def deposit(self, amount):
        self.account.deposit(amount)
        return self.account.balance

    # Method to withdraw a specified amount from the customer's account if sufficient funds are available
    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self.account.balance

    # Method to check the current balance of the customer's account
    def check_balance(self):
        return self.account.check_balance()


# Define the Bank class, which represents a bank with customers
class Bank:
    """
    Attributes:
        name (str): The name of the bank
        customers (dict): A dictionary of customers, where the key is the customer's name and the value is the customer object
        
    Methods:
        add_customer(name, account): Adds a customer to the bank with the specified name and account
        remove_customer(name): Removes a customer from the bank with the specified name
        get_customer(name): Returns the customer object with the specified name
        get_customers(): Returns a dictionary of all customers in the bank
        
    """
    
    # Constructor method for initializing a bank with a given name
    def __init__(self, name):
        self.name = name
        self.customers = {}  # Initialize an empty dictionary to store customers

    # Method to add a customer to the bank
    def add_customer(self, name, account):
        self.customers[name] = Customer(name, account)

    # Method to remove a customer from the bank
    def remove_customer(self, name):
        del self.customers[name]

    # Method to get a specific customer from the bank by their name
    def get_customer(self, name):
        return self.customers[name]

    # Method to get all customers in the bank
    def get_customers(self):
        return self.customers


# The code below is the main execution block that demonstrates the functionality of the classes
if __name__ == "__main__":
    account1 = Account(1000)
    account2 = Account(2000)

    customer1 = Customer("John", account1)
    customer2 = Customer("Jane", account2)

    bank = Bank("Bank of America")
    bank.add_customer(customer1.name, customer1.account)
    bank.add_customer(customer2.name, customer2.account)

    print(bank.get_customers())
    print(bank.get_customer("John").check_balance())
    print(bank.get_customer("Jane").check_balance())
    print(bank.get_customer("John").deposit(100))
    print(bank.get_customer("Jane").withdraw(100))
    print(bank.get_customer("John").check_balance())
    print(bank.get_customer("Jane").check_balance())
    print(bank.get_customer("John").withdraw(2000))
    print(bank.get_customer("Jane").check_balance())
    bank.remove_customer("John")
    print(bank.get_customers())
