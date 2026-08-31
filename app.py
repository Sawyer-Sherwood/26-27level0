print ("Hello, World!") 

# Hashtags in Python can be used for line comments 
# This will not run or interfere with the code in any way. 

# Our First Variable! 
first_name = "Bill" # note: this is a string. it is surrounded by quotes 
print(first_name) 
sport = "Cross Country" 

#fstrings -  Allow you to embed variable into strings. 
#print(f"") 
print(f"{first_name} likes {sport}") 

#int  (or integer) demo: 
age = 100 
# Bill likes cross country and he is 100 years old.
print(f"{first_name} likes {sport} and he is {age} years old") 

# Floats (decimal numbers) 
gpa = 1.89 
print(f"Unfortunately, {first_name} has a GPA of {gpa}")

# booleans (true/false) 
# more often used for conditional logic 
allowed_to_play = False 
print(f"Is {first_name} allowed to play? {allowed_to_play}") 

#demo of an if statement! 
if allowed_to_play: 
    print(f"{first_name} is allowed to play! Huzzah!") 
else:
    print(f"{first_name} is NOT allowed to play! What a bum.")
print_triangle = True
if print_triangle:
    print("   *   ")
    print("  ***  ")
    print(" ***** ")
    print("*******") 
else:
    print("*******") 
    print("*     *") 
    print("*     *") 
    print("*******") 

