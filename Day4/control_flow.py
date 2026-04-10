#Basic else-if

age = int(input("Enter your age: "))
if age>=18:
    print("You are an adult")
else:
    print("You are a minor")

print("-------------------------------")
#Comparison operators

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
if num1==num2:
    print("Both numbers are equal")     
elif num1>num2:
    print(f"{num1} number is greater")
elif num1<num2:
    print(f"{num2} number is greater")

print("-------------------------------")

#Elif ladder

score = int(input("Enter your score (0-100): "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

print("-------------------------------")

#Nestedif

user_name = "admin"
pass_word = "1234"
username = input("Enter username: ")
password = input("Enter password: ")

if username != user_name:
    print("Wrong Username")
elif password != pass_word:
    print("Wrong Password")
else:
    print("Login Successful")

print("-------------------------------")

#logical operations

num = int(input("Enter a number: "))
if (num > 0 and num % 2 == 0) or num == 0:
    print("The number is positive and even or  zero")
else:
    print("The  condition not satisfied")

print("-------------------------------")

#input validation

num = input("Enter a number: ")
if num.isdigit():
    num = int(num)  
    
    if num > 0:
        print(f"{num} is positive")
    else:
        print(f"{num} is negative")
   
else:
    print("Invalid input! Please enter a valid number.")