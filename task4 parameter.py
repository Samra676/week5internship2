#Task 2:Write a function `greet_user(name, age)` that returns a greeting like: 'Hello Ali, you are 20 years old.'

def greet_user(name, age):
    return f"Hello {name}, you are {age} years old."

# Function ko call karna aur output print karna
message = greet_user("samra", 20)
print(message)
