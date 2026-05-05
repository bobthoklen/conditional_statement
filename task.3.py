#1
age=int(input("enter your age in years. "))
height= int(input("enter your heigt in cm. "))
if age >= 12 and height >= 140:
    print("you can ride the roller coaster.")
else:
    print("you cannot ride the roller coaster.")

#2
color=input("enter any color. ")
colour={
    'red':'stop',
    'yellow':'wait',
    'green':'go'
}
if color.lower() in colour:
   print(colour[color])
else:
   print("invalid color")

#3
num=int(input("enter a number between 1-4. "))
season={
    1:'spring',
    2:'winter',
    3:'autumn',
    4:'summer'
}
if num in season:
    print(season[num])
else:
    print('invalid number')

#4
username=input("enter your username")
if username == 'admin':
    print("valid username.")
    password=input("enter your password")
    if password == 'pass123':
        print("valid password.")
    else:
        print("invalid password")
else:
    print("invalid username")