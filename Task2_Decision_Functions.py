# ==========================================================
# TASK 2: Python Decision Making & Functions
# Developed by: Sanjay Jangid
# File Name: Task2_Decision_Functions.py
# ==========================================================

print("\n========== TASK 2: PYTHON DECISION MAKING & FUNCTIONS ==========\n")

# ==========================================================
# Task 2.1: Conditional Statements
# ==========================================================

# ----------------------------------------------------------
# Program 1: Check Positive or Negative Number
# ----------------------------------------------------------
print("\n----- Program 1: Positive or Negative -----")

num = float(input("Enter a number: "))

if num >= 0:
    print("Positive Number")
else:
    print("Negative Number")


# ----------------------------------------------------------
# Program 2: Voting Eligibility
# ----------------------------------------------------------
print("\n----- Program 2: Voting Eligibility -----")

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")


# ----------------------------------------------------------
# Program 3: Even or Odd Number
# ----------------------------------------------------------
print("\n----- Program 3: Even or Odd -----")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# ==========================================================
# Nested If Programs
# ==========================================================

# ----------------------------------------------------------
# Program 4: College Admission Eligibility
# ----------------------------------------------------------
print("\n----- Program 4: College Admission -----")

marks = int(input("Enter Marks: "))
age = int(input("Enter Age: "))

if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Age criteria not satisfied")
else:
    print("Insufficient Marks")


# ----------------------------------------------------------
# Program 5: ATM Withdrawal Validation
# ----------------------------------------------------------
print("\n----- Program 5: ATM Withdrawal -----")

balance = 10000
amount = float(input("Enter withdrawal amount: "))

if amount <= balance:
    if amount > 0:
        balance -= amount
        print("Transaction Successful")
        print("Remaining Balance:", balance)
    else:
        print("Invalid Amount")
else:
    print("Insufficient Balance")


# ----------------------------------------------------------
# Program 6: Employee Bonus Eligibility
# ----------------------------------------------------------
print("\n----- Program 6: Employee Bonus -----")

years = int(input("Enter years of service: "))
salary = float(input("Enter salary: "))

if years >= 5:
    bonus = salary * 0.10
    print("Bonus Amount:", bonus)
else:
    print("Not Eligible for Bonus")


# ==========================================================
# Elif Programs
# ==========================================================

# ----------------------------------------------------------
# Program 7: Grade Classification
# ----------------------------------------------------------
print("\n----- Program 7: Grade Classification -----")

marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


# ----------------------------------------------------------
# Program 8: Traffic Signal Simulation
# ----------------------------------------------------------
print("\n----- Program 8: Traffic Signal -----")

signal = input("Enter Signal Color (red/yellow/green): ").lower()

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")


# ----------------------------------------------------------
# Program 9: Weather Recommendation
# ----------------------------------------------------------
print("\n----- Program 9: Weather Recommendation -----")

weather = input("Enter Weather (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print("Wear Sunglasses")
elif weather == "rainy":
    print("Carry an Umbrella")
elif weather == "cold":
    print("Wear Warm Clothes")
else:
    print("Enjoy your day!")


# ==========================================================
# Multiple Conditions (and, or, not)
# ==========================================================

# ----------------------------------------------------------
# Program 10: Login Validation (and)
# ----------------------------------------------------------
print("\n----- Program 10: Login Validation -----")

username = "admin"
password = "1234"

u = input("Username: ")
p = input("Password: ")

if u == username and p == password:
    print("Login Successful")
else:
    print("Invalid Credentials")


# ----------------------------------------------------------
# Program 11: Loan Eligibility (and)
# ----------------------------------------------------------
print("\n----- Program 11: Loan Eligibility -----")

age = int(input("Enter Age: "))
income = float(input("Enter Monthly Income: "))

if age >= 21 and income >= 30000:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")


# ----------------------------------------------------------
# Program 12: Scholarship Eligibility (and)
# ----------------------------------------------------------
print("\n----- Program 12: Scholarship Eligibility -----")

marks = int(input("Enter Marks: "))
income = float(input("Enter Family Income: "))

if marks >= 85 and income <= 500000:
    print("Scholarship Granted")
else:
    print("Not Eligible")


# ----------------------------------------------------------
# Program 13: OR Operator Example
# ----------------------------------------------------------
print("\n----- Program 13: OR Operator Example -----")

attendance = 80
sports = True

if attendance >= 75 or sports:
    print("Eligible for Event")
else:
    print("Not Eligible")


# ----------------------------------------------------------
# Program 14: NOT Operator Example
# ----------------------------------------------------------
print("\n----- Program 14: NOT Operator Example -----")

is_banned = False

if not is_banned:
    print("Access Granted")
else:
    print("Access Denied")


# ==========================================================
# Task 2.2: Create Reusable Functions
# ==========================================================

print("\n========== FUNCTIONS ==========\n")


# ----------------------------------------------------------
# Function with Parameters
# ----------------------------------------------------------
def greet(name):
    print("Hello", name)

greet("Sanjay")


# ----------------------------------------------------------
# Return Value Function
# ----------------------------------------------------------
def add(a, b):
    return a + b

result = add(10, 20)
print("Addition:", result)


# ----------------------------------------------------------
# Default Parameter Function
# ----------------------------------------------------------
def welcome(name="Guest"):
    print("Welcome", name)

welcome()
welcome("Sanjay")


# ----------------------------------------------------------
# Scope Demonstration
# ----------------------------------------------------------
x = 100

def demo():
    y = 50
    print("Global Variable x =", x)
    print("Local Variable y =", y)

demo()


# ==========================================================
# Task 2.3: Practice Coding Projects
# ==========================================================

print("\n========== MINI PROJECTS ==========\n")


# ----------------------------------------------------------
# Project 1: Grade Calculator
# ----------------------------------------------------------
print("\n----- Project 1: Grade Calculator -----")

marks = int(input("Enter Marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C"

print("Grade:", grade)


# ----------------------------------------------------------
# Project 2: Temperature Converter
# ----------------------------------------------------------
print("\n----- Project 2: Temperature Converter -----")

celsius = float(input("Enter Temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit, "°F")


# ----------------------------------------------------------
# Project 3: Simple Login Validation
# ----------------------------------------------------------
print("\n----- Project 3: Login Validation -----")

stored_username = "admin"
stored_password = "1234"

user = input("Username: ")
pwd = input("Password: ")

if user == stored_username and pwd == stored_password:
    print("Login Successful")
else:
    print("Login Failed")


# ----------------------------------------------------------
# Project 4: Factorial Using Functions
# ----------------------------------------------------------
print("\n----- Project 4: Factorial Calculator -----")

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


number = int(input("Enter a Number: "))

if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print("Factorial:", factorial(number))


print("\n========== TASK COMPLETED SUCCESSFULLY ==========")
