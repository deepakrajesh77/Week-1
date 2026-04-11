#Basic for loop

for number in range(1,11):
    print(number)
print("------------------------")

#String Iteration

name="deepak"
for letter in name:
    print(letter)
print("------------------------")

#The while loop

count=10
while count>0:
    print(count)
    count-=1
print("------------------------")

#Sum of numbers

total=0
for number in range(1,51):
    total+=number
print("Sum of numbers from 1 to 50 is:", total)

#break and continue statements

for number in range(1,11):
    if number==7:
        break
    print(number)
print("------------------------")



for number in range(1,11):
    if number==5:
        continue
    print(number)
print("------------------------")

#nested loops

for i in range(5):
    for j in range(5):
       print("*", end="")
    print()