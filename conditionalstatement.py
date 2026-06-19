#if-elif-else statement

age = int(input("Enter your age: "))
if(age <= 13):
    print("child")
elif(age > 13 and age < 18):
    print("teenager")
else:
    print("adult")

#Nested if statement

username = input("Enter your username: ")
password = input("Enter your password: ")
if(username == "admin" and password == "admin123"):
    print("Login successful")
else:
    if(username != "admin"):
        print("Invalid username")
    else:
        print("Invalid password")