class Car:
    def __init__(self,name,engine,wheels,doors):
        #creating object calls init(constructor)
        # instance variable - self
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
    # instance method
    def horn(self):
        return f"{self.name} says vroom vroom"

ferrari = Car("ferrari","v8",4,4)#object
alto = Car("alto","v8",4,4) #object
mclaren = Car("mcLaren", "v8", 4, 2)
mercedes = Car("G-Wagon", "v8", 4, 5)

# print(ferrari["name"]) # error

print(type(ferrari),type("cool")) # <class '__main__.Car'> <class 'str'>
print(ferrari.name,ferrari.wheels)

print(ferrari.horn())
print(alto.horn())

# Task 1

#bank account
# 1.acc_no
# 2.name
# 3.balance

# amisha 500
# mathesh 700
# sai ganesh 665

class Bank_Account_1:
    def __init__(self,account_no,name,balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def display_balance(self):
        return f"your balance is : ₹ {self.balance:,}"
    
    def withdraw(self,amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            return f"success,{self.display_balance()}" 
        else:
            return f"insufficient funds,{self.display_balance()}"
    def deposit(self,amount):
        self.balance = self.balance + amount
        return f"success,{self.display_balance()}"
    
amisha = Bank_Account_1(123,"amisha",50000)
mathesh = Bank_Account_1(124,"mathesh",700)
sai_ganesh = Bank_Account_1(125,"sai ganesh",665)


print(amisha.balance)

# task 2

print(amisha.display_balance()) # your balance is ₹50,000

# task 3

#mathesh withdraw(100) # success,your balance is: ₹600
# mathesh.display_balance() # your balance is: ₹600
print(mathesh.display_balance())
print(mathesh.withdraw(10_000))



#task 4
# sai.deposit(100) #success your balance is ₹765
#sai.display_balance() # your balance is: ₹765
print(mathesh.deposit(100))

# Encapsulation: properties + action(logic)

class Bank_Account_1:
    # class variable | all your instance share the class variable
    interest_rate = 0.02

    def __init__(self,account_no,name,balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def display_balance(self):
        return f"your balance is : ₹ {self.balance:,}"
    
    def withdraw(self,amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            return f"success,{self.display_balance()}" 
        else:
            return f"insufficient funds,{self.display_balance()}"
    def deposit(self,amount):
        self.balance = self.balance + amount
        return f"success,{self.display_balance()}"
    def appy_interest(self):
        self.balance=self.balance + self.balance * Bank_Account_1.interest_rate
        return f"{self.display_balance()}"
    
tonika= Bank_Account_1(123,"tonika",50000)
mat = Bank_Account_1(124,"mat",700000)

print(Bank_Account_1.interest_rate)


#task 4
#after 1 year
tonika.appy_interest()
mat.appy_interest()

print(tonika.display_balance())

