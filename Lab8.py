              #Task 1
class Car:
    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Manufacturing Year: {self.year}")
        print(f"Mileage: {self.mileage} miles")

    def drive(self, miles):
        self.mileage += miles
        print(f"Driven {miles} miles. New mileage: {self.mileage} miles.")

my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()
my_car.drive(100)

            #Task 2
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = []

    def add_marks(self, marks):
        self.marks.extend(marks)

    def average_marks(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def display_info(self):
        avg_marks = self.average_marks()
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Average Marks: {avg_marks:.2f}")

student = Student("Alice", 20)
student.add_marks([85, 90, 78])
student.display_info()

             #Task 3
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")

account = BankAccount("John Doe", 1000)
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)             