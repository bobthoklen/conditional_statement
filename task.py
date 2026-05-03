#1. Check number between 1 and 100
num = int(input("Enter a number: "))
if 1 <= num <= 100:
    print("Number is between 1 and 100")
else:
    print("Number is NOT between 1 and 100")

#2. Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd") 

#3. Month from number
num = int(input("Enter month number (1-12): "))

months = {
    1: "January", 2: "February", 3: "March",
    4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September",
    10: "October", 11: "November", 12: "December"
}

if num in months:
    print(months[num])
else:
    print("Invalid input")

#4. Grading system
marks = int(input("Enter marks: "))

if marks < 25:
    print("F")
elif marks < 45:
    print("E")
elif marks < 50:
    print("D")
elif marks < 60:
    print("C")
elif marks < 80:
    print("B")
else:
    print("A")

#5. Divisible by 7
num = int(input("Enter a number: "))
if num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")

#6. Simple Calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Answer:", a + b)
elif op == "-":
    print("Answer:", a - b)
elif op == "*":
    print("Answer:", a * b)
elif op == "/":
    print("Answer:", a / b)
else:
    print("Invalid operator")

#7. Car loan eligibility
salary = int(input("Enter salary: "))
credit = int(input("Enter credit score: "))

if salary >= 50000 and credit >= 700:
    print("Eligible")
else:
    print("Not Eligible")

#8. FizzBuzz
n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
elif n % 3 == 0:
    print("Fizz")
else:
    print(n)   

# 9. Vowel or Consonant
ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#10. Grade system (2)
marks = int(input("Enter marks: "))

if 90 <= marks <= 100:
    print("A")
elif 80 <= marks <= 89:
    print("B")
elif 70 <= marks <= 79:
    print("C")
else:
    print("Fail")

#11. Age category
age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")


#12. Character type
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Other")

#13. Traffic light
color = input("Enter color: ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")

#14. Job eligibility
age = int(input("Enter age: "))
exp = int(input("Enter experience (years): "))

if age > 18 and exp >= 2:
    print("Eligible")
else:
    print("Not Eligible")

#15. Temperature advice
temp = float(input("Enter temperature: "))

if temp > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temp <= 30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")

#16. Menu price
item = input("Enter item (Pizza/Burger/Pasta): ").lower()

menu = {
    "pizza": 10,
    "burger": 7,
    "pasta": 8
}

if item in menu:
    print("Price: $", menu[item])
else:
    print("Item not found")

#17. Height selection
height = float(input("Enter height (feet): "))

if height >= 6:
    print("Selected")
else:
    print("Not Selected")

#18. Movie eligibility
age = int(input("Enter age: "))

if age >= 18:
    print("Allowed")
else:
    print("Not Allowed")
    
#19. Write a Python program to check login credentials:
 #Username: "admin", Password: "password123"
 #If correct, print "Access Granted"; otherwise, print "Access Denied."

username=input("enter your usename. ")
if username != 'admin':
   print("invalid username.")
else:
   password=input("enter your password ")
   if password == 'password123':
      print("Valid username and password.")
   else:
      print("Invalid password.")
   

#20. Write a Python program that takes a month number (1–12) and outputs the corresponding season:

 #12, 1, 2: "Winter"
 #3, 4, 5: "Spring"
 #6, 7, 8: "Summer"
 #9, 10, 11: "Autumn

monthh = int(input("Enter month number (1-12): "))

if monthh in (12, 1, 2):
    print("Winter")
elif monthh in (3, 4, 5):
    print("Spring")
elif monthh in (6, 7, 8):
    print("Summer")
elif monthh in (9, 10, 11):
    print("Autumn")
else:
    print("Invalid month")