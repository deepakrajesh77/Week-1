# Declare Variables
user_name = "Deepak"
user_age = 18
user_height = 180

# Experiment with Types
integer_value = 10
float_value = 3.14
string_value = "Hello"
boolean_value = True

# Check Types
print("type of username:", type(user_name))
print("type of user_age:", type(user_age))
print("type of user_height:", type(user_height))
print("type of integer_value:", type(integer_value))
print("type of float_value:", type(float_value))
print("type of string_value:", type(string_value))
print("type of boolean_value:", type(boolean_value))

# Practice Casting
string_number = "25"
converted_int = int(string_number)
print("converted integer:", converted_int, "type:", type(converted_int))

number = 150
converted_str = str(number)
print("converted string:", converted_str, "type:", type(converted_str))

# String Formatting
print(f"My name is {user_name}, I am {user_age} years old and my height is {user_height}.")

# Input Task
birth_year = input("Enter your birth year: ")
birth_year = int(birth_year)

current_year = 2026
age = current_year - birth_year

print(f"You are {age} years old.")