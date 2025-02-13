#Exercise 1
age = int(input("Enter your age: "))
if age < 0:
    print( "invalid input")
elif age < 3:
    print( "Free")
elif age >= 3 and age <= 12:
    print( "$10")
elif age >= 13 and age <= 59:
    print( "$15")
elif age >= 60:
    print( "$8")
else:
    print( "invalid input")

#Exercise 2-1

number = int(input("Enter a number: "))

if number //2 == number / 2 :
    print("Even")
else:
    print("Odd")

#Exercise 2-2

number = int(input("Enter a number: "))
if number %2 == 0 :
    print("Even")
else:
    print("Odd")

#Exercise 2-3

number = int(input("Enter a number: "))
if number & 1 == 0:
    print("Even")
else:
    print("Odd")

#Exercise 3

username= input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")