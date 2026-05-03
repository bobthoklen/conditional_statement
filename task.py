

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