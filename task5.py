#Task 1:Create a function `change_counter()` that modifies a global counter variable.
# Global variable 
counter = 7

def change_counter():
    global counter
    counter += 1  # Counter ko 1 se increase kar raha hai

# Function ko call karna
print(f"Counter before: {counter}")
change_counter()
print(f"Counter after: {counter}")
