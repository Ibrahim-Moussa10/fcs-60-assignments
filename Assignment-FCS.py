#Exercise 1
age = int(input("Enter your age: "))
if age < 0:
    print( "invalid input")
if age < 3:
    print( "Free")
elif age >= 3 and age <= 12:
    print( "$10")
elif age >= 13 and age <= 59:
    print( "$15")
elif age >= 60:
    print( "$8")

